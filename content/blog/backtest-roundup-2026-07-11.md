---
title: "Weekly Backtest Roundup (Jul 11, 2026)"
description: "Backtest results for 17 trading indicators across 4 asset classes. 100 total tests. Top performer: EMA Ribbon (+12.9% CAGR)."
date: 2026-07-11
draft: false
type: blog
image: "/images/til-og-default.png"
tags:
  - backtest roundup
  - trading indicators
  - quantitative analysis
  - strategy testing
  - tradingview
author: "The Indicator Lab"
---

We run weekly backtests on 18+ trading indicators across stocks, crypto, forex, and futures — 5 years of historical data, real execution, no curve-fitting. Here's what this week's numbers say.

## The Numbers

| Metric | Value |
|--------|-------|
| Indicators tested | 17 |
| Total backtests | 100 |
| Profitable tests | 67 / 100 (67%) |
| Average CAGR | +2.6% |
| Average Sharpe | -0.07 |

## Top Performers (by Sharpe Ratio)

| # | Strategy | Asset | CAGR | Sharpe | Win Rate | Profit Factor | Trades |
|---|----------|-------|------|--------|----------|--------------|--------|
| 1 | EMA Ribbon | QQQ | +12.9% | 0.68 | 37.5% | 2.85 | 16 |
| 2 | MACD Crossover | TSLA | +33.6% | 0.65 | 34.7% | 2.01 | 49 |
| 3 | Liquidity Sweep Pro | AAPL | +10.3% | 0.54 | 37.6% | 1.43 | 93 |
| 4 | RSI Oversold/Overbought | AAPL | +12.3% | 0.54 | 33.3% | 1.85 | 12 |
| 5 | Volume Spike Breakout | ETH | +8.3% | 0.54 | 55.2% | 2.13 | 29 |
| 6 | Whale Liquidity / Absorption Profil | ETH | +8.3% | 0.54 | 55.2% | 2.13 | 29 |
| 7 | Ichimoku Cloud | QQQ | +10.4% | 0.52 | 42.1% | 2.73 | 19 |
| 8 | Bollinger Band Squeeze | TSLA | +15.9% | 0.46 | 29.9% | 1.34 | 67 |

## Top Performers (by CAGR)

| # | Strategy | Asset | CAGR | Sharpe | Win Rate | Profit Factor | Trades |
|---|----------|-------|------|--------|----------|--------------|--------|
| 1 | MACD Crossover | TSLA | +33.6% | 0.65 | 34.7% | 2.01 | 49 |
| 2 | Bollinger Band Squeeze | TSLA | +15.9% | 0.46 | 29.9% | 1.34 | 67 |
| 3 | TTM Squeeze Pro | TSLA | +15.9% | 0.46 | 29.9% | 1.34 | 67 |
| 4 | EMA Ribbon | BTC | +15.6% | 0.44 | 34.4% | 1.73 | 32 |
| 5 | EMA Ribbon | QQQ | +12.9% | 0.68 | 37.5% | 2.85 | 16 |
| 6 | RSI Oversold/Overbought | AAPL | +12.3% | 0.54 | 33.3% | 1.85 | 12 |
| 7 | Donchian Channel Breakout | TSLA | +11.5% | 0.36 | 32.4% | 1.19 | 71 |
| 8 | Market Structure Pro | TSLA | +11.5% | 0.36 | 32.4% | 1.19 | 71 |

## By Asset Class

- **Stocks** (US equities (SPY, QQQ, AAPL, TSLA)): 57 tests, avg CAGR +4.7%, avg Sharpe 0.01
- **Crypto** (crypto (BTC/USD, ETH/USD)): 34 tests, avg CAGR +0.5%, avg Sharpe 0.08
- **Forex** (forex (EUR/USD, GBP/USD)): 7 tests, avg CAGR -4.5%, avg Sharpe -1.61

## Best in Each Asset Class

**Stocks**: [EMA Ribbon](/backtests/ema-ribbon/) on QQQ — +12.9% CAGR, Sharpe 0.68
**Crypto**: [Volume Spike Breakout](/backtests/volume-spike-breakout/) on ETH — +8.3% CAGR, Sharpe 0.54
**Forex**: [Ichimoku Cloud](/backtests/ichimoku-cloud/) on EURUSD — -0.6% CAGR, Sharpe -0.49

## Underperformers

Not every strategy works everywhere. These combinations struggled this testing period:

| # | Strategy | Asset | CAGR | Sharpe | Win Rate | Profit Factor | Trades |
|---|----------|-------|------|--------|----------|--------------|--------|
| 1 | RSI Oversold/Overbought | ETH | -12.7% | -0.03 | 14.3% | 0.64 | 21 |
| 2 | SuperTrend + ATR Trailing Stop | ETH | -14.5% | -0.58 | 36.3% | 0.92 | 466 |
| 3 | Fisher Transform MTF Divergence | ETH | -17.9% | -0.50 | 34.7% | 0.89 | 337 |

## This Week's Takeaway

The gap between the top and bottom performers is widening. Strategies with a clear edge (strong trend following, disciplined exits) continue to compound. Ones without a filter (trading every signal regardless of market regime) are bleeding in choppy conditions.

---

*Backtest period: 5-year historical data. Past performance does not guarantee future results. All tests use long-only entry with standard stop-loss parameters. See individual backtest pages for methodology and full trade logs.*

📊 Browse all backtests at the [Backtest Archive](/backtests/)
