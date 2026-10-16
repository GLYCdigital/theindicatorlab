---
title: "Weekly Backtest Roundup (Oct 17, 2026)"
description: "Backtest results for 18 trading indicators across 4 asset classes. 101 total tests. Top performer: Volume Spike Breakout (+10.1% CAGR)."
date: 2026-10-17
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
| Average CAGR | +1.7% |
| Average Sharpe | -0.10 |

## Top Performers (by Sharpe Ratio)

| # | Strategy | Asset | CAGR | Sharpe | Win Rate | Profit Factor | Trades |
|---|----------|-------|------|--------|----------|--------------|--------|
| 1 | Volume Spike Breakout | ETH | +10.1% | 0.74 | 56.7% | 2.43 | 30 |
| 2 | Whale Liquidity / Absorption Profil | ETH | +10.1% | 0.74 | 56.7% | 2.43 | 30 |
| 3 | EMA Ribbon | QQQ | +12.3% | 0.68 | 37.5% | 3.86 | 16 |
| 4 | Liquidity Sweep Pro | AAPL | +11.3% | 0.63 | 41.6% | 1.50 | 89 |
| 5 | RSI Oversold/Overbought | AAPL | +14.2% | 0.61 | 33.3% | 1.85 | 12 |
| 6 | MACD Crossover | TSLA | +29.5% | 0.58 | 34.0% | 1.83 | 47 |
| 7 | Ichimoku Cloud | SPY | +8.6% | 0.52 | 55.0% | 2.99 | 20 |
| 8 | Ichimoku Cloud | QQQ | +9.1% | 0.50 | 40.0% | 2.45 | 20 |

## Top Performers (by CAGR)

| # | Strategy | Asset | CAGR | Sharpe | Win Rate | Profit Factor | Trades |
|---|----------|-------|------|--------|----------|--------------|--------|
| 1 | MACD Crossover | TSLA | +29.5% | 0.58 | 34.0% | 1.83 | 47 |
| 2 | EMA Ribbon | BTC | +14.5% | 0.42 | 29.4% | 1.51 | 34 |
| 3 | RSI Oversold/Overbought | AAPL | +14.2% | 0.61 | 33.3% | 1.85 | 12 |
| 4 | Golden Cross | BTC | +13.4% | 0.39 | 60.0% | 3.54 | 5 |
| 5 | Volume Profile Pro | ETH | +12.5% | 0.42 | 22.5% | 1.34 | 102 |
| 6 | EMA Ribbon | QQQ | +12.3% | 0.68 | 37.5% | 3.86 | 16 |
| 7 | Liquidity Sweep Pro | AAPL | +11.3% | 0.63 | 41.6% | 1.50 | 89 |
| 8 | RSI Oversold/Overbought | QQQ | +10.7% | 0.39 | 37.5% | 1.88 | 8 |

## By Asset Class

- **Stocks** (US equities (SPY, QQQ, AAPL, TSLA)): 57 tests, avg CAGR +2.9%, avg Sharpe -0.06
- **Crypto** (crypto (BTC/USD, ETH/USD)): 35 tests, avg CAGR +0.6%, avg Sharpe 0.09
- **Forex** (forex (EUR/USD, GBP/USD)): 7 tests, avg CAGR -4.2%, avg Sharpe -1.43

## Best in Each Asset Class

**Stocks**: [EMA Ribbon](/backtests/ema-ribbon/) on QQQ — +12.3% CAGR, Sharpe 0.68
**Crypto**: [Volume Spike Breakout](/backtests/volume-spike-breakout/) on ETH — +10.1% CAGR, Sharpe 0.74
**Forex**: [Ichimoku Cloud](/backtests/ichimoku-cloud/) on EURUSD — +0.3% CAGR, Sharpe -0.38

## Underperformers

Not every strategy works everywhere. These combinations struggled this testing period:

| # | Strategy | Asset | CAGR | Sharpe | Win Rate | Profit Factor | Trades |
|---|----------|-------|------|--------|----------|--------------|--------|
| 1 | SuperTrend + ATR Trailing Stop | ETH | -16.4% | -0.72 | 36.0% | 0.89 | 469 |
| 2 | Parabolic SAR | ETH | -19.8% | -0.49 | 32.4% | 0.66 | 74 |
| 3 | Fisher Transform MTF Divergence | ETH | -22.7% | -1.04 | 33.6% | 0.82 | 339 |

## This Week's Takeaway

The gap between the top and bottom performers is widening. Strategies with a clear edge (strong trend following, disciplined exits) continue to compound. Ones without a filter (trading every signal regardless of market regime) are bleeding in choppy conditions.

---

*Backtest period: 5-year historical data. Past performance does not guarantee future results. All tests use long-only entry with standard stop-loss parameters. See individual backtest pages for methodology and full trade logs.*

📊 Browse all backtests at the [Backtest Archive](/backtests/)
