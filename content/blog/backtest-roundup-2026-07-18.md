---
title: "Weekly Backtest Roundup (Jul 18, 2026)"
description: "Backtest results for 17 trading indicators across 4 asset classes. 100 total tests. Top performer: MACD Crossover (+33.3% CAGR)."
date: 2026-07-18
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
| Average CAGR | +2.6% |
| Average Sharpe | -0.07 |

## Top Performers (by Sharpe Ratio)

| # | Strategy | Asset | CAGR | Sharpe | Win Rate | Profit Factor | Trades |
|---|----------|-------|------|--------|----------|--------------|--------|
| 1 | MACD Crossover | TSLA | +33.3% | 0.65 | 33.3% | 1.89 | 48 |
| 2 | EMA Ribbon | QQQ | +12.1% | 0.64 | 37.5% | 2.85 | 16 |
| 3 | RSI Oversold/Overbought | AAPL | +13.5% | 0.58 | 33.3% | 1.85 | 12 |
| 4 | Liquidity Sweep Pro | AAPL | +11.4% | 0.56 | 37.6% | 1.43 | 93 |
| 5 | Volume Spike Breakout | ETH | +8.3% | 0.54 | 55.2% | 2.13 | 29 |
| 6 | Whale Liquidity / Absorption Profil | ETH | +8.3% | 0.54 | 55.2% | 2.13 | 29 |
| 7 | Bollinger Band Squeeze | AAPL | +11.2% | 0.47 | 43.1% | 1.62 | 51 |
| 8 | CVD Divergence Alerts | AAPL | +11.2% | 0.47 | 43.1% | 1.62 | 51 |

## Top Performers (by CAGR)

| # | Strategy | Asset | CAGR | Sharpe | Win Rate | Profit Factor | Trades |
|---|----------|-------|------|--------|----------|--------------|--------|
| 1 | MACD Crossover | TSLA | +33.3% | 0.65 | 33.3% | 1.89 | 48 |
| 2 | EMA Ribbon | BTC | +15.6% | 0.44 | 34.4% | 1.73 | 32 |
| 3 | Bollinger Band Squeeze | TSLA | +15.4% | 0.45 | 29.9% | 1.31 | 67 |
| 4 | TTM Squeeze Pro | TSLA | +15.4% | 0.45 | 29.9% | 1.31 | 67 |
| 5 | RSI Oversold/Overbought | AAPL | +13.5% | 0.58 | 33.3% | 1.85 | 12 |
| 6 | EMA Ribbon | QQQ | +12.1% | 0.64 | 37.5% | 2.85 | 16 |
| 7 | Volume Profile Pro | ETH | +11.6% | 0.40 | 21.0% | 1.21 | 100 |
| 8 | Liquidity Sweep Pro | AAPL | +11.4% | 0.56 | 37.6% | 1.43 | 93 |

## By Asset Class

- **Stocks** (US equities (SPY, QQQ, AAPL, TSLA)): 57 tests, avg CAGR +4.7%, avg Sharpe 0.01
- **Crypto** (crypto (BTC/USD, ETH/USD)): 34 tests, avg CAGR +0.3%, avg Sharpe 0.07
- **Forex** (forex (EUR/USD, GBP/USD)): 7 tests, avg CAGR -4.5%, avg Sharpe -1.58

## Best in Each Asset Class

**Stocks**: [MACD Crossover](/backtests/macd-crossover/) on TSLA — +33.3% CAGR, Sharpe 0.65
**Crypto**: [Volume Spike Breakout](/backtests/volume-spike-breakout/) on ETH — +8.3% CAGR, Sharpe 0.54
**Forex**: [Ichimoku Cloud](/backtests/ichimoku-cloud/) on EURUSD — -0.4% CAGR, Sharpe -0.45

## Underperformers

Not every strategy works everywhere. These combinations struggled this testing period:

| # | Strategy | Asset | CAGR | Sharpe | Win Rate | Profit Factor | Trades |
|---|----------|-------|------|--------|----------|--------------|--------|
| 1 | RSI Oversold/Overbought | ETH | -12.2% | -0.03 | 14.3% | 0.64 | 21 |
| 2 | SuperTrend + ATR Trailing Stop | ETH | -16.8% | -0.73 | 36.2% | 0.91 | 467 |
| 3 | Fisher Transform MTF Divergence | ETH | -19.4% | -0.62 | 34.3% | 0.87 | 338 |

## This Week's Takeaway

The gap between the top and bottom performers is widening. Strategies with a clear edge (strong trend following, disciplined exits) continue to compound. Ones without a filter (trading every signal regardless of market regime) are bleeding in choppy conditions.

---

*Backtest period: 5-year historical data. Past performance does not guarantee future results. All tests use long-only entry with standard stop-loss parameters. See individual backtest pages for methodology and full trade logs.*

📊 Browse all backtests at the [Backtest Archive](/backtests/)
