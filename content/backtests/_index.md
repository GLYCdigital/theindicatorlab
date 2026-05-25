---
title: "Indicator Backtests"
date: 2026-05-25
draft: false
type: backtests
layout: list
description: "Real backtest results for popular TradingView indicators. 5+ years of historical data. No opinions — just numbers."
---

## 10 Indicators · 8 Assets · 5-Year Data

<div class="indicator-cards">
<div class="indicator-card">
    <h3><a href="/backtests/bollinger-band-squeeze-tsla/">BollingerBands</a> 🟢</h3>
    <p class="card-best">Best: <strong>TSLA</strong> — +131.5% return, 0.53 Sharpe</p>
    <p class="card-assets">Tested on: TSLA, QQQ, AAPL, BTC-USD, ETH-USD, SPY</p>
</div><div class="indicator-card">
    <h3><a href="/backtests/donchian-channel-breakout-aapl/">Donchian</a> 🔴</h3>
    <p class="card-best">Best: <strong>AAPL</strong> — +0.0% return, 0.00 Sharpe</p>
    <p class="card-assets">Tested on: AAPL, BTC-USD, ETH-USD, GC=F, QQQ, SPY, TSLA</p>
</div><div class="indicator-card">
    <h3><a href="/backtests/ema-ribbon-qqq/">EMA</a> 🟢</h3>
    <p class="card-best">Best: <strong>QQQ</strong> — +81.5% return, 0.67 Sharpe</p>
    <p class="card-assets">Tested on: QQQ, BTC-USD, SPY, AAPL, ETH-USD</p>
</div><div class="indicator-card">
    <h3><a href="/backtests/ichimoku-cloud-qqq/">Ichimoku</a> 🟢</h3>
    <p class="card-best">Best: <strong>QQQ</strong> — +64.6% return, 0.54 Sharpe</p>
    <p class="card-assets">Tested on: QQQ, SPY, BTC-USD, ETH-USD, EURUSD=X</p>
</div><div class="indicator-card">
    <h3><a href="/backtests/macd-crossover-tsla/">MACD</a> 🟢</h3>
    <p class="card-best">Best: <strong>TSLA</strong> — +334.6% return, 0.66 Sharpe</p>
    <p class="card-assets">Tested on: TSLA, BTC-USD, AAPL, GC=F, ETH-USD, QQQ, SPY, EURUSD=X</p>
</div><div class="indicator-card">
    <h3><a href="/backtests/rsi-oversold-overbought-aapl/">RSI</a> 🟢</h3>
    <p class="card-best">Best: <strong>AAPL</strong> — +75.5% return, 0.52 Sharpe</p>
    <p class="card-assets">Tested on: AAPL, SPY, QQQ, BTC-USD, ETH-USD, TSLA, EURUSD=X</p>
</div><div class="indicator-card">
    <h3><a href="/backtests/parabolic-sar-aapl/">SAR</a> 🟡</h3>
    <p class="card-best">Best: <strong>AAPL</strong> — +43.1% return, 0.31 Sharpe</p>
    <p class="card-assets">Tested on: AAPL, QQQ, SPY, BTC-USD, ETH-USD, EURUSD=X</p>
</div><div class="indicator-card">
    <h3><a href="/backtests/golden-cross-qqq/">SMA</a> 🟢</h3>
    <p class="card-best">Best: <strong>QQQ</strong> — +110.3% return, 0.80 Sharpe</p>
    <p class="card-assets">Tested on: QQQ, SPY, GC=F, BTC-USD, AAPL, TSLA</p>
</div><div class="indicator-card">
    <h3><a href="/backtests/stochastic-crossover-btc-usd/">Stochastic</a> 🟡</h3>
    <p class="card-best">Best: <strong>BTC</strong> — +22.4% return, 0.22 Sharpe</p>
    <p class="card-assets">Tested on: BTC-USD, ETH-USD, SPY, QQQ, EURUSD=X</p>
</div><div class="indicator-card">
    <h3><a href="/backtests/volume-spike-breakout-eth-usd/">Volume</a> 🟢</h3>
    <p class="card-best">Best: <strong>ETH</strong> — +50.3% return, 0.56 Sharpe</p>
    <p class="card-assets">Tested on: ETH-USD, TSLA, BTC-USD, SPY, AAPL, QQQ</p>
</div>
</div>

## Methodology

All backtests run on **5 years of daily OHLCV data** from Yahoo Finance using the **backtrader** engine. Starting capital: $10,000, 95% position sizing, 0.1% commission per trade. No curve-fitting.

## FAQ

**Are these results real?** Yes. Every number comes from an actual backtest against historical price data.

**Can I copy these signals?** Past performance doesn't guarantee future results. Educational use only.

**How often are results updated?** Weekly. Every Saturday we refresh all existing backtests and add new indicators.

<style>
.indicator-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 1.2rem;
  margin: 1.5rem 0;
}
.indicator-card {
  background: var(--card-background, #f6f8fa);
  border-radius: 10px;
  padding: 1.3rem 1.5rem;
  transition: box-shadow 0.2s;
}
.indicator-card:hover {
  box-shadow: 0 2px 12px rgba(0,0,0,0.08);
}
.indicator-card h3 {
  margin: 0 0 0.5rem;
  font-size: 1.15rem;
}
.indicator-card h3 a {
  color: var(--accent-color, #1a73e8);
  text-decoration: none;
}
.indicator-card .card-best {
  margin: 0 0 0.4rem;
  font-size: 0.92rem;
  color: var(--text-color, #333);
}
.indicator-card .card-assets {
  margin: 0;
  font-size: 0.78rem;
  color: var(--text-secondary, #888);
}
</style>
