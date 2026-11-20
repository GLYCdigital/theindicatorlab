---
title: "Weekly Backtest Roundup (Nov 21, 2026)"
description: "Backtest results for 18 trading indicators across 4 asset classes. 101 total tests. Top performer: Volume Spike Breakout (+10.1% CAGR)."
date: 2026-11-21
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
| Profitable tests | 64 / 101 (63%) |
| Average CAGR | +1.1% |
| Average Sharpe | -0.11 |

## Top Performers (by Sharpe Ratio)

| # | Strategy | Asset | CAGR | Sharpe | Win Rate | Profit Factor | Trades |
|---|----------|-------|------|--------|----------|--------------|--------|
| 1 | Volume Spike Breakout | ETH | +10.1% | 0.74 | 56.7% | 2.43 | 30 |
| 2 | Whale Liquidity / Absorption Profil | ETH | +10.1% | 0.74 | 56.7% | 2.43 | 30 |
| 3 | EMA Ribbon | QQQ | +12.3% | 0.68 | 37.5% | 3.70 | 16 |
| 4 | RSI Oversold/Overbought | AAPL | +14.4% | 0.61 | 33.3% | 1.85 | 12 |
| 5 | MACD Crossover | TSLA | +26.4% | 0.54 | 35.4% | 1.62 | 48 |
| 6 | Ichimoku Cloud | QQQ | +9.2% | 0.50 | 40.0% | 2.15 | 20 |
| 7 | Ichimoku Cloud | SPY | +8.5% | 0.50 | 52.6% | 2.85 | 19 |
| 8 | Volume Profile Pro | ETH | +13.8% | 0.47 | 23.2% | 1.33 | 99 |

## Top Performers (by CAGR)

| # | Strategy | Asset | CAGR | Sharpe | Win Rate | Profit Factor | Trades |
|---|----------|-------|------|--------|----------|--------------|--------|
| 1 | MACD Crossover | TSLA | +26.4% | 0.54 | 35.4% | 1.62 | 48 |
| 2 | RSI Oversold/Overbought | AAPL | +14.4% | 0.61 | 33.3% | 1.85 | 12 |
| 3 | Volume Profile Pro | ETH | +13.8% | 0.47 | 23.2% | 1.33 | 99 |
| 4 | EMA Ribbon | BTC | +13.1% | 0.39 | 31.4% | 1.59 | 35 |
| 5 | EMA Ribbon | QQQ | +12.3% | 0.68 | 37.5% | 3.70 | 16 |
| 6 | Volume Spike Breakout | ETH | +10.1% | 0.74 | 56.7% | 2.43 | 30 |
| 7 | Whale Liquidity / Absorption Profil | ETH | +10.1% | 0.74 | 56.7% | 2.43 | 30 |
| 8 | Ichimoku Cloud | QQQ | +9.2% | 0.50 | 40.0% | 2.15 | 20 |

## By Asset Class

- **Stocks** (US equities (SPY, QQQ, AAPL, TSLA)): 57 tests, avg CAGR +2.3%, avg Sharpe -0.08
- **Crypto** (crypto (BTC/USD, ETH/USD)): 35 tests, avg CAGR -0.0%, avg Sharpe 0.06
- **Forex** (forex (EUR/USD, GBP/USD)): 7 tests, avg CAGR -4.3%, avg Sharpe -1.34

## Best in Each Asset Class

**Stocks**: [EMA Ribbon](/backtests/ema-ribbon/) on QQQ — +12.3% CAGR, Sharpe 0.68
**Crypto**: [Volume Spike Breakout](/backtests/volume-spike-breakout/) on ETH — +10.1% CAGR, Sharpe 0.74
**Forex**: [Ichimoku Cloud](/backtests/ichimoku-cloud/) on EURUSD — +0.7% CAGR, Sharpe -0.33

## Underperformers

Not every strategy works everywhere. These combinations struggled this testing period:

| # | Strategy | Asset | CAGR | Sharpe | Win Rate | Profit Factor | Trades |
|---|----------|-------|------|--------|----------|--------------|--------|
| 1 | SuperTrend + ATR Trailing Stop | ETH | -19.8% | -0.90 | 35.7% | 0.87 | 471 |
| 2 | Parabolic SAR | ETH | -23.1% | -0.62 | 31.1% | 0.62 | 74 |
| 3 | Fisher Transform MTF Divergence | ETH | -26.0% | -1.27 | 32.9% | 0.78 | 337 |

## This Week's Takeaway

The gap between the top and bottom performers is widening. Strategies with a clear edge (strong trend following, disciplined exits) continue to compound. Ones without a filter (trading every signal regardless of market regime) are bleeding in choppy conditions.

---

*Backtest period: 5-year historical data. Past performance does not guarantee future results. All tests use long-only entry with standard stop-loss parameters. See individual backtest pages for methodology and full trade logs.*

📊 Browse all backtests at the [Backtest Archive](/backtests/)
