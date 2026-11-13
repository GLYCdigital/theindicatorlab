---
title: "Weekly Backtest Roundup (Nov 14, 2026)"
description: "Backtest results for 18 trading indicators across 4 asset classes. 101 total tests. Top performer: Volume Spike Breakout (+10.1% CAGR)."
date: 2026-11-14
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
| Profitable tests | 65 / 101 (64%) |
| Average CAGR | +1.2% |
| Average Sharpe | -0.11 |

## Top Performers (by Sharpe Ratio)

| # | Strategy | Asset | CAGR | Sharpe | Win Rate | Profit Factor | Trades |
|---|----------|-------|------|--------|----------|--------------|--------|
| 1 | Volume Spike Breakout | ETH | +10.1% | 0.74 | 56.7% | 2.43 | 30 |
| 2 | Whale Liquidity / Absorption Profil | ETH | +10.1% | 0.74 | 56.7% | 2.43 | 30 |
| 3 | EMA Ribbon | QQQ | +12.3% | 0.68 | 37.5% | 3.70 | 16 |
| 4 | RSI Oversold/Overbought | AAPL | +15.2% | 0.63 | 33.3% | 1.85 | 12 |
| 5 | MACD Crossover | TSLA | +28.5% | 0.57 | 36.2% | 1.65 | 47 |
| 6 | Ichimoku Cloud | QQQ | +9.2% | 0.50 | 40.0% | 2.15 | 20 |
| 7 | Ichimoku Cloud | SPY | +8.5% | 0.50 | 52.6% | 2.85 | 19 |
| 8 | Liquidity Sweep Pro | AAPL | +8.6% | 0.46 | 42.2% | 1.38 | 90 |

## Top Performers (by CAGR)

| # | Strategy | Asset | CAGR | Sharpe | Win Rate | Profit Factor | Trades |
|---|----------|-------|------|--------|----------|--------------|--------|
| 1 | MACD Crossover | TSLA | +28.5% | 0.57 | 36.2% | 1.65 | 47 |
| 2 | RSI Oversold/Overbought | AAPL | +15.2% | 0.63 | 33.3% | 1.85 | 12 |
| 3 | EMA Ribbon | BTC | +13.2% | 0.39 | 31.4% | 1.60 | 35 |
| 4 | Volume Profile Pro | ETH | +12.5% | 0.43 | 23.0% | 1.31 | 100 |
| 5 | EMA Ribbon | QQQ | +12.3% | 0.68 | 37.5% | 3.70 | 16 |
| 6 | Volume Spike Breakout | ETH | +10.1% | 0.74 | 56.7% | 2.43 | 30 |
| 7 | Whale Liquidity / Absorption Profil | ETH | +10.1% | 0.74 | 56.7% | 2.43 | 30 |
| 8 | Golden Cross | BTC | +9.9% | 0.31 | 60.0% | 3.54 | 5 |

## By Asset Class

- **Stocks** (US equities (SPY, QQQ, AAPL, TSLA)): 57 tests, avg CAGR +2.6%, avg Sharpe -0.07
- **Crypto** (crypto (BTC/USD, ETH/USD)): 35 tests, avg CAGR -0.2%, avg Sharpe 0.06
- **Forex** (forex (EUR/USD, GBP/USD)): 7 tests, avg CAGR -4.2%, avg Sharpe -1.34

## Best in Each Asset Class

**Stocks**: [EMA Ribbon](/backtests/ema-ribbon/) on QQQ — +12.3% CAGR, Sharpe 0.68
**Crypto**: [Volume Spike Breakout](/backtests/volume-spike-breakout/) on ETH — +10.1% CAGR, Sharpe 0.74
**Forex**: [Ichimoku Cloud](/backtests/ichimoku-cloud/) on EURUSD — +0.7% CAGR, Sharpe -0.33

## Underperformers

Not every strategy works everywhere. These combinations struggled this testing period:

| # | Strategy | Asset | CAGR | Sharpe | Win Rate | Profit Factor | Trades |
|---|----------|-------|------|--------|----------|--------------|--------|
| 1 | SuperTrend + ATR Trailing Stop | ETH | -18.2% | -0.82 | 36.0% | 0.89 | 470 |
| 2 | Parabolic SAR | ETH | -21.1% | -0.54 | 32.4% | 0.67 | 74 |
| 3 | Fisher Transform MTF Divergence | ETH | -24.8% | -1.20 | 33.2% | 0.79 | 337 |

## This Week's Takeaway

The gap between the top and bottom performers is widening. Strategies with a clear edge (strong trend following, disciplined exits) continue to compound. Ones without a filter (trading every signal regardless of market regime) are bleeding in choppy conditions.

---

*Backtest period: 5-year historical data. Past performance does not guarantee future results. All tests use long-only entry with standard stop-loss parameters. See individual backtest pages for methodology and full trade logs.*

📊 Browse all backtests at the [Backtest Archive](/backtests/)
