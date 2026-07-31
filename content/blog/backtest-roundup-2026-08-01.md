---
title: "Weekly Backtest Roundup (Aug 01, 2026)"
description: "Backtest results for 17 trading indicators across 4 asset classes. 100 total tests. Top performer: MACD Crossover (+34.4% CAGR)."
date: 2026-08-01
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
| Average CAGR | +1.9% |
| Average Sharpe | -0.10 |

## Top Performers (by Sharpe Ratio)

| # | Strategy | Asset | CAGR | Sharpe | Win Rate | Profit Factor | Trades |
|---|----------|-------|------|--------|----------|--------------|--------|
| 1 | MACD Crossover | TSLA | +34.4% | 0.67 | 34.8% | 1.91 | 46 |
| 2 | EMA Ribbon | QQQ | +11.9% | 0.62 | 43.8% | 3.43 | 16 |
| 3 | Liquidity Sweep Pro | AAPL | +9.3% | 0.54 | 39.6% | 1.58 | 91 |
| 4 | Volume Spike Breakout | ETH | +8.3% | 0.54 | 55.2% | 2.13 | 29 |
| 5 | Whale Liquidity / Absorption Profil | ETH | +8.3% | 0.54 | 55.2% | 2.13 | 29 |
| 6 | RSI Oversold/Overbought | AAPL | +11.3% | 0.49 | 33.3% | 1.85 | 12 |
| 7 | Ichimoku Cloud | QQQ | +9.3% | 0.47 | 42.1% | 2.37 | 19 |
| 8 | Ichimoku Cloud | SPY | +8.0% | 0.45 | 50.0% | 2.77 | 20 |

## Top Performers (by CAGR)

| # | Strategy | Asset | CAGR | Sharpe | Win Rate | Profit Factor | Trades |
|---|----------|-------|------|--------|----------|--------------|--------|
| 1 | MACD Crossover | TSLA | +34.4% | 0.67 | 34.8% | 1.91 | 46 |
| 2 | Bollinger Band Squeeze | TSLA | +14.9% | 0.44 | 28.1% | 1.31 | 64 |
| 3 | EMA Ribbon | BTC | +14.9% | 0.43 | 33.3% | 1.65 | 33 |
| 4 | TTM Squeeze Pro | TSLA | +14.9% | 0.44 | 28.1% | 1.31 | 64 |
| 5 | Volume Profile Pro | ETH | +12.9% | 0.44 | 21.8% | 1.22 | 101 |
| 6 | EMA Ribbon | QQQ | +11.9% | 0.62 | 43.8% | 3.43 | 16 |
| 7 | RSI Oversold/Overbought | AAPL | +11.3% | 0.49 | 33.3% | 1.85 | 12 |
| 8 | RSI Oversold/Overbought | QQQ | +9.4% | 0.35 | 33.3% | 1.79 | 9 |

## By Asset Class

- **Stocks** (US equities (SPY, QQQ, AAPL, TSLA)): 57 tests, avg CAGR +3.8%, avg Sharpe -0.02
- **Crypto** (crypto (BTC/USD, ETH/USD)): 34 tests, avg CAGR -0.4%, avg Sharpe 0.05
- **Forex** (forex (EUR/USD, GBP/USD)): 7 tests, avg CAGR -4.5%, avg Sharpe -1.56

## Best in Each Asset Class

**Stocks**: [MACD Crossover](/backtests/macd-crossover/) on TSLA — +34.4% CAGR, Sharpe 0.67
**Crypto**: [Volume Spike Breakout](/backtests/volume-spike-breakout/) on ETH — +8.3% CAGR, Sharpe 0.54
**Forex**: [Ichimoku Cloud](/backtests/ichimoku-cloud/) on EURUSD — -0.2% CAGR, Sharpe -0.42

## Underperformers

Not every strategy works everywhere. These combinations struggled this testing period:

| # | Strategy | Asset | CAGR | Sharpe | Win Rate | Profit Factor | Trades |
|---|----------|-------|------|--------|----------|--------------|--------|
| 1 | Parabolic SAR | ETH | -17.0% | -0.31 | 35.1% | 0.78 | 74 |
| 2 | SuperTrend + ATR Trailing Stop | ETH | -17.6% | -0.79 | 36.4% | 0.90 | 467 |
| 3 | Fisher Transform MTF Divergence | ETH | -20.9% | -0.69 | 34.2% | 0.86 | 339 |

## This Week's Takeaway

The gap between the top and bottom performers is widening. Strategies with a clear edge (strong trend following, disciplined exits) continue to compound. Ones without a filter (trading every signal regardless of market regime) are bleeding in choppy conditions.

---

*Backtest period: 5-year historical data. Past performance does not guarantee future results. All tests use long-only entry with standard stop-loss parameters. See individual backtest pages for methodology and full trade logs.*

📊 Browse all backtests at the [Backtest Archive](/backtests/)
