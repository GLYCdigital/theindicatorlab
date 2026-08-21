---
title: "Weekly Backtest Roundup (Aug 22, 2026)"
description: "Backtest results for 17 trading indicators across 4 asset classes. 100 total tests. Top performer: Volume Spike Breakout (+9.8% CAGR)."
date: 2026-08-22
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
| Profitable tests | 74 / 100 (74%) |
| Average CAGR | +3.2% |
| Average Sharpe | -0.04 |

## Top Performers (by Sharpe Ratio)

| # | Strategy | Asset | CAGR | Sharpe | Win Rate | Profit Factor | Trades |
|---|----------|-------|------|--------|----------|--------------|--------|
| 1 | Volume Spike Breakout | ETH | +9.8% | 0.71 | 53.3% | 2.13 | 30 |
| 2 | Whale Liquidity / Absorption Profil | ETH | +9.8% | 0.71 | 53.3% | 2.13 | 30 |
| 3 | MACD Crossover | TSLA | +36.4% | 0.70 | 34.0% | 1.90 | 47 |
| 4 | Donchian Channel Breakout | GC=F | +10.3% | 0.63 | 36.2% | 1.64 | 69 |
| 5 | EMA Ribbon | QQQ | +11.8% | 0.61 | 37.5% | 3.52 | 16 |
| 6 | Liquidity Sweep Pro | AAPL | +10.2% | 0.59 | 40.0% | 1.46 | 90 |
| 7 | Volume Profile Pro | ETH | +15.6% | 0.53 | 21.4% | 1.23 | 103 |
| 8 | RSI Oversold/Overbought | AAPL | +12.0% | 0.52 | 33.3% | 1.85 | 12 |

## Top Performers (by CAGR)

| # | Strategy | Asset | CAGR | Sharpe | Win Rate | Profit Factor | Trades |
|---|----------|-------|------|--------|----------|--------------|--------|
| 1 | MACD Crossover | TSLA | +36.4% | 0.70 | 34.0% | 1.90 | 47 |
| 2 | Bollinger Band Squeeze | TSLA | +16.2% | 0.47 | 27.7% | 1.31 | 65 |
| 3 | TTM Squeeze Pro | TSLA | +16.2% | 0.47 | 27.7% | 1.31 | 65 |
| 4 | Volume Profile Pro | ETH | +15.6% | 0.53 | 21.4% | 1.23 | 103 |
| 5 | MACD Crossover | BTC | +14.1% | 0.43 | 33.8% | 1.25 | 68 |
| 6 | EMA Ribbon | BTC | +13.4% | 0.40 | 29.4% | 1.51 | 34 |
| 7 | RSI Oversold/Overbought | AAPL | +12.0% | 0.52 | 33.3% | 1.85 | 12 |
| 8 | EMA Ribbon | QQQ | +11.8% | 0.61 | 37.5% | 3.52 | 16 |

## By Asset Class

- **Stocks** (US equities (SPY, QQQ, AAPL, TSLA)): 57 tests, avg CAGR +4.2%, avg Sharpe -0.01
- **Crypto** (crypto (BTC/USD, ETH/USD)): 34 tests, avg CAGR +2.7%, avg Sharpe 0.16
- **Forex** (forex (EUR/USD, GBP/USD)): 7 tests, avg CAGR -4.1%, avg Sharpe -1.48

## Best in Each Asset Class

**Stocks**: [MACD Crossover](/backtests/macd-crossover/) on TSLA — +36.4% CAGR, Sharpe 0.70
**Crypto**: [Volume Spike Breakout](/backtests/volume-spike-breakout/) on ETH — +9.8% CAGR, Sharpe 0.71
**Forex**: [Ichimoku Cloud](/backtests/ichimoku-cloud/) on EURUSD — +0.1% CAGR, Sharpe -0.39

## Underperformers

Not every strategy works everywhere. These combinations struggled this testing period:

| # | Strategy | Asset | CAGR | Sharpe | Win Rate | Profit Factor | Trades |
|---|----------|-------|------|--------|----------|--------------|--------|
| 1 | SuperTrend + ATR Trailing Stop | ETH | -13.7% | -0.56 | 36.5% | 0.90 | 463 |
| 2 | Parabolic SAR | ETH | -14.9% | -0.27 | 33.8% | 0.74 | 74 |
| 3 | Fisher Transform MTF Divergence | ETH | -19.2% | -0.81 | 33.9% | 0.84 | 339 |

## This Week's Takeaway

The gap between the top and bottom performers is widening. Strategies with a clear edge (strong trend following, disciplined exits) continue to compound. Ones without a filter (trading every signal regardless of market regime) are bleeding in choppy conditions.

---

*Backtest period: 5-year historical data. Past performance does not guarantee future results. All tests use long-only entry with standard stop-loss parameters. See individual backtest pages for methodology and full trade logs.*

📊 Browse all backtests at the [Backtest Archive](/backtests/)
