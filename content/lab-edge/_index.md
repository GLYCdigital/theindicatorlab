---
title: "The Lab Edge"
date: 2026-05-29
draft: false
type: page
description: "The same Time-Series Momentum framework institutions use. 166 markets. Weekly signals. Now on your phone."
---

{{< rawhtml >}}
<style>
  .le-hero { text-align: center; padding: 6rem 1rem 4rem; }
  .le-hero h1 { font-size: 5.5rem; line-height: 1.1; margin: 0 0 2rem; color: var(--text); letter-spacing: -1.5px; }
  .le-hero h1 .le-line1 { display: block; font-size: 3.5rem; margin-bottom: 1.8rem; font-weight: 700; }
  .le-hero h1 span { color: var(--accent); }
  .le-hero .sub { font-size: 2rem; color: var(--text-secondary); max-width: 700px; margin: 0 auto 3rem; line-height: 1.5; font-weight: 400; }
  .le-cta { display: block; width: fit-content; margin: 0 auto; background: var(--accent); color: #fff !important; font-weight: 700; padding: 20px 56px; border-radius: var(--radius); font-size: 1.7rem; text-decoration: none !important; transition: background 0.15s, transform 0.15s; box-shadow: 0 2px 12px rgba(232, 119, 34, 0.35); }
  .le-cta:hover { background: var(--accent-hover); transform: translateY(-2px); box-shadow: 0 6px 20px rgba(232, 119, 34, 0.5); }
  .le-cta-sub { margin-top: 1.5rem; font-size: 1.3rem; color: var(--text-muted); }
  .le-stats { display: flex; justify-content: center; gap: 3rem; flex-wrap: wrap; padding: 2rem 1rem; border-top: 1px solid var(--card-border); border-bottom: 1px solid var(--card-border); max-width: 800px; margin: 0 auto; }
  .le-stat { text-align: center; }
  .le-stat .num { font-size: 2.8rem; font-weight: 800; color: var(--accent); display: block; line-height: 1; }
  .le-stat .label { font-size: 1.2rem; color: var(--text-muted); margin-top: 0.5rem; }
  .le-section { max-width: 720px; margin: 0 auto; padding: 5rem 1rem; }
  .le-section h2 { font-size: 2.4rem; font-weight: 700; margin: 0 0 1rem; color: var(--text); letter-spacing: -0.5px; }
  .le-section h3 { font-size: 1.8rem; font-weight: 600; margin: 0 0 0.5rem; }
  .le-section p { font-size: 1.5rem; color: var(--text-secondary); line-height: 1.7; margin: 0 0 1.5rem; }
  .le-table { width: 100%; border-collapse: collapse; margin: 1.5rem 0; font-size: 1.35rem; }
  .le-table th { text-align: left; padding: 10px 14px; border-bottom: 2px solid var(--card-border); color: var(--text-muted); font-weight: 600; }
  .le-table td { padding: 10px 14px; border-bottom: 1px solid var(--card-border); }
  .le-table .grn { color: #22c55e; font-weight: 600; }
  .le-transparency { background: var(--card-bg); border: 1px solid var(--card-border); border-radius: var(--radius); padding: 2rem; margin: 2rem 0; }
  .le-quote { border-left: 3px solid var(--accent); padding-left: 1.5rem; font-style: italic; color: var(--text-secondary); font-size: 1.4rem; margin: 2rem 0; }
  .le-blocks { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 1.5rem; margin: 2rem 0; }
  .le-block { background: var(--card-bg); border: 1px solid var(--card-border); border-radius: var(--radius); padding: 2rem; text-align: center; }
  .le-block .icon { font-size: 2.4rem; margin-bottom: 1rem; }
  .le-block h4 { margin: 0 0 0.5rem; font-size: 1.4rem; font-weight: 600; color: var(--text); }
  .le-block p { margin: 0; color: var(--text-secondary); font-size: 1.3rem; line-height: 1.5; }
  .le-pricing { text-align: center; background: var(--primary); border-radius: var(--radius-lg); padding: 3.5rem 2rem; margin: 2rem 0; color: #fff; }
  .le-pricing h2 { margin: 0 0 0.5rem; font-size: 2rem; color: rgba(255,255,255,0.95); }
  .le-price { font-size: 5.5rem; font-weight: 800; margin: 1.5rem 0 0.5rem; color: #fff; }
  .le-price span { font-size: 1.6rem; color: rgba(255,255,255,0.7); font-weight: 400; }
  .le-price-sub { color: rgba(255,255,255,0.7); margin: 0 0 2rem; font-size: 1.5rem; }
  .le-pricing .le-cta { background: var(--accent); }
  .le-pricing .le-cta:hover { background: var(--accent-hover); }
  .le-bundle { text-align: center; background: linear-gradient(135deg, var(--primary) 0%, #5a1f8a 100%); border-radius: var(--radius-lg); padding: 3rem 2rem; margin: 2rem 0; color: #fff; }
  .le-bundle h2 { margin: 0 0 0.5rem; font-size: 1.8rem; color: rgba(255,255,255,0.9); }
  .le-bundle .le-price { font-size: 4rem; }
  .le-faq { border-top: 1px solid var(--card-border); padding: 2rem 0; }
  .le-faq h3 { margin: 0 0 0.8rem; font-size: 1.5rem; font-weight: 600; color: var(--text); }
  .le-faq p { margin: 0; color: var(--text-secondary); font-size: 1.4rem; line-height: 1.7; }
  .le-close { text-align: center; padding: 5rem 1rem; background: var(--primary); border-radius: var(--radius-lg); max-width: 720px; margin: 0 auto; color: #fff; }
  .le-close h2 { font-size: 3rem; margin: 0 0 1rem; font-weight: 700; color: #fff; }
  .le-close p { font-size: 1.6rem; color: rgba(255,255,255,0.8); margin: 0 0 2rem; }
  @media (max-width: 768px) {
    .le-blocks { grid-template-columns: 1fr; }
    .le-hero h1 .le-line1 { font-size: 2.2rem; }
  }
</style>
{{< /rawhtml >}}

{{< rawhtml >}}
<div class="le-hero">
  <h1><span class="le-line1">A strategy that institutions keep quiet.</span>The <span>Edge</span> to hear it anyway.</h1>
  <p class="sub">Time-Series Momentum — the same framework Bridgewater, AQR, and Renaissance have used for decades — across 166 markets. One signal. Once a week. Delivered to your phone.</p>
  <p class="le-cta-sub">7-day free trial. Cancel anytime.</p>
</div>

<div class="le-stats">
  <div class="le-stat"><span class="num">166</span><span class="label">markets across 9 asset classes</span></div>
  <div class="le-stat"><span class="num">95%</span><span class="label">of markets profitable</span></div>
  <div class="le-stat"><span class="num">33K+</span><span class="label">trades validated</span></div>
</div>

<div class="le-section">
  <h2>Institutions have been running this since the 1970s. They just never gave you the dashboard.</h2>
  <p>Time-Series Momentum is the documented anomaly that never went away — Moskowitz, Ooi, and Pedersen published it in 2012. AQR runs it. Bridgewater runs it. Renaissance runs it. The difference? They run it with teams of quants and Bloomberg terminals. You now run it with a Telegram bot.</p>
  <p>Two moving averages. SMA10 crossing above SMA40. That's the entire signal. No machine learning. No black box. Just a mechanical rule that works across every asset class — stocks, bonds, commodities, crypto, forex — because human behaviour patterns are universal.</p>
  <p>SMA10 crosses above SMA40 → buy. Crosses below → sell. Position sized by volatility so you don't get wiped out during the chop. Rebalanced once a week because daily noise kills returns. The framework is documented. The engine that runs it across 166 markets, every Sunday, with zero input from you — that's what took years to build. That's what $79 gets you.</p>
</div>

<div class="le-section">
  <h2>We built this for ourselves. We're now opening access.</h2>
  <p>The Lab Edge scan engine has been running privately, watching 166 markets around the clock. Every Sunday at 22:00 SGT, it runs the numbers and surfaces what's moving. We didn't build this to sell. We built it because we wanted it. The decision to share it came after we realized how well it works.</p>

  <table class="le-table">
    <thead><tr><th>Asset Class</th><th>Markets</th><th>Profitable</th><th>Avg Return</th><th>Sharpe</th></tr></thead>
    <tbody>
      <tr><td>US Equities</td><td>50</td><td class="grn">50/50</td><td>+506%</td><td>0.71</td></tr>
      <tr><td>Equity ETFs</td><td>10</td><td class="grn">10/10</td><td>+90%</td><td>0.68</td></tr>
      <tr><td>Bonds</td><td>15</td><td class="grn">15/15</td><td>+19%</td><td>0.68</td></tr>
      <tr><td>Sector ETFs</td><td>11</td><td class="grn">11/11</td><td>+74%</td><td>0.57</td></tr>
      <tr><td>Alternatives</td><td>5</td><td class="grn">5/5</td><td>+45%</td><td>0.50</td></tr>
      <tr><td>Int'l ETFs</td><td>20</td><td class="grn">20/20</td><td>+72%</td><td>0.43</td></tr>
      <tr><td>Commodities</td><td>20</td><td class="grn">20/20</td><td>+62%</td><td>0.34</td></tr>
      <tr><td>Crypto</td><td>15</td><td class="grn">12/15</td><td>+29%</td><td>0.30</td></tr>
      <tr><td>Forex</td><td>20</td><td>14/20</td><td>+5%</td><td>0.06</td></tr>
    </tbody>
  </table>
  <p style="text-align:center;font-size:1.25rem;color:var(--text-muted);margin-top:1rem;">157 of 166 markets profitable · 33,112 trades · +185% average return · 61 years of data (1965–2026)</p>

  <div class="le-transparency">
    <p style="margin:0;font-size:1.3rem;color:var(--text-secondary);"><strong>⚡ Full transparency:</strong> Two moving averages. No optimisation. The same SMA10/40 rule applied to every market. We show you the framework because it holds up to scrutiny — verify any signal yourself. Nothing is hidden because there's nothing to hide.</p>
  </div>
</div>

<div class="le-section">
  <h2>What you get</h2>

  <div class="le-blocks">
    <div class="le-block">
      <div class="icon">📡</div>
      <h4>Weekly Signal</h4>
      <p>Every Sunday 22:00 SGT. New entries, exits, trends. One message. Clear. No noise.</p>
    </div>
    <div class="le-block">
      <div class="icon">🎯</div>
      <h4>Exact Levels</h4>
      <p>Entry price. Stop-loss. Position size. You decide. The math is done for you.</p>
    </div>
    <div class="le-block">
      <div class="icon">🌍</div>
      <h4>166 Markets</h4>
      <p>Stocks, ETFs, bonds, commodities, crypto, forex. One framework, everywhere.</p>
    </div>
    <div class="le-block">
      <div class="icon">📊</div>
      <h4>On-Demand</h4>
      <p>/report — weekly snapshot. /trending — what's moving. /markets — browse by class.</p>
    </div>
    <div class="le-block">
      <div class="icon">🔍</div>
      <h4>No Black Box</h4>
      <p>SMA10 × SMA40. ATR-sized. Every signal verifiable. Transparency is the proof.</p>
    </div>
    <div class="le-block">
      <div class="icon">📋</div>
      <h4>Weekly Rebalance</h4>
      <p>Once a week. Not once an hour. TSM works on weekly signals. We don't add noise.</p>
    </div>
  </div>
</div>

<div class="le-section">
  <h2>Why once a week?</h2>
  <p>Because the data says so. More trades ≠ more profit. The 3-month live verification across all 166 markets showed that weekly rebalancing maximises every metric that matters — Sharpe ratio, win rate, drawdown recovery. Daily signals introduce noise. Hourly signals introduce chaos. The Edge is patience.</p>
  <p>You live your life. The engine runs on Sunday evening. You open one message.</p>
</div>

<div class="le-section">
  <h2>How it works</h2>
  <p>1. Subscribe — 7-day free trial. No card tricks.</p>
  <p>2. Start <a href="https://t.me/TheLabEdge_bot" style="color:var(--accent);font-weight:600;">@TheLabEdge_bot</a> on Telegram.</p>
  <p>3. Sunday 22:00 SGT — you get the week's signal broadcast. New entries. Exits. What's still trending.</p>
  <p>4. During the week: /report for the latest snapshot. /trending for what's moving. /markets to explore 166 markets by class.</p>
  <p>5. Next Sunday: same time, updated signals. A new snapshot overwrites the old one. Simple.</p>
</div>

<div id="pricing" class="le-section">
  <div class="le-pricing">
    <h2>The Lab Edge</h2>
    <div class="le-price">$79<span>/mo</span></div>
    <p class="le-price-sub">Weekly TSM signals on 166 markets · 7-day free trial · Cancel anytime</p>
    <p style="color:rgba(255,255,255,0.7);font-size:1.35rem;">Annual: $759/yr (save 20%)</p>
    <a href="https://buy.stripe.com/cNidR19q6aG06Ts0QhaAw0b" class="le-cta">Get The Lab Edge →</a>
  </div>

  <p style="text-align:center;color:var(--text-muted);font-size:1.15rem;margin-bottom:0;">Want the full picture? Real-time consensus from 44 indicators every 15 minutes:</p>

  <div class="le-bundle">
    <h2>Bundle — Edge + Report</h2>
    <div class="le-price">$99<span>/mo</span></div>
    <p class="le-price-sub">Weekly Edge signals + 15-min Report consensus. Two products, one price.</p>
    <p style="color:rgba(255,255,255,0.6);font-size:1.3rem;">7-day free trial. Annual: $950 (20% off).</p>
    <a href="https://buy.stripe.com/dRm7sD0TA7tO2DcbuVaAw0c" class="le-cta">Get The Bundle →</a>
  </div>
</div>

<div class="le-section">
  <h2>FAQ</h2>

  <div class="le-faq">
    <h3>Why only once a week?</h3>
    <p>TSM works best on weekly signals. Daily noise generates false entries. Across 33,000+ trades, weekly rebalancing produces the highest Sharpe ratio and lowest drawdowns. More signals ≠ better results.</p>
  </div>

  <div class="le-faq">
    <h3>How do I receive the signals?</h3>
    <p>Telegram. <a href="https://t.me/TheLabEdge_bot" style="color:var(--accent);">@TheLabEdge_bot</a>. Every Sunday at 22:00 SGT. You can also ping it anytime — /report for the latest snapshot, /trending for active signals, /markets to browse all 166 markets.</p>
  </div>

  <div class="le-faq">
    <h3>Is this a black box?</h3>
    <p>No. Two moving averages: SMA10 and SMA40. When the fast line crosses above the slow line, it signals a bullish trend. Position size is scaled by ATR. We open the hood because the framework holds up to scrutiny — you can verify every signal. What you're paying for is the engine that scans 166 markets every week and surfaces what matters, so you don't have to.</p>
  </div>

  <div class="le-faq">
    <h3>What's the catch with the free trial?</h3>
    <p>No catch. Full access for 7 days. All 166 markets. All commands. Cancel before the trial ends and you're not charged. We're confident you'll stay because the strategy works — not because we made it hard to leave.</p>
  </div>

  <div class="le-faq">
    <h3>Is this financial advice?</h3>
    <p>No. The Lab Edge is an analytical tool — it applies a mechanical, transparent strategy to market data. You decide what to do with the signals. Past performance, including our backtest results, does not guarantee future returns.</p>
  </div>
</div>

<div class="le-section">
  <div class="le-close">
    <h2>You don't need to watch 166 markets. That's our job.</h2>
    <p>One message every Sunday. The signal. The stop. The size.</p>
    <p style="font-size:1.3rem;color:rgba(255,255,255,0.6);">7-day free trial. Cancel anytime.</p>
  </div>
</div>

{{< /rawhtml >}}
