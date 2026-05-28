---
title: "The Lab Edge"
date: 2026-05-28
draft: false
type: page
description: "Time-Series Momentum on 166 markets.<br>Weekly signals. Institutional framework. Your phone."
---

{{< rawhtml >}}
<style>
  .le-hero { text-align: center; padding: 5rem 1rem 3rem; }
  .le-hero h1 { font-size: 5rem; line-height: 1.1; margin: 0 0 1.5rem; color: var(--text); letter-spacing: -1px; }
  .le-hero h1 span { color: var(--accent); }
  .le-hero p { font-size: 1.8rem; color: var(--text-secondary); max-width: 680px; margin: 0 auto 2.5rem; line-height: 1.6; }
  .le-cta { display: block; width: fit-content; margin: 0 auto; background: var(--accent); color: #fff !important; font-weight: 700; padding: 18px 52px; border-radius: var(--radius); font-size: 1.6rem; text-decoration: none !important; transition: background 0.15s, transform 0.15s; box-shadow: 0 2px 8px rgba(232, 119, 34, 0.3); }
  .le-cta:hover { background: var(--accent-hover); transform: translateY(-1px); box-shadow: 0 4px 16px rgba(232, 119, 34, 0.4); }
  .le-cta-sub { margin-top: 1.5rem; font-size: 1.25rem; color: var(--text-muted); }
  .le-trust { display: flex; justify-content: center; gap: 2.5rem; flex-wrap: wrap; padding: 1.5rem 1rem; border-top: 1px solid var(--card-border); border-bottom: 1px solid var(--card-border); max-width: 720px; margin: 0 auto 3rem; color: var(--text-muted); font-size: 1.3rem; }
  .le-trust strong { color: var(--text); }
  .le-section { max-width: 720px; margin: 0 auto; padding: 4rem 1rem; }
  .le-section h2 { font-size: 2.2rem; font-weight: 700; margin: 0 0 1rem; color: var(--text); }
  .le-section h3 { font-size: 1.7rem; font-weight: 600; margin: 0 0 0.5rem; }
  .le-table { width: 100%; border-collapse: collapse; margin: 1.5rem 0; font-size: 1.3rem; }
  .le-table th { text-align: left; padding: 8px 12px; border-bottom: 2px solid var(--card-border); color: var(--text-muted); font-weight: 600; }
  .le-table td { padding: 8px 12px; border-bottom: 1px solid var(--card-border); }
  .le-table .green { color: #22c55e; font-weight: 600; }
  .le-step { display: flex; gap: 1.5rem; margin: 2rem 0; align-items: center; }
  .le-step-num { background: var(--primary); color: #fff; width: 44px; height: 44px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 1.3rem; flex-shrink: 0; }
  .le-step h3 { margin: 0 0 0.3rem; font-size: 1.6rem; font-weight: 600; }
  .le-step p { margin: 0; color: var(--text-secondary); font-size: 1.4rem; line-height: 1.6; }
  .le-benefits { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin: 2rem 0; }
  .le-benefit { background: var(--card-bg); border: 1px solid var(--card-border); border-radius: var(--radius); padding: 1.5rem; }
  .le-benefit .icon { font-size: 1.8rem; margin-bottom: 0.5rem; }
  .le-benefit h4 { margin: 0 0 0.3rem; font-size: 1.4rem; font-weight: 600; color: var(--text); }
  .le-benefit p { margin: 0; color: var(--text-secondary); font-size: 1.3rem; line-height: 1.5; }
  .le-pricing { text-align: center; background: var(--primary); border-radius: var(--radius-lg); padding: 2.5rem 2rem 3rem; margin: 2rem 0; color: #fff; }
  .le-pricing h2 { margin: 0 0 0.5rem; font-size: 2rem; color: rgba(255,255,255,0.9); }
  .le-pricing > p { font-size: 1.5rem; color: rgba(255,255,255,0.7); }
  .le-price { font-size: 5rem; font-weight: 800; margin: 1rem 0; color: #fff; }
  .le-price span { font-size: 1.6rem; color: rgba(255,255,255,0.7); font-weight: 400; }
  .le-price-sub { color: rgba(255,255,255,0.7); margin: 0 0 2rem; font-size: 1.5rem; }
  .le-pricing .le-cta { background: var(--accent); }
  .le-pricing .le-cta:hover { background: var(--accent-hover); }
  .le-compare { display: grid; grid-template-columns: 1fr 1px 1fr; gap: 1.5rem; margin: 2rem 0; align-items: start; }
  .le-compare-col { padding: 1.5rem; }
  .le-compare-divider { background: var(--card-border); }
  .le-compare h3 { font-size: 1.5rem; margin: 0 0 0.5rem; }
  .le-compare .price { font-size: 2.4rem; font-weight: 800; color: var(--accent); }
  .le-compare ul { list-style: none; padding: 0; margin: 1rem 0; }
  .le-compare li { padding: 4px 0; font-size: 1.25rem; color: var(--text-secondary); }
  .le-faq { border-top: 1px solid var(--card-border); padding: 1.5rem 0; }
  .le-faq h3 { margin: 0 0 0.5rem; font-size: 1.5rem; font-weight: 600; color: var(--text); }
  .le-faq p { margin: 0; color: var(--text-secondary); font-size: 1.4rem; line-height: 1.6; }
  .le-close { text-align: center; padding: 5rem 1rem; background: var(--primary); border-radius: var(--radius-lg); max-width: 720px; margin: 0 auto; color: #fff; }
  .le-close h2 { font-size: 2.8rem; margin: 0 0 1rem; font-weight: 700; color: #fff; }
  .le-close p { font-size: 1.5rem; color: rgba(255,255,255,0.8); margin: 0 0 2rem; }
  @media (max-width: 768px) {
    .le-benefits { grid-template-columns: 1fr; }
    .le-compare { grid-template-columns: 1fr; }
    .le-compare-divider { display: none; }
    .le-hero h1 { font-size: 3.2rem; }
  }
</style>
{{< /rawhtml >}}

{{< rawhtml >}}
<div class="le-hero">
  <h1>The Lab<span>.</span>Edge</h1>
  <p>Time-Series Momentum on <strong>166 markets</strong>. One signal every Sunday. Same framework institutional funds have used for 50+ years — packaged for your phone.</p>
  <p class="le-cta-sub" style="font-size:1.4rem;color:var(--text-secondary);">7-day free trial. Cancel anytime. Annual plans available.</p>
</div>

<div class="le-trust">
  <span><strong>166</strong> markets</span>
  <span><strong>9</strong> asset classes</span>
  <span><strong>95%</strong> profitable</span>
  <span><strong>33K+</strong> trades analyzed</span>
</div>

<div class="le-section">
  <h2>The Lab Report tells you what's happening.<br>The Lab Edge tells you what to do about it.</h2>

  <div class="le-compare" style="margin-top:2rem;">
    <div class="le-compare-col">
      <div class="icon" style="font-size:2rem;">📊</div>
      <h3>The Lab Report</h3>
      <div class="price">$29/mo</div>
      <ul>
        <li>44 indicators tracked</li>
        <li>20 markets covered</li>
        <li>Updates every 15 minutes</li>
        <li>Consensus signals</li>
        <li>"What's happening?"</li>
      </ul>
      <a href="/the-lab-report/" style="color:var(--accent);font-weight:600;">View →</a>
    </div>
    <div class="le-compare-divider"></div>
    <div class="le-compare-col">
      <div class="icon" style="font-size:2rem;">🎯</div>
      <h3>The Lab Edge</h3>
      <div class="price">$79/mo</div>
      <ul>
        <li>Time-Series Momentum</li>
        <li>166 markets covered</li>
        <li>Weekly signals (Sunday)</li>
        <li>Entry, stop, position size</li>
        <li>"What to do about it."</li>
      </ul>
      <a href="#pricing" style="color:var(--accent);font-weight:600;">Scroll ↓</a>
    </div>
  </div>
</div>

<div class="le-section">
  <h2>The Strategy</h2>
  
  <div class="le-step">
    <div class="le-step-num">1</div>
    <div><h3>Time-Series Momentum (SMA10/40)</h3><p>The simplest trend-following rule in finance: buy when the 10-day moving average crosses above the 40-day. Sell when it crosses below. No complex indicators. No curve-fitting. Just time-tested momentum.</p></div>
  </div>
  <div class="le-step">
    <div class="le-step-num">2</div>
    <div><h3>Position Sized by ATR</h3><p>Every trade size is risk-adjusted based on 2× Average True Range. Your position automatically scales down in volatile markets and up when things are calm.</p></div>
  </div>
  <div class="le-step">
    <div class="le-step-num">3</div>
    <div><h3>Weekly Rebalance</h3><p>Every Sunday at 22:00 SGT, the engine scans all 166 markets. You get a Telegram message with: new entries, exits, and a summary of what's trending. One message. Once a week. No noise.</p></div>
  </div>
</div>

<div class="le-section">
  <h2>Backtest Results</h2>
  <p style="font-size:1.4rem;color:var(--text-secondary);margin-bottom:1.5rem;">166 markets tested. 61 years of data on the longest-running index (Nikkei, 1965–2026). No cherry-picking. No curve-fitting.</p>

  <table class="le-table">
    <thead><tr><th>Asset Class</th><th>Markets</th><th>Profitable</th><th>Avg Return</th><th>Sharpe</th></tr></thead>
    <tbody>
      <tr><td>US Equities</td><td>50</td><td class="green">50/50</td><td>+506%</td><td>0.71</td></tr>
      <tr><td>Equity ETFs</td><td>10</td><td class="green">10/10</td><td>+90%</td><td>0.68</td></tr>
      <tr><td>Bonds</td><td>15</td><td class="green">15/15</td><td>+19%</td><td>0.68</td></tr>
      <tr><td>Sector ETFs</td><td>11</td><td class="green">11/11</td><td>+74%</td><td>0.57</td></tr>
      <tr><td>Alternatives</td><td>5</td><td class="green">5/5</td><td>+45%</td><td>0.50</td></tr>
      <tr><td>Int'l ETFs</td><td>20</td><td class="green">20/20</td><td>+72%</td><td>0.43</td></tr>
      <tr><td>Commodities</td><td>20</td><td class="green">20/20</td><td>+62%</td><td>0.34</td></tr>
      <tr><td>Crypto</td><td>15</td><td class="green">12/15</td><td>+29%</td><td>0.30</td></tr>
      <tr><td>Forex</td><td>20</td><td>14/20</td><td>+5%</td><td>0.06</td></tr>
    </tbody>
  </table>
  <p style="text-align:center;font-size:1.2rem;color:var(--text-muted);margin-top:1rem;">157 of 166 markets profitable · 33,112 trades · +185% average return · Data: yFinance + backtrader</p>
</div>

<div class="le-section">
  <h2>What You Get</h2>
  
  <div class="le-benefits">
    <div class="le-benefit">
      <div class="icon">📡</div>
      <h4>Weekly Signal Broadcast</h4>
      <p>Every Sunday at 22:00 SGT — new entries, exits, and trend status. One message. Clear action.</p>
    </div>
    <div class="le-benefit">
      <div class="icon">🎯</div>
      <h4>Exact Levels</h4>
      <p>Entry price. Stop loss (2× ATR). Position size. No guessing. No interpretation required.</p>
    </div>
    <div class="le-benefit">
      <div class="icon">🌍</div>
      <h4>166 Markets</h4>
      <p>Stocks, ETFs, bonds, commodities, crypto, forex — the same framework works across all asset classes.</p>
    </div>
    <div class="le-benefit">
      <div class="icon">📊</div>
      <h4>On-Demand Commands</h4>
      <p>Reply /trending for active signals, /markets to browse by class, /signals for pending entries.</p>
    </div>
    <div class="le-benefit">
      <div class="icon">🔍</div>
      <h4>Full Transparency</h4>
      <p>Two moving averages. That's it. No black box. You can replicate the signal on any chart in 30 seconds.</p>
    </div>
    <div class="le-benefit">
      <div class="icon">🤖</div>
      <h4>Paper-Trade Verified</h4>
      <p>Grid execution bot paper-trades every signal. 3-month live track record before commercial launch.</p>
    </div>
  </div>
</div>

<div id="pricing" class="le-section">
  <div class="le-pricing">
    <h2>Lab Edge</h2>
    <div class="le-price">$79<span>/mo</span></div>
    <p class="le-price-sub">Weekly TSM signals on 166 markets · Cancel anytime</p>
    <p style="color:rgba(255,255,255,0.7);font-size:1.3rem;">7-day free trial. Cancel anytime. Annual: $759 (20% off).</p>
    <a href="https://buy.stripe.com/cNidR19q6aG06Ts0QhaAw0b" class="le-cta">Get The Lab Edge →</a>
  </div>

  <div class="le-pricing" style="background: linear-gradient(135deg, var(--primary) 0%, var(--accent) 100%);">
    <h2>Bundle — Lab Report + Lab Edge</h2>
    <div class="le-price">$99<span>/mo</span></div>
    <p class="le-price-sub">The Lab Report ($29) + Lab Edge ($79) together. Save $9/mo.</p>
    <p style="color:rgba(255,255,255,0.7);font-size:1.3rem;">7-day free trial. Annual: $950 (20% off).</p>
    <a href="https://buy.stripe.com/dRm7sD0TA7tO2DcbuVaAw0c" class="le-cta">Get The Bundle →</a>
  </div>

  <p style="text-align:center;font-size:1.15rem;color:var(--text-muted);margin-top:1rem;"></p>
</div>

<div class="le-section">
  <h2>FAQ</h2>

  <div class="le-faq">
    <h3>How is this different from The Lab Report?</h3>
    <p>The Lab Report aggregates 44 indicators into a consensus score — it answers "what's the market doing?" The Lab Edge uses one proven strategy (TSM) to answer "what should I do about it?" Report is real-time. Edge is weekly.</p>
  </div>

  <div class="le-faq">
    <h3>Why only once a week?</h3>
    <p>TSM works best on weekly signals. Daily noise generates false entries. A 3-month paper-trading period proved this across 166 markets: more trades ≠ more profit. Weekly rebalancing maximises Sharpe.</p>
  </div>

  <div class="le-faq">
    <h3>How do I receive the signals?</h3>
    <p>Via Telegram. Every Sunday at 22:00 SGT, @TheLabEdge_bot sends you the weekly broadcast. You can also ping it anytime with /trending, /signals, /markets, or /status.</p>
  </div>

  <div class="le-faq">
    <h3>Is this financial advice?</h3>
    <p>No. The Lab Edge is an analytical tool — it applies a mechanical strategy to historical data and current prices. You decide whether to act. All results are based on backtesting; past performance does not guarantee future results.</p>
  </div>
</div>

<div class="le-section">
  <div class="le-close">
    <h2>The Edge is patience.</h2>
    <p>One signal per week. 166 markets. No noise.</p>
    <p style="font-size:1.3rem;color:rgba(255,255,255,0.6);">7-day free trial. Cancel anytime.</p>
  </div>
</div>

{{< /rawhtml >}}
