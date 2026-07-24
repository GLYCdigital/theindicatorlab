---
title: "Weekly Backtest Roundup (Jul 25, 2026)"
description: "Backtest results for 17 trading indicators across 4 asset classes. 100 total tests. Top performer: MACD Crossover (+34.9% CAGR)."
date: 2026-07-25
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
| Profitable tests | 65 / 100 (65%) |
| Average CAGR | +2.1% |
| Average Sharpe | -0.09 |

## Top Performers (by Sharpe Ratio)

| # | Strategy | Asset | CAGR | Sharpe | Win Rate | Profit Factor | Trades |
|---|----------|-------|------|--------|----------|--------------|--------|
| 1 | MACD Crossover | TSLA | +34.9% | 0.67 | 34.8% | 1.91 | 46 |
| 2 | EMA Ribbon | QQQ | +12.2% | 0.64 | 43.8% | 3.58 | 16 |
| 3 | RSI Oversold/Overbought | AAPL | +13.5% | 0.58 | 33.3% | 1.85 | 12 |
| 4 | Liquidity Sweep Pro | AAPL | +10.9% | 0.56 | 39.1% | 1.54 | 92 |
| 5 | Volume Spike Breakout | ETH | +8.3% | 0.54 | 55.2% | 2.13 | 29 |
| 6 | Whale Liquidity / Absorption Profil | ETH | +8.3% | 0.54 | 55.2% | 2.13 | 29 |
| 7 | Bollinger Band Squeeze | AAPL | +11.4% | 0.48 | 44.0% | 1.63 | 50 |
| 8 | CVD Divergence Alerts | AAPL | +11.4% | 0.48 | 44.0% | 1.63 | 50 |

## Top Performers (by CAGR)

| # | Strategy | Asset | CAGR | Sharpe | Win Rate | Profit Factor | Trades |
|---|----------|-------|------|--------|----------|--------------|--------|
| 1 | MACD Crossover | TSLA | +34.9% | 0.67 | 34.8% | 1.91 | 46 |
| 2 | Bollinger Band Squeeze | TSLA | +15.3% | 0.45 | 28.8% | 1.31 | 66 |
| 3 | TTM Squeeze Pro | TSLA | +15.3% | 0.45 | 28.8% | 1.31 | 66 |
| 4 | EMA Ribbon | BTC | +15.0% | 0.43 | 33.3% | 1.73 | 33 |
| 5 | RSI Oversold/Overbought | AAPL | +13.5% | 0.58 | 33.3% | 1.85 | 12 |
| 6 | EMA Ribbon | QQQ | +12.2% | 0.64 | 43.8% | 3.58 | 16 |
| 7 | Volume Profile Pro | ETH | +11.9% | 0.41 | 21.0% | 1.21 | 100 |
| 8 | Bollinger Band Squeeze | AAPL | +11.4% | 0.48 | 44.0% | 1.63 | 50 |

## By Asset Class

- **Stocks** (US equities (SPY, QQQ, AAPL, TSLA)): 57 tests, avg CAGR +4.3%, avg Sharpe -0.00
- **Crypto** (crypto (BTC/USD, ETH/USD)): 34 tests, avg CAGR -0.3%, avg Sharpe 0.05
- **Forex** (forex (EUR/USD, GBP/USD)): 7 tests, avg CAGR -4.5%, avg Sharpe -1.57

## Best in Each Asset Class

**Stocks**: [MACD Crossover](/backtests/macd-crossover/) on TSLA — +34.9% CAGR, Sharpe 0.67
**Crypto**: [Volume Spike Breakout](/backtests/volume-spike-breakout/) on ETH — +8.3% CAGR, Sharpe 0.54
**Forex**: [Ichimoku Cloud](/backtests/ichimoku-cloud/) on EURUSD — -0.4% CAGR, Sharpe -0.45

## Underperformers

Not every strategy works everywhere. These combinations struggled this testing period:

| # | Strategy | Asset | CAGR | Sharpe | Win Rate | Profit Factor | Trades |
|---|----------|-------|------|--------|----------|--------------|--------|
| 1 | SuperTrend + ATR Trailing Stop | ETH | -17.4% | -0.78 | 36.3% | 0.90 | 466 |
| 2 | Parabolic SAR | ETH | -17.8% | -0.37 | 33.3% | 0.73 | 72 |
| 3 | Fisher Transform MTF Divergence | ETH | -21.6% | -0.88 | 34.2% | 0.85 | 339 |

## This Week's Takeaway

The gap between the top and bottom performers is widening. Strategies with a clear edge (strong trend following, disciplined exits) continue to compound. Ones without a filter (trading every signal regardless of market regime) are bleeding in choppy conditions.

---

*Backtest period: 5-year historical data. Past performance does not guarantee future results. All tests use long-only entry with standard stop-loss parameters. See individual backtest pages for methodology and full trade logs.*

📊 Browse all backtests at the [Backtest Archive](/backtests/)
