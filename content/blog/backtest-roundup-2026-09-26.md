---
title: "Weekly Backtest Roundup (Sep 26, 2026)"
description: "Backtest results for 18 trading indicators across 4 asset classes. 101 total tests. Top performer: EMA Ribbon (+13.2% CAGR)."
date: 2026-09-26
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
| Profitable tests | 72 / 101 (71%) |
| Average CAGR | +2.5% |
| Average Sharpe | -0.06 |

## Top Performers (by Sharpe Ratio)

| # | Strategy | Asset | CAGR | Sharpe | Win Rate | Profit Factor | Trades |
|---|----------|-------|------|--------|----------|--------------|--------|
| 1 | EMA Ribbon | QQQ | +13.2% | 0.74 | 37.5% | 3.86 | 16 |
| 2 | Volume Spike Breakout | ETH | +10.1% | 0.74 | 56.7% | 2.43 | 30 |
| 3 | Whale Liquidity / Absorption Profil | ETH | +10.1% | 0.74 | 56.7% | 2.43 | 30 |
| 4 | Liquidity Sweep Pro | AAPL | +12.2% | 0.67 | 41.6% | 1.51 | 89 |
| 5 | RSI Oversold/Overbought | AAPL | +14.0% | 0.60 | 33.3% | 1.85 | 12 |
| 6 | MACD Crossover | TSLA | +29.2% | 0.58 | 34.0% | 1.94 | 47 |
| 7 | Ichimoku Cloud | QQQ | +10.0% | 0.55 | 42.1% | 2.45 | 19 |
| 8 | Ichimoku Cloud | SPY | +8.8% | 0.53 | 57.9% | 2.99 | 19 |

## Top Performers (by CAGR)

| # | Strategy | Asset | CAGR | Sharpe | Win Rate | Profit Factor | Trades |
|---|----------|-------|------|--------|----------|--------------|--------|
| 1 | MACD Crossover | TSLA | +29.2% | 0.58 | 34.0% | 1.94 | 47 |
| 2 | EMA Ribbon | BTC | +15.1% | 0.43 | 29.4% | 1.51 | 34 |
| 3 | Golden Cross | BTC | +14.1% | 0.40 | 60.0% | 3.54 | 5 |
| 4 | RSI Oversold/Overbought | AAPL | +14.0% | 0.60 | 33.3% | 1.85 | 12 |
| 5 | Volume Profile Pro | ETH | +13.5% | 0.44 | 21.6% | 1.31 | 102 |
| 6 | EMA Ribbon | QQQ | +13.2% | 0.74 | 37.5% | 3.86 | 16 |
| 7 | Liquidity Sweep Pro | AAPL | +12.2% | 0.67 | 41.6% | 1.51 | 89 |
| 8 | RSI Oversold/Overbought | QQQ | +11.7% | 0.43 | 37.5% | 1.88 | 8 |

## By Asset Class

- **Stocks** (US equities (SPY, QQQ, AAPL, TSLA)): 57 tests, avg CAGR +3.8%, avg Sharpe -0.01
- **Crypto** (crypto (BTC/USD, ETH/USD)): 35 tests, avg CAGR +1.4%, avg Sharpe 0.11
- **Forex** (forex (EUR/USD, GBP/USD)): 7 tests, avg CAGR -4.2%, avg Sharpe -1.43

## Best in Each Asset Class

**Stocks**: [EMA Ribbon](/backtests/ema-ribbon/) on QQQ — +13.2% CAGR, Sharpe 0.74
**Crypto**: [Volume Spike Breakout](/backtests/volume-spike-breakout/) on ETH — +10.1% CAGR, Sharpe 0.74
**Forex**: [Ichimoku Cloud](/backtests/ichimoku-cloud/) on EURUSD — +0.3% CAGR, Sharpe -0.38

## Underperformers

Not every strategy works everywhere. These combinations struggled this testing period:

| # | Strategy | Asset | CAGR | Sharpe | Win Rate | Profit Factor | Trades |
|---|----------|-------|------|--------|----------|--------------|--------|
| 1 | SuperTrend + ATR Trailing Stop | ETH | -13.5% | -0.54 | 36.5% | 0.91 | 466 |
| 2 | Parabolic SAR | ETH | -16.5% | -0.34 | 33.3% | 0.74 | 75 |
| 3 | Fisher Transform MTF Divergence | ETH | -20.5% | -0.90 | 34.2% | 0.84 | 339 |

## This Week's Takeaway

The gap between the top and bottom performers is widening. Strategies with a clear edge (strong trend following, disciplined exits) continue to compound. Ones without a filter (trading every signal regardless of market regime) are bleeding in choppy conditions.

---

*Backtest period: 5-year historical data. Past performance does not guarantee future results. All tests use long-only entry with standard stop-loss parameters. See individual backtest pages for methodology and full trade logs.*

📊 Browse all backtests at the [Backtest Archive](/backtests/)
