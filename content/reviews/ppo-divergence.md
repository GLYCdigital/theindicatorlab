---
title: "Ppo_Divergence Review: Settings, Strategy & How to Use It"
date: 2026-09-09
draft: false
type: reviews
image: "/screenshots/ppo-divergence.png"
tags:
  - "ppo divergence"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Ppo_Divergence review: 4-star TradingView tool that flags hidden and regular PPO divergences. Tested settings, entry logic, and honest pros & cons."
---
Let me cut through the noise. Ppo_Divergence is exactly what the name says — it scans the Percentage Price Oscillator for divergences and plots them directly on your chart. No machine learning, no predictive AI, no repainting nonsense. Just a clean utility that does one job and does it well.

I've spent the last two weeks running this on BTCUSD, EURUSD, and a handful of large-cap stocks across multiple timeframes. As you can see in the chart above, the indicator marks divergences with distinct arrows — regular bearish in one color, bullish in another, and it handles hidden divergences separately. That separation matters more than most traders realize.

**What actually sets it apart**

Most divergence indicators on TradingView are repackaged RSI or MACD scripts with a divergence scanner bolted on. Ppo_Divergence uses the PPO instead of MACD, which gives you a normalized oscillator. That's a meaningful difference — PPO readings are comparable across different assets because they're percentage-based, not absolute-value based. A MACD reading of 50 means something entirely different on a $30 stock versus a $500 stock. PPO doesn't have that problem.

The indicator also gives you control over divergence sensitivity. You can adjust the PPO length, the signal smoothing, and how strict the divergence detection algorithm is. I found the default settings work fine for swing trading, but if you're scalping, you'll want to tighten things up.

**Settings I actually tested**

Here's what I landed on after testing:

- **PPO Length:** 12 (default works, but 9 makes it more responsive on lower timeframes)
- **Signal Smoothing:** 9 (keep this — the signal line is your confirmation)
- **Divergence Lookback:** Set this to 2-3 bars for swing trading. Anything higher generates too many false positives on choppy days.

For intraday, drop the PPO length to 8 and increase the divergence sensitivity one notch. You'll get more signals, but you have to be willing to filter them yourself.

**How I trade it**

The setup is straightforward. When a bullish regular divergence prints — price makes a lower low while PPO makes a higher low — I wait for the PPO to cross above its signal line before entering long. The divergence is the warning shot; the cross is the trigger. For shorts, flip it.

Hidden divergences are where this indicator earns its keep for trend traders. In a strong uptrend, a hidden bullish divergence (higher low on price, lower low on PPO) tells you the pullback is losing steam. That's a continuation signal, not a reversal. I use those to add to existing positions rather than open new ones.

Stop loss goes below the divergence swing low, take profit at the previous swing high or a 1.5R minimum. Nothing fancy — the indicator gives you the setup, not the whole system.

**The honest trade-offs**

Pros:
- Clean visual output. Divergences are plotted with clear arrows, no clutter
- PPO normalization makes it useful across different asset classes without constant re-tuning
- Hidden and regular divergence separation is genuinely useful
- Doesn't repaint — I verified this by refreshing charts multiple times mid-session

Cons:
- No alert functionality built in. You have to set price alerts manually, which defeats some of the purpose
- The divergence detection algorithm can be fooled by extended sideways movement
- No multi-timeframe analysis. You're stuck with whatever timeframe you're viewing
- Documentation inside the script is sparse — took me a while to figure out what each input actually controlled

**Who should install this**

This is for traders who already know how to trade divergences and just want a reliable scanner that works. If you're new to divergence trading, this indicator won't teach you the concept — you'll need to understand what regular versus hidden divergence means before this becomes useful.

It's also better suited for swing trading and position trading than scalping. On the 1-minute chart, the PPO throws off too many noise signals. I tested it on the 15-minute and above with much better results.

**Alternatives worth considering**

If you want the same concept built on MACD instead of PPO, look for MACD divergence indicators — they're more common and often have more features. If you want multi-timeframe divergence analysis, you'll need to look at paid tools. And if you're a crypto trader who lives on RSI divergences, you're better off with a dedicated RSI divergence script.

**What traders usually ask**

*Does this indicator repaint?*
No. I checked this specifically. Once a divergence arrow prints, it stays.

*Can I use it on any asset?*
Yes, and that's the PPO advantage. It works on crypto, forex, stocks, and futures without adjusting for price scale.

*Does it work on lower timeframes?*
Technically yes, but expect more false signals below the 15-minute chart.

**Final verdict**

Ppo_Divergence gets four stars because it does what it claims without unnecessary complexity. The lack of alerts is frustrating, and the learning curve for the settings is steeper than it should be. But for a free divergence scanner that handles both regular and hidden divergences with clean visuals, it's one of the better options on TradingView. If you already trade divergences as part of your strategy, this is a worthwhile addition to your toolkit.

⭐⭐⭐⭐ (4/5) — Solid, reliable, and worth installing. Just don't expect it to think for you.

## Frequently Asked Questions

### Is Ppo_Divergence worth it?

Based on testing across multiple timeframes, Ppo_Divergence delivers solid value for traders who need trend analysis.

### Does this indicator repaint?

No — all signals are calculated on closed bars. Past signals will not change when new data arrives.
## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 93 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $49/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $79/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*
