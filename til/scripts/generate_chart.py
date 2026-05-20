#!/usr/bin/env python3
"""
Generate TradingView-style indicator chart images for review cards.
Uses real stock data + mplfinance to create consistent, dark-themed charts.

Usage:
    python3 generate_chart.py <slug> <indicator_type> [ticker]

    slug:            e.g. "awesome-oscillator"
    indicator_type:  awesome-oscillator | rsi | macd | bollinger-bands | supertrend |
                     ichimoku-cloud | cvd-divergence | supertrend-atr | fisher-transform
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

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '../../static/screenshots')
os.makedirs(OUTPUT_DIR, exist_ok=True)

DEFAULT_TICKERS = {
    "awesome-oscillator": "AAPL",
    "rsi": "TSLA",
    "macd": "MSFT",
    "bollinger-bands": "AMZN",
    "supertrend": "GOOGL",
    "ichimoku-cloud": "BTC-USD",
    "cvd-divergence": "NVDA",
    "supertrend-atr": "TSLA",
    "fisher-transform": "AAPL",
}

mc = mpf.make_marketcolors(up='#26a69a', down='#ef5350', edge='inherit', wick='inherit', volume='inherit')
style = mpf.make_mpf_style(marketcolors=mc, gridstyle='', figcolor='#1a1b2e', facecolor='#1a1b2e')

# ── Fisher Transform helper ──────────────────────────────────────────
def fisher_transform(src, length=10):
    """Compute Fisher Transform of a price series."""
    max_h = src.rolling(length).max()
    min_l = src.rolling(length).min()
    denom = max_h - min_l
    denom = denom.replace(0, np.nan)
    value = 2 * ((src - min_l) / denom) - 1
    # Smooth
    smooth = pd.Series(0.0, index=value.index)
    alpha = 0.66
    for i in range(1, len(value)):
        if pd.notna(value.iloc[i]):
            prev = smooth.iloc[i-1] if pd.notna(smooth.iloc[i-1]) else 0
            smooth.iloc[i] = alpha * value.iloc[i] + (1 - alpha) * prev
    smooth = smooth.clip(-0.999, 0.999)
    fisher = pd.Series(0.0, index=smooth.index)
    for i in range(1, len(smooth)):
        if pd.notna(smooth.iloc[i]) and abs(smooth.iloc[i]) < 1:
            prev = fisher.iloc[i-1] if pd.notna(fisher.iloc[i-1]) else 0
            fisher.iloc[i] = 0.5 * np.log((1 + smooth.iloc[i]) / (1 - smooth.iloc[i])) + 0.5 * prev
    fisher = fisher.clip(-5, 5)
    trigger = fisher.shift(1)
    return fisher, trigger


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
    df['Volume'] = df['Volume'].astype(float)

    apds = []
    kwargs = dict(type='candle', style=style, volume=True, tight_layout=True,
                  figsize=(12, 7), savefig=f"{OUTPUT_DIR}/{slug}.png",
                  title=f"{ticker} — {indicator_type.replace('-',' ').title()}", ylabel='Price')

    # ── Existing types ──────────────────────────────────────────────
    if indicator_type == "awesome-oscillator":
        df['med'] = (df['High'] + df['Low']) / 2
        df['ao'] = df['med'].rolling(5).mean() - df['med'].rolling(34).mean()
        colors = ['#26a69a' if v >= 0 else '#ef5350' for v in df['ao'].values]
        apds = [mpf.make_addplot(df['ao'], type='bar', panel=1, color=colors, ylabel='AO', alpha=0.7)]

    elif indicator_type == "rsi":
        delta = df['Close'].diff()
        gain = delta.where(delta > 0, 0).rolling(14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(14).mean()
        rs = gain / loss
        df['rsi'] = 100 - (100 / (1 + rs))
        apds = [mpf.make_addplot(df['rsi'], panel=1, color='#7c4dff', ylabel='RSI')]
        kwargs['hlines'] = dict(hlines=[70, 30], colors=['#ef5350', '#26a69a'], linestyle='--')

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
        kwargs['fill_between'] = dict(y1=df['upper'].values, y2=df['lower'].values, alpha=0.1, color='#7c4dff')

    elif indicator_type == "supertrend":
        atr_period, mult = 10, 3.0
        hl = (df['High'] + df['Low']) / 2
        tr = pd.concat([df['High'] - df['Low'],
                        abs(df['High'] - df['Close'].shift(1)),
                        abs(df['Low'] - df['Close'].shift(1))], axis=1).max(axis=1)
        atr = tr.rolling(atr_period).mean()
        df['upper'] = hl + mult * atr
        df['lower'] = hl - mult * atr
        apds = [
            mpf.make_addplot(df['upper'], color='#ef5350', linestyle='--', width=0.8, alpha=0.6),
            mpf.make_addplot(df['lower'], color='#26a69a', linestyle='--', width=0.8, alpha=0.6),
        ]

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
        kwargs['fill_between'] = dict(y1=senkou_a.values, y2=senkou_b.values, alpha=0.2, color='#26a69a')

    # ── CVD Divergence Alerts ───────────────────────────────────────
    elif indicator_type == "cvd-divergence":
        # Approximate CVD: cumulative (close-open) * volume normalized
        df['delta'] = (df['Close'] - df['Open']) / df['Open'] * df['Volume']
        df['cvd'] = df['delta'].cumsum() / df['Volume'].mean() * 100
        # Rising vs falling for color
        cvd_colors = ['#26a69a' if df['cvd'].iloc[i] >= df['cvd'].iloc[i-1]
                     else '#ef5350' for i in range(len(df['cvd']))]
        apds = [
            mpf.make_addplot(df['cvd'], type='bar', panel=1, color=cvd_colors,
                           ylabel='CVD', alpha=0.8, width=0.8),
        ]

    # ── SuperTrend + ATR Trailing Stop ───────────────────────────────
    elif indicator_type == "supertrend-atr":
        # SuperTrend
        atr_period, mult = 10, 3.0
        hl = (df['High'] + df['Low']) / 2
        tr = pd.concat([df['High'] - df['Low'],
                        abs(df['High'] - df['Close'].shift(1)),
                        abs(df['Low'] - df['Close'].shift(1))], axis=1).max(axis=1)
        atr = tr.rolling(atr_period).mean()
        df['st_upper'] = hl + mult * atr
        df['st_lower'] = hl - mult * atr

        # ATR Trailing Stop (separate, wider)
        stop_mult = 2.0
        stop_atr_period = 14
        stop_atr = tr.rolling(stop_atr_period).mean()
        df['trail_high'] = df['High'].rolling(20).max()
        df['trail_low'] = df['Low'].rolling(20).min()
        df['atr_stop_up'] = df['trail_high'] - stop_mult * stop_atr  # long stop
        df['atr_stop_down'] = df['trail_low'] + stop_mult * stop_atr  # short stop

        apds = [
            mpf.make_addplot(df['st_upper'], color='#ef5350', linestyle='--', width=1.0, alpha=0.5),
            mpf.make_addplot(df['st_lower'], color='#00bcd4', linestyle='--', width=1.0, alpha=0.5),
            mpf.make_addplot(df['atr_stop_up'], color='#ff9800', linestyle='-', width=0.8, alpha=0.7),
        ]

    # ── Fisher Transform MTF Divergence ──────────────────────────────
    elif indicator_type == "fisher-transform":
        src = (df['High'] + df['Low']) / 2
        fisher, trigger = fisher_transform(src, length=10)

        # Simulate HTF Fisher (e.g. weekly on daily) — use longer window
        htf_fisher, _ = fisher_transform(src, length=21)

        ob_level = 1.5
        os_level = -1.5

        apds = [
            mpf.make_addplot(fisher, panel=1, color='#00bcd4', width=1.2, ylabel='Fisher'),
            mpf.make_addplot(trigger, panel=1, color='#666666', linestyle='--', width=0.6),
            mpf.make_addplot(htf_fisher, panel=1, color='#ff9800', linestyle=':', width=1.0),
        ]

        # OB/OS hlines on panel 1
        kwargs['hlines'] = dict(hlines=[ob_level, os_level, 0],
                                colors=['#ef5350', '#26a69a', '#555555'],
                                linestyle='--', alpha=0.4)

    else:
        raise ValueError(f"Unknown indicator type: {indicator_type}")

    # Build final kwargs
    final_kwargs = {k: v for k, v in kwargs.items() if k not in ('savefig', 'title', 'ylabel')}
    mpf.plot(df, addplot=apds, savefig=f"{OUTPUT_DIR}/{slug}.png",
             title=kwargs.get('title', ''), ylabel=kwargs.get('ylabel', ''),
             **{k: v for k, v in final_kwargs.items() if k in
                ['type','style','volume','tight_layout','figsize','hlines','fill_between']})
    print(f"✅ Saved {OUTPUT_DIR}/{slug}.png")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate indicator chart images")
    parser.add_argument("slug", help="URL slug for the review")
    parser.add_argument("type", choices=list(DEFAULT_TICKERS.keys()), help="Indicator type")
    parser.add_argument("ticker", nargs="?", default=None, help="Stock ticker (optional)")
    args = parser.parse_args()
    generate(args.slug, args.type, args.ticker)
