---
title: "Weekly Backtest Roundup (Aug 29, 2026)"
description: "Backtest results for 17 trading indicators across 4 asset classes. 100 total tests. Top performer: Volume Spike Breakout (+10.1% CAGR)."
date: 2026-08-29
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
| Profitable tests | 71 / 100 (71%) |
| Average CAGR | +2.9% |
| Average Sharpe | -0.05 |

## Top Performers (by Sharpe Ratio)

| # | Strategy | Asset | CAGR | Sharpe | Win Rate | Profit Factor | Trades |
|---|----------|-------|------|--------|----------|--------------|--------|
| 1 | Volume Spike Breakout | ETH | +10.1% | 0.74 | 56.7% | 2.43 | 30 |
| 2 | Whale Liquidity / Absorption Profil | ETH | +10.1% | 0.74 | 56.7% | 2.43 | 30 |
| 3 | EMA Ribbon | QQQ | +11.9% | 0.62 | 37.5% | 3.52 | 16 |
| 4 | Liquidity Sweep Pro | AAPL | +10.9% | 0.61 | 40.0% | 1.46 | 90 |
| 5 | Volume Profile Pro | ETH | +17.2% | 0.59 | 21.6% | 1.25 | 102 |
| 6 | Donchian Channel Breakout | GC=F | +9.5% | 0.56 | 36.2% | 1.64 | 69 |
| 7 | MACD Crossover | TSLA | +27.5% | 0.56 | 32.6% | 1.80 | 46 |
| 8 | Ichimoku Cloud | SPY | +9.1% | 0.54 | 52.6% | 2.96 | 19 |

## Top Performers (by CAGR)

| # | Strategy | Asset | CAGR | Sharpe | Win Rate | Profit Factor | Trades |
|---|----------|-------|------|--------|----------|--------------|--------|
| 1 | MACD Crossover | TSLA | +27.5% | 0.56 | 32.6% | 1.80 | 46 |
| 2 | Volume Profile Pro | ETH | +17.2% | 0.59 | 21.6% | 1.25 | 102 |
| 3 | EMA Ribbon | BTC | +13.5% | 0.40 | 29.4% | 1.51 | 34 |
| 4 | EMA Ribbon | QQQ | +11.9% | 0.62 | 37.5% | 3.52 | 16 |
| 5 | RSI Oversold/Overbought | AAPL | +11.5% | 0.45 | 30.8% | 1.69 | 13 |
| 6 | Liquidity Sweep Pro | AAPL | +10.9% | 0.61 | 40.0% | 1.46 | 90 |
| 7 | Volume Spike Breakout | ETH | +10.1% | 0.74 | 56.7% | 2.43 | 30 |
| 8 | Whale Liquidity / Absorption Profil | ETH | +10.1% | 0.74 | 56.7% | 2.43 | 30 |

## By Asset Class

- **Stocks** (US equities (SPY, QQQ, AAPL, TSLA)): 57 tests, avg CAGR +3.7%, avg Sharpe -0.01
- **Crypto** (crypto (BTC/USD, ETH/USD)): 34 tests, avg CAGR +2.9%, avg Sharpe 0.17
- **Forex** (forex (EUR/USD, GBP/USD)): 7 tests, avg CAGR -4.3%, avg Sharpe -1.50

## Best in Each Asset Class

**Stocks**: [EMA Ribbon](/backtests/ema-ribbon/) on QQQ — +11.9% CAGR, Sharpe 0.62
**Crypto**: [Volume Spike Breakout](/backtests/volume-spike-breakout/) on ETH — +10.1% CAGR, Sharpe 0.74
**Forex**: [Ichimoku Cloud](/backtests/ichimoku-cloud/) on EURUSD — -0.1% CAGR, Sharpe -0.41

## Underperformers

Not every strategy works everywhere. These combinations struggled this testing period:

| # | Strategy | Asset | CAGR | Sharpe | Win Rate | Profit Factor | Trades |
|---|----------|-------|------|--------|----------|--------------|--------|
| 1 | RSI Oversold/Overbought | TSLA | -11.6% | -0.13 | 20.0% | 0.37 | 15 |
| 2 | Parabolic SAR | ETH | -15.7% | -0.31 | 32.9% | 0.71 | 73 |
| 3 | Fisher Transform MTF Divergence | ETH | -19.7% | -0.81 | 34.1% | 0.86 | 340 |

## This Week's Takeaway

The gap between the top and bottom performers is widening. Strategies with a clear edge (strong trend following, disciplined exits) continue to compound. Ones without a filter (trading every signal regardless of market regime) are bleeding in choppy conditions.

---

*Backtest period: 5-year historical data. Past performance does not guarantee future results. All tests use long-only entry with standard stop-loss parameters. See individual backtest pages for methodology and full trade logs.*

📊 Browse all backtests at the [Backtest Archive](/backtests/)
