---
title: "Weekly Backtest Roundup (Aug 15, 2026)"
description: "Backtest results for 17 trading indicators across 4 asset classes. 100 total tests. Top performer: MACD Crossover (+34.5% CAGR)."
date: 2026-08-15
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
| Average CAGR | +1.9% |
| Average Sharpe | -0.08 |

## Top Performers (by Sharpe Ratio)

| # | Strategy | Asset | CAGR | Sharpe | Win Rate | Profit Factor | Trades |
|---|----------|-------|------|--------|----------|--------------|--------|
| 1 | MACD Crossover | TSLA | +34.5% | 0.67 | 33.3% | 1.89 | 48 |
| 2 | EMA Ribbon | QQQ | +12.0% | 0.62 | 37.5% | 3.37 | 16 |
| 3 | Liquidity Sweep Pro | AAPL | +10.0% | 0.57 | 40.0% | 1.44 | 90 |
| 4 | Volume Spike Breakout | ETH | +8.3% | 0.54 | 55.2% | 2.13 | 29 |
| 5 | Whale Liquidity / Absorption Profil | ETH | +8.3% | 0.54 | 55.2% | 2.13 | 29 |
| 6 | Donchian Channel Breakout | GC=F | +9.1% | 0.52 | 36.2% | 1.64 | 69 |
| 7 | RSI Oversold/Overbought | AAPL | +11.7% | 0.51 | 33.3% | 1.85 | 12 |
| 8 | Ichimoku Cloud | SPY | +8.9% | 0.50 | 50.0% | 2.77 | 20 |

## Top Performers (by CAGR)

| # | Strategy | Asset | CAGR | Sharpe | Win Rate | Profit Factor | Trades |
|---|----------|-------|------|--------|----------|--------------|--------|
| 1 | MACD Crossover | TSLA | +34.5% | 0.67 | 33.3% | 1.89 | 48 |
| 2 | Bollinger Band Squeeze | TSLA | +14.9% | 0.44 | 27.7% | 1.31 | 65 |
| 3 | TTM Squeeze Pro | TSLA | +14.9% | 0.44 | 27.7% | 1.31 | 65 |
| 4 | EMA Ribbon | QQQ | +12.0% | 0.62 | 37.5% | 3.37 | 16 |
| 5 | RSI Oversold/Overbought | AAPL | +11.7% | 0.51 | 33.3% | 1.85 | 12 |
| 6 | Volume Profile Pro | ETH | +11.3% | 0.39 | 21.4% | 1.25 | 103 |
| 7 | RSI Oversold/Overbought | QQQ | +11.2% | 0.41 | 37.5% | 1.88 | 8 |
| 8 | EMA Ribbon | BTC | +11.0% | 0.35 | 30.3% | 1.51 | 33 |

## By Asset Class

- **Stocks** (US equities (SPY, QQQ, AAPL, TSLA)): 57 tests, avg CAGR +4.1%, avg Sharpe 0.00
- **Crypto** (crypto (BTC/USD, ETH/USD)): 34 tests, avg CAGR -0.8%, avg Sharpe 0.04
- **Forex** (forex (EUR/USD, GBP/USD)): 7 tests, avg CAGR -4.4%, avg Sharpe -1.53

## Best in Each Asset Class

**Stocks**: [MACD Crossover](/backtests/macd-crossover/) on TSLA — +34.5% CAGR, Sharpe 0.67
**Crypto**: [Volume Spike Breakout](/backtests/volume-spike-breakout/) on ETH — +8.3% CAGR, Sharpe 0.54
**Forex**: [Ichimoku Cloud](/backtests/ichimoku-cloud/) on EURUSD — -0.1% CAGR, Sharpe -0.42

## Underperformers

Not every strategy works everywhere. These combinations struggled this testing period:

| # | Strategy | Asset | CAGR | Sharpe | Win Rate | Profit Factor | Trades |
|---|----------|-------|------|--------|----------|--------------|--------|
| 1 | SuperTrend + ATR Trailing Stop | ETH | -15.7% | -0.64 | 36.6% | 0.91 | 465 |
| 2 | Parabolic SAR | ETH | -18.6% | -0.40 | 34.2% | 0.74 | 73 |
| 3 | Fisher Transform MTF Divergence | ETH | -21.0% | -0.66 | 34.2% | 0.86 | 339 |

## This Week's Takeaway

The gap between the top and bottom performers is widening. Strategies with a clear edge (strong trend following, disciplined exits) continue to compound. Ones without a filter (trading every signal regardless of market regime) are bleeding in choppy conditions.

---

*Backtest period: 5-year historical data. Past performance does not guarantee future results. All tests use long-only entry with standard stop-loss parameters. See individual backtest pages for methodology and full trade logs.*

📊 Browse all backtests at the [Backtest Archive](/backtests/)
