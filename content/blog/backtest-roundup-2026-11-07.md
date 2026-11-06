---
title: "Weekly Backtest Roundup (Nov 07, 2026)"
description: "Backtest results for 18 trading indicators across 4 asset classes. 101 total tests. Top performer: Volume Spike Breakout (+10.1% CAGR)."
date: 2026-11-07
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
| Profitable tests | 64 / 101 (63%) |
| Average CAGR | +0.9% |
| Average Sharpe | -0.12 |

## Top Performers (by Sharpe Ratio)

| # | Strategy | Asset | CAGR | Sharpe | Win Rate | Profit Factor | Trades |
|---|----------|-------|------|--------|----------|--------------|--------|
| 1 | Volume Spike Breakout | ETH | +10.1% | 0.74 | 56.7% | 2.43 | 30 |
| 2 | Whale Liquidity / Absorption Profil | ETH | +10.1% | 0.74 | 56.7% | 2.43 | 30 |
| 3 | EMA Ribbon | QQQ | +12.3% | 0.69 | 37.5% | 3.73 | 16 |
| 4 | RSI Oversold/Overbought | AAPL | +14.3% | 0.61 | 33.3% | 1.85 | 12 |
| 5 | MACD Crossover | TSLA | +28.5% | 0.57 | 36.2% | 1.65 | 47 |
| 6 | Ichimoku Cloud | QQQ | +9.2% | 0.50 | 40.0% | 2.15 | 20 |
| 7 | Ichimoku Cloud | SPY | +8.5% | 0.50 | 52.6% | 2.85 | 19 |
| 8 | Liquidity Sweep Pro | AAPL | +8.2% | 0.44 | 42.7% | 1.42 | 89 |

## Top Performers (by CAGR)

| # | Strategy | Asset | CAGR | Sharpe | Win Rate | Profit Factor | Trades |
|---|----------|-------|------|--------|----------|--------------|--------|
| 1 | MACD Crossover | TSLA | +28.5% | 0.57 | 36.2% | 1.65 | 47 |
| 2 | RSI Oversold/Overbought | AAPL | +14.3% | 0.61 | 33.3% | 1.85 | 12 |
| 3 | EMA Ribbon | BTC | +13.6% | 0.40 | 31.4% | 1.61 | 35 |
| 4 | EMA Ribbon | QQQ | +12.3% | 0.69 | 37.5% | 3.73 | 16 |
| 5 | Golden Cross | BTC | +11.9% | 0.35 | 60.0% | 3.54 | 5 |
| 6 | Volume Profile Pro | ETH | +11.1% | 0.38 | 22.8% | 1.27 | 101 |
| 7 | Volume Spike Breakout | ETH | +10.1% | 0.74 | 56.7% | 2.43 | 30 |
| 8 | Whale Liquidity / Absorption Profil | ETH | +10.1% | 0.74 | 56.7% | 2.43 | 30 |

## By Asset Class

- **Stocks** (US equities (SPY, QQQ, AAPL, TSLA)): 57 tests, avg CAGR +2.2%, avg Sharpe -0.09
- **Crypto** (crypto (BTC/USD, ETH/USD)): 35 tests, avg CAGR -0.3%, avg Sharpe 0.06
- **Forex** (forex (EUR/USD, GBP/USD)): 7 tests, avg CAGR -4.2%, avg Sharpe -1.35

## Best in Each Asset Class

**Stocks**: [EMA Ribbon](/backtests/ema-ribbon/) on QQQ — +12.3% CAGR, Sharpe 0.69
**Crypto**: [Volume Spike Breakout](/backtests/volume-spike-breakout/) on ETH — +10.1% CAGR, Sharpe 0.74
**Forex**: [Ichimoku Cloud](/backtests/ichimoku-cloud/) on EURUSD — +0.7% CAGR, Sharpe -0.33

## Underperformers

Not every strategy works everywhere. These combinations struggled this testing period:

| # | Strategy | Asset | CAGR | Sharpe | Win Rate | Profit Factor | Trades |
|---|----------|-------|------|--------|----------|--------------|--------|
| 1 | SuperTrend + ATR Trailing Stop | ETH | -17.1% | -0.78 | 36.0% | 0.89 | 470 |
| 2 | Parabolic SAR | ETH | -22.1% | -0.58 | 32.0% | 0.64 | 75 |
| 3 | Fisher Transform MTF Divergence | ETH | -24.4% | -1.16 | 33.1% | 0.80 | 338 |

## This Week's Takeaway

The gap between the top and bottom performers is widening. Strategies with a clear edge (strong trend following, disciplined exits) continue to compound. Ones without a filter (trading every signal regardless of market regime) are bleeding in choppy conditions.

---

*Backtest period: 5-year historical data. Past performance does not guarantee future results. All tests use long-only entry with standard stop-loss parameters. See individual backtest pages for methodology and full trade logs.*

📊 Browse all backtests at the [Backtest Archive](/backtests/)
