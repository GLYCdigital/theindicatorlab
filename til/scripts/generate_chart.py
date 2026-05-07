#!/usr/bin/env python3
"""
Generate TradingView-style indicator chart images for review cards.
Uses real stock data + mplfinance to create consistent, dark-themed charts.

Usage:
    python3 generate_chart.py <slug> <indicator_type> [ticker]

    slug:            e.g. "awesome-oscillator"
    indicator_type:  awesome-oscillator | rsi | macd | bollinger-bands | supertrend | ichimoku-cloud
    ticker:          optional, defaults to a predefined stock per indicator

Output:
    Saves PNG to theindicatorlab/static/screenshots/<slug>.png

Dependencies:
    pip install yfinance mplfinance pandas matplotlib
"""

import yfinance as yf
import mplfinance as mpf
import matplotlib
matplotlib.use('Agg')
import pandas as pd
import numpy as np
import os, sys, argparse

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '../../theindicatorlab/static/screenshots')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Each indicator type maps to a different stock for visual variety
DEFAULT_TICKERS = {
    "awesome-oscillator": "AAPL",
    "rsi": "TSLA",
    "macd": "MSFT",
    "bollinger-bands": "AMZN",
    "supertrend": "GOOGL",
    "ichimoku-cloud": "BTC-USD",
}

mc = mpf.make_marketcolors(up='#26a69a', down='#ef5350', edge='inherit', wick='inherit', volume='inherit')
style = mpf.make_mpf_style(marketcolors=mc, gridstyle='', figcolor='#1a1b2e', facecolor='#1a1b2e')


def generate(slug: str, indicator_type: str, ticker: str = None):
    if not ticker:
        ticker = DEFAULT_TICKERS.get(indicator_type, "AAPL")

    print(f"Downloading {ticker}...")
    raw = yf.download(ticker, period="4mo", interval="1d", progress=False)

    if isinstance(raw.columns, pd.MultiIndex):
        raw.columns = raw.columns.get_level_values(0)

    df = raw.copy()
    for col in ['Open', 'High', 'Low', 'Close', 'Volume']:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    df = df.dropna()

    apds = []

    if indicator_type == "awesome-oscillator":
        df['med'] = (df['High'] + df['Low']) / 2
        df['ao'] = df['med'].rolling(5).mean() - df['med'].rolling(34).mean()
        colors = ['#26a69a' if v >= 0 else '#ef5350' for v in df['ao'].values]
        apds = [mpf.make_addplot(df['ao'], type='bar', panel=1, color=colors, ylabel='Awesome Osc', alpha=0.7)]
        mpf.plot(df, type='candle', style=style, addplot=apds, volume=True,
                savefig=f"{OUTPUT_DIR}/{slug}.png", tight_layout=True, figsize=(12, 7))

    elif indicator_type == "rsi":
        delta = df['Close'].diff()
        gain = delta.where(delta > 0, 0).rolling(14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(14).mean()
        rs = gain / loss
        df['rsi'] = 100 - (100 / (1 + rs))
        apds = [mpf.make_addplot(df['rsi'], panel=1, color='#7c4dff', ylabel='RSI')]
        mpf.plot(df, type='candle', style=style, addplot=apds, volume=True,
                hlines=dict(hlines=[70, 30], colors=['#ef5350', '#26a69a'], linestyle='--'),
                savefig=f"{OUTPUT_DIR}/{slug}.png", tight_layout=True, figsize=(12, 7))

    elif indicator_type == "macd":
        e1 = df['Close'].ewm(span=12).mean()
        e2 = df['Close'].ewm(span=26).mean()
        df['macd'] = e1 - e2
        df['sig'] = df['macd'].ewm(span=9).mean()
        df['hist'] = df['macd'] - df['sig']
        bar_colors = ['#26a69a' if v >= 0 else '#ef5350' for v in df['hist'].values]
        apds = [
            mpf.make_addplot(df['macd'], panel=1, color='#2979ff', ylabel='MACD'),
            mpf.make_addplot(df['sig'], panel=1, color='#ff6d00'),
            mpf.make_addplot(df['hist'], type='bar', panel=1, color=bar_colors, alpha=0.5),
        ]
        mpf.plot(df, type='candle', style=style, addplot=apds, volume=True,
                savefig=f"{OUTPUT_DIR}/{slug}.png", tight_layout=True, figsize=(12, 7))

    elif indicator_type == "bollinger-bands":
        df['sma'] = df['Close'].rolling(20).mean()
        std = df['Close'].rolling(20).std()
        df['upper'] = df['sma'] + 2 * std
        df['lower'] = df['sma'] - 2 * std
        apds = [
            mpf.make_addplot(df['sma'], color='#ff6d00', width=0.8),
            mpf.make_addplot(df['upper'], color='#7c4dff', linestyle='--', width=0.5),
            mpf.make_addplot(df['lower'], color='#7c4dff', linestyle='--', width=0.5),
        ]
        mpf.plot(df, type='candle', style=style, addplot=apds, volume=True,
                fill_between=dict(y1=df['upper'].values, y2=df['lower'].values, alpha=0.1, color='#7c4dff'),
                savefig=f"{OUTPUT_DIR}/{slug}.png", tight_layout=True, figsize=(12, 7))

    elif indicator_type == "supertrend":
        hl = (df['High'] + df['Low']) / 2
        atr = df['High'].rolling(10).max() - df['Low'].rolling(10).min()
        df['upper'] = hl + 3 * atr
        df['lower'] = hl - 3 * atr
        apds = [
            mpf.make_addplot(df['upper'], color='#ef5350', linestyle='--', width=0.8, alpha=0.6),
            mpf.make_addplot(df['lower'], color='#26a69a', linestyle='--', width=0.8, alpha=0.6),
        ]
        mpf.plot(df, type='candle', style=style, addplot=apds, volume=True,
                savefig=f"{OUTPUT_DIR}/{slug}.png", tight_layout=True, figsize=(12, 7))

    elif indicator_type == "ichimoku-cloud":
        high9 = df['High'].rolling(9).max()
        low9 = df['Low'].rolling(9).min()
        high26 = df['High'].rolling(26).max()
        low26 = df['Low'].rolling(26).min()
        high52 = df['High'].rolling(52).max()
        low52 = df['Low'].rolling(52).min()
        tenkan = (high9 + low9) / 2
        kijun = (high26 + low26) / 2
        senkou_a = ((tenkan + kijun) / 2).shift(26)
        senkou_b = ((high52 + low52) / 2).shift(26)
        chikou = df['Close'].shift(-26)
        apds = [
            mpf.make_addplot(tenkan, color='#ef5350', width=0.8),
            mpf.make_addplot(kijun, color='#2979ff', width=0.8),
            mpf.make_addplot(chikou, color='#ff6d00', width=0.8, alpha=0.5),
        ]
        mpf.plot(df, type='candle', style=style, addplot=apds, volume=True,
                fill_between=dict(y1=senkou_a.values, y2=senkou_b.values, alpha=0.2, color='#26a69a'),
                savefig=f"{OUTPUT_DIR}/{slug}.png", tight_layout=True, figsize=(12, 7))

    else:
        raise ValueError(f"Unknown indicator type: {indicator_type}")

    print(f"✅ Saved {OUTPUT_DIR}/{slug}.png")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate indicator chart images")
    parser.add_argument("slug", help="URL slug for the review")
    parser.add_argument("type", choices=list(DEFAULT_TICKERS.keys()), help="Indicator type")
    parser.add_argument("ticker", nargs="?", default=None, help="Stock ticker (optional)")
    args = parser.parse_args()
    generate(args.slug, args.type, args.ticker)
