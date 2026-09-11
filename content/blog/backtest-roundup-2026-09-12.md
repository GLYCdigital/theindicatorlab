---
title: "Weekly Backtest Roundup (Sep 12, 2026)"
description: "Backtest results for 18 trading indicators across 4 asset classes. 101 total tests. Top performer: Volume Spike Breakout (+10.1% CAGR)."
date: 2026-09-12
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
| Indicators tested | 18 |
| Total backtests | 101 |
| Profitable tests | 74 / 101 (73%) |
| Average CAGR | +2.7% |
| Average Sharpe | -0.05 |

## Top Performers (by Sharpe Ratio)

| # | Strategy | Asset | CAGR | Sharpe | Win Rate | Profit Factor | Trades |
|---|----------|-------|------|--------|----------|--------------|--------|
| 1 | Volume Spike Breakout | ETH | +10.1% | 0.74 | 56.7% | 2.43 | 30 |
| 2 | Whale Liquidity / Absorption Profil | ETH | +10.1% | 0.74 | 56.7% | 2.43 | 30 |
| 3 | EMA Ribbon | QQQ | +12.7% | 0.71 | 40.0% | 4.01 | 15 |
| 4 | Liquidity Sweep Pro | AAPL | +11.3% | 0.64 | 41.1% | 1.49 | 90 |
| 5 | MACD Crossover | TSLA | +28.8% | 0.58 | 32.6% | 1.80 | 46 |
| 6 | Ichimoku Cloud | SPY | +8.8% | 0.53 | 57.9% | 2.99 | 19 |
| 7 | RSI Oversold/Overbought | AAPL | +13.5% | 0.51 | 30.8% | 1.84 | 13 |
| 8 | SuperTrend + ATR Trailing Stop | AAPL | +9.8% | 0.50 | 44.5% | 1.20 | 290 |

## Top Performers (by CAGR)

| # | Strategy | Asset | CAGR | Sharpe | Win Rate | Profit Factor | Trades |
|---|----------|-------|------|--------|----------|--------------|--------|
| 1 | MACD Crossover | TSLA | +28.8% | 0.58 | 32.6% | 1.80 | 46 |
| 2 | RSI Oversold/Overbought | AAPL | +13.5% | 0.51 | 30.8% | 1.84 | 13 |
| 3 | EMA Ribbon | BTC | +13.4% | 0.40 | 29.4% | 1.51 | 34 |
| 4 | Volume Profile Pro | ETH | +13.0% | 0.43 | 20.8% | 1.16 | 101 |
| 5 | EMA Ribbon | QQQ | +12.7% | 0.71 | 40.0% | 4.01 | 15 |
| 6 | Golden Cross | BTC | +12.4% | 0.36 | 60.0% | 3.54 | 5 |
| 7 | Liquidity Sweep Pro | AAPL | +11.3% | 0.64 | 41.1% | 1.49 | 90 |
| 8 | Bollinger Band Squeeze | AAPL | +10.7% | 0.46 | 43.1% | 1.58 | 51 |

## By Asset Class

- **Stocks** (US equities (SPY, QQQ, AAPL, TSLA)): 57 tests, avg CAGR +3.9%, avg Sharpe -0.00
- **Crypto** (crypto (BTC/USD, ETH/USD)): 35 tests, avg CAGR +1.8%, avg Sharpe 0.14
- **Forex** (forex (EUR/USD, GBP/USD)): 7 tests, avg CAGR -4.2%, avg Sharpe -1.43

## Best in Each Asset Class

**Stocks**: [EMA Ribbon](/backtests/ema-ribbon/) on QQQ — +12.7% CAGR, Sharpe 0.71
**Crypto**: [Volume Spike Breakout](/backtests/volume-spike-breakout/) on ETH — +10.1% CAGR, Sharpe 0.74
**Forex**: [Ichimoku Cloud](/backtests/ichimoku-cloud/) on EURUSD — +0.3% CAGR, Sharpe -0.38

## Underperformers

Not every strategy works everywhere. These combinations struggled this testing period:

| # | Strategy | Asset | CAGR | Sharpe | Win Rate | Profit Factor | Trades |
|---|----------|-------|------|--------|----------|--------------|--------|
| 1 | SuperTrend + ATR Trailing Stop | ETH | -12.4% | -0.47 | 36.5% | 0.93 | 466 |
| 2 | Parabolic SAR | ETH | -16.0% | -0.32 | 34.2% | 0.75 | 73 |
| 3 | Fisher Transform MTF Divergence | ETH | -18.0% | -0.58 | 34.3% | 0.88 | 338 |

## This Week's Takeaway

The gap between the top and bottom performers is widening. Strategies with a clear edge (strong trend following, disciplined exits) continue to compound. Ones without a filter (trading every signal regardless of market regime) are bleeding in choppy conditions.

---

*Backtest period: 5-year historical data. Past performance does not guarantee future results. All tests use long-only entry with standard stop-loss parameters. See individual backtest pages for methodology and full trade logs.*

📊 Browse all backtests at the [Backtest Archive](/backtests/)
