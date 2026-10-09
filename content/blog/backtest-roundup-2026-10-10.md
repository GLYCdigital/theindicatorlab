---
title: "Weekly Backtest Roundup (Oct 10, 2026)"
description: "Backtest results for 18 trading indicators across 4 asset classes. 101 total tests. Top performer: Volume Spike Breakout (+10.1% CAGR)."
date: 2026-10-10
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
| Profitable tests | 71 / 101 (70%) |
| Average CAGR | +2.0% |
| Average Sharpe | -0.08 |

## Top Performers (by Sharpe Ratio)

| # | Strategy | Asset | CAGR | Sharpe | Win Rate | Profit Factor | Trades |
|---|----------|-------|------|--------|----------|--------------|--------|
| 1 | Volume Spike Breakout | ETH | +10.1% | 0.74 | 56.7% | 2.43 | 30 |
| 2 | Whale Liquidity / Absorption Profil | ETH | +10.1% | 0.74 | 56.7% | 2.43 | 30 |
| 3 | EMA Ribbon | QQQ | +12.6% | 0.65 | 35.3% | 3.41 | 17 |
| 4 | Liquidity Sweep Pro | AAPL | +10.8% | 0.61 | 41.6% | 1.50 | 89 |
| 5 | RSI Oversold/Overbought | AAPL | +13.7% | 0.59 | 33.3% | 1.85 | 12 |
| 6 | Ichimoku Cloud | QQQ | +10.3% | 0.57 | 40.0% | 2.45 | 20 |
| 7 | MACD Crossover | TSLA | +28.4% | 0.57 | 33.3% | 1.87 | 48 |
| 8 | Ichimoku Cloud | SPY | +9.1% | 0.54 | 55.0% | 2.99 | 20 |

## Top Performers (by CAGR)

| # | Strategy | Asset | CAGR | Sharpe | Win Rate | Profit Factor | Trades |
|---|----------|-------|------|--------|----------|--------------|--------|
| 1 | MACD Crossover | TSLA | +28.4% | 0.57 | 33.3% | 1.87 | 48 |
| 2 | EMA Ribbon | BTC | +14.8% | 0.43 | 29.4% | 1.51 | 34 |
| 3 | Golden Cross | BTC | +13.8% | 0.40 | 60.0% | 3.54 | 5 |
| 4 | RSI Oversold/Overbought | AAPL | +13.7% | 0.59 | 33.3% | 1.85 | 12 |
| 5 | EMA Ribbon | QQQ | +12.6% | 0.65 | 35.3% | 3.41 | 17 |
| 6 | Volume Profile Pro | ETH | +12.5% | 0.42 | 22.5% | 1.34 | 102 |
| 7 | RSI Oversold/Overbought | QQQ | +11.8% | 0.43 | 37.5% | 1.88 | 8 |
| 8 | Liquidity Sweep Pro | AAPL | +10.8% | 0.61 | 41.6% | 1.50 | 89 |

## By Asset Class

- **Stocks** (US equities (SPY, QQQ, AAPL, TSLA)): 57 tests, avg CAGR +3.5%, avg Sharpe -0.03
- **Crypto** (crypto (BTC/USD, ETH/USD)): 35 tests, avg CAGR +0.7%, avg Sharpe 0.09
- **Forex** (forex (EUR/USD, GBP/USD)): 7 tests, avg CAGR -4.2%, avg Sharpe -1.44

## Best in Each Asset Class

**Stocks**: [EMA Ribbon](/backtests/ema-ribbon/) on QQQ — +12.6% CAGR, Sharpe 0.65
**Crypto**: [Volume Spike Breakout](/backtests/volume-spike-breakout/) on ETH — +10.1% CAGR, Sharpe 0.74
**Forex**: [Ichimoku Cloud](/backtests/ichimoku-cloud/) on EURUSD — +0.3% CAGR, Sharpe -0.38

## Underperformers

Not every strategy works everywhere. These combinations struggled this testing period:

| # | Strategy | Asset | CAGR | Sharpe | Win Rate | Profit Factor | Trades |
|---|----------|-------|------|--------|----------|--------------|--------|
| 1 | SuperTrend + ATR Trailing Stop | ETH | -15.4% | -0.64 | 36.2% | 0.89 | 467 |
| 2 | Parabolic SAR | ETH | -19.3% | -0.46 | 33.3% | 0.68 | 75 |
| 3 | Fisher Transform MTF Divergence | ETH | -22.2% | -1.09 | 33.9% | 0.82 | 339 |

## This Week's Takeaway

The gap between the top and bottom performers is widening. Strategies with a clear edge (strong trend following, disciplined exits) continue to compound. Ones without a filter (trading every signal regardless of market regime) are bleeding in choppy conditions.

---

*Backtest period: 5-year historical data. Past performance does not guarantee future results. All tests use long-only entry with standard stop-loss parameters. See individual backtest pages for methodology and full trade logs.*

📊 Browse all backtests at the [Backtest Archive](/backtests/)
