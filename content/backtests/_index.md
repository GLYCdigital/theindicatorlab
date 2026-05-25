---
title: "Indicator Backtests"
date: 2026-05-25
draft: false
type: backtests
layout: list
description: "Real backtest results for popular TradingView indicators. 5+ years of historical data. No opinions — just numbers."
---

<h2 id="indicators-tested" style="color:var(--navy-bar)">Indicators Backtested</h2>
<div class="lr-benefits">
      <div class="lr-benefit">
        <div class="icon">📉</div>
        <h4><a href="/backtests/bollinger-band-squeeze-tsla/" style="text-decoration:none;color:var(--text)">BollingerBands</a></h4>
        <p>6 assets tested · Best: TSLA (+131.5%, Sharpe 0.53)</p>
      </div>      <div class="lr-benefit">
        <div class="icon">📐</div>
        <h4><a href="/backtests/donchian-channel-breakout-aapl/" style="text-decoration:none;color:var(--text)">Donchian</a></h4>
        <p>7 assets tested · Best: AAPL (+0.0%, Sharpe 0.00)</p>
      </div>      <div class="lr-benefit">
        <div class="icon">📈</div>
        <h4><a href="/backtests/ema-ribbon-qqq/" style="text-decoration:none;color:var(--text)">EMA</a></h4>
        <p>5 assets tested · Best: QQQ (+81.5%, Sharpe 0.67)</p>
      </div>      <div class="lr-benefit">
        <div class="icon">☁️</div>
        <h4><a href="/backtests/ichimoku-cloud-qqq/" style="text-decoration:none;color:var(--text)">Ichimoku</a></h4>
        <p>5 assets tested · Best: QQQ (+64.6%, Sharpe 0.54)</p>
      </div>      <div class="lr-benefit">
        <div class="icon">📊</div>
        <h4><a href="/backtests/macd-crossover-tsla/" style="text-decoration:none;color:var(--text)">MACD</a></h4>
        <p>8 assets tested · Best: TSLA (+334.6%, Sharpe 0.66)</p>
      </div>      <div class="lr-benefit">
        <div class="icon">📈</div>
        <h4><a href="/backtests/rsi-oversold-overbought-aapl/" style="text-decoration:none;color:var(--text)">RSI</a></h4>
        <p>7 assets tested · Best: AAPL (+75.5%, Sharpe 0.52)</p>
      </div>      <div class="lr-benefit">
        <div class="icon">📍</div>
        <h4><a href="/backtests/parabolic-sar-aapl/" style="text-decoration:none;color:var(--text)">SAR</a></h4>
        <p>6 assets tested · Best: AAPL (+43.1%, Sharpe 0.31)</p>
      </div>      <div class="lr-benefit">
        <div class="icon">📊</div>
        <h4><a href="/backtests/golden-cross-qqq/" style="text-decoration:none;color:var(--text)">SMA</a></h4>
        <p>6 assets tested · Best: QQQ (+110.3%, Sharpe 0.80)</p>
      </div>      <div class="lr-benefit">
        <div class="icon">🎯</div>
        <h4><a href="/backtests/stochastic-crossover-btc-usd/" style="text-decoration:none;color:var(--text)">Stochastic</a></h4>
        <p>5 assets tested · Best: BTC (+22.4%, Sharpe 0.22)</p>
      </div>      <div class="lr-benefit">
        <div class="icon">🔊</div>
        <h4><a href="/backtests/volume-spike-breakout-eth-usd/" style="text-decoration:none;color:var(--text)">Volume</a></h4>
        <p>6 assets tested · Best: ETH (+50.3%, Sharpe 0.56)</p>
      </div>
</div>

<h2 id="methodology" style="margin-top:3rem;color:var(--navy-bar);margin-bottom:1rem">Methodology</h2>
<p style="font-size:1.3rem;color:var(--text-secondary);line-height:1.6">All backtests run on <strong>5 years of daily OHLCV data</strong> from Yahoo Finance using the <strong>backtrader</strong> engine. Starting capital: $10,000, 95% position sizing, 0.1% commission per trade. No curve-fitting, no cherry-picking.</p>
<p style="font-size:1.3rem;color:var(--text-secondary);line-height:1.6">Updated every Saturday. 10 indicators across 8 assets and growing.</p>

<h2 id="faq" style="margin-top:3rem;color:var(--navy-bar)">FAQ</h2>

<div class="lr-faq">
  <h3>Are these results real?</h3>
  <p>Yes. Every number comes from an actual backtest against historical price data. No curve-fitting, no cherry-picking. We test every indicator with the same parameters across all assets.</p>
</div>

<div class="lr-faq">
  <h3>Can I copy these signals?</h3>
  <p>You can — but past performance doesn't guarantee future results. These backtests are educational tools, not trading advice. Always test strategies yourself before risking capital.</p>
</div>

<div class="lr-faq">
  <h3>How often are results updated?</h3>
  <p>Every Saturday we refresh all existing backtests with the latest market data and add new indicators to the roster. The methodology stays consistent — same engine, same parameters, same starting capital.</p>
</div>

<div class="lr-faq">
  <h3>What if an indicator shows 0 trades?</h3>
  <p>Some indicators rarely fire on certain assets — they're designed for specific market conditions. A Donchian Channel might sit idle for months, then trigger during a breakout. Zero trades doesn't mean broken — it means selective.</p>
</div>
