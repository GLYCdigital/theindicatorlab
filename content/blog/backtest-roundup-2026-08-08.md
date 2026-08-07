---
title: "Weekly Backtest Roundup (Aug 08, 2026)"
description: "Backtest results for 17 trading indicators across 4 asset classes. 100 total tests. Top performer: MACD Crossover (+34.0% CAGR)."
date: 2026-08-08
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
| Profitable tests | 68 / 100 (68%) |
| Average CAGR | +2.0% |
| Average Sharpe | -0.08 |

## Top Performers (by Sharpe Ratio)

| # | Strategy | Asset | CAGR | Sharpe | Win Rate | Profit Factor | Trades |
|---|----------|-------|------|--------|----------|--------------|--------|
| 1 | MACD Crossover | TSLA | +34.0% | 0.66 | 36.2% | 1.90 | 47 |
| 2 | EMA Ribbon | QQQ | +12.2% | 0.64 | 41.2% | 3.43 | 17 |
| 3 | Liquidity Sweep Pro | AAPL | +10.0% | 0.57 | 40.0% | 1.44 | 90 |
| 4 | Volume Spike Breakout | ETH | +8.3% | 0.54 | 55.2% | 2.13 | 29 |
| 5 | Whale Liquidity / Absorption Profil | ETH | +8.3% | 0.54 | 55.2% | 2.13 | 29 |
| 6 | RSI Oversold/Overbought | AAPL | +12.2% | 0.53 | 33.3% | 1.85 | 12 |
| 7 | Donchian Channel Breakout | GC=F | +8.9% | 0.50 | 36.2% | 1.64 | 69 |
| 8 | Ichimoku Cloud | SPY | +8.8% | 0.49 | 50.0% | 2.77 | 20 |

## Top Performers (by CAGR)

| # | Strategy | Asset | CAGR | Sharpe | Win Rate | Profit Factor | Trades |
|---|----------|-------|------|--------|----------|--------------|--------|
| 1 | MACD Crossover | TSLA | +34.0% | 0.66 | 36.2% | 1.90 | 47 |
| 2 | Bollinger Band Squeeze | TSLA | +14.9% | 0.44 | 28.1% | 1.31 | 64 |
| 3 | TTM Squeeze Pro | TSLA | +14.9% | 0.44 | 28.1% | 1.31 | 64 |
| 4 | EMA Ribbon | BTC | +14.3% | 0.42 | 33.3% | 1.63 | 33 |
| 5 | EMA Ribbon | QQQ | +12.2% | 0.64 | 41.2% | 3.43 | 17 |
| 6 | RSI Oversold/Overbought | AAPL | +12.2% | 0.53 | 33.3% | 1.85 | 12 |
| 7 | Volume Profile Pro | ETH | +11.0% | 0.38 | 21.8% | 1.23 | 101 |
| 8 | MACD Crossover | BTC | +10.8% | 0.35 | 34.8% | 1.26 | 66 |

## By Asset Class

- **Stocks** (US equities (SPY, QQQ, AAPL, TSLA)): 57 tests, avg CAGR +4.2%, avg Sharpe 0.00
- **Crypto** (crypto (BTC/USD, ETH/USD)): 34 tests, avg CAGR -0.7%, avg Sharpe 0.04
- **Forex** (forex (EUR/USD, GBP/USD)): 7 tests, avg CAGR -4.4%, avg Sharpe -1.53

## Best in Each Asset Class

**Stocks**: [MACD Crossover](/backtests/macd-crossover/) on TSLA — +34.0% CAGR, Sharpe 0.66
**Crypto**: [Volume Spike Breakout](/backtests/volume-spike-breakout/) on ETH — +8.3% CAGR, Sharpe 0.54
**Forex**: [Ichimoku Cloud](/backtests/ichimoku-cloud/) on EURUSD — -0.1% CAGR, Sharpe -0.42

## Underperformers

Not every strategy works everywhere. These combinations struggled this testing period:

| # | Strategy | Asset | CAGR | Sharpe | Win Rate | Profit Factor | Trades |
|---|----------|-------|------|--------|----------|--------------|--------|
| 1 | SuperTrend + ATR Trailing Stop | ETH | -16.5% | -0.71 | 36.7% | 0.91 | 466 |
| 2 | Parabolic SAR | ETH | -20.8% | -0.51 | 33.3% | 0.70 | 75 |
| 3 | Fisher Transform MTF Divergence | ETH | -20.9% | -0.68 | 34.1% | 0.86 | 340 |

## This Week's Takeaway

The gap between the top and bottom performers is widening. Strategies with a clear edge (strong trend following, disciplined exits) continue to compound. Ones without a filter (trading every signal regardless of market regime) are bleeding in choppy conditions.

---

*Backtest period: 5-year historical data. Past performance does not guarantee future results. All tests use long-only entry with standard stop-loss parameters. See individual backtest pages for methodology and full trade logs.*

📊 Browse all backtests at the [Backtest Archive](/backtests/)
