---
title: "Three_Session_Volume_Profile Review: Settings, Strategy & How to Use It"
date: 2026-09-17
draft: false
type: reviews
image: "/screenshots/three-session-volume-profile.png"
tags:
  - "three session volume profile"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Three_Session_Volume_Profile review: an honest look at this volume profile tool, its best settings, how to trade it, and where it falls short."
tv_script_url: "https://www.tradingview.com/script/CDfsfyDO-Three-Session-Volume-Profile/"
---
Most "volume profile" scripts on TradingView do the same thing: they draw a histogram on the side of your chart and call it a day. Three_Session_Volume_Profile takes a different angle. Instead of one profile, it builds three — typically covering distinct trading sessions (Asia, London, New York, or whatever split you configure) — and plots them side by side so you can compare where volume actually piled up across the day.

I ran it on MACD-style trend setups and intraday charts for a couple of weeks. Here's what it does, where it earns its keep, and where it stumbles.

## What this indicator actually does

Strip away the naming and you get a session-segmented volume profile. The script divides the trading day into three windows, calculates a volume-at-price distribution for each, and renders them as horizontal bars anchored to the right edge of the chart. Each session gets its own color, and the Point of Control (POC) — the price level with the most traded volume — is marked for each session.

That's the core mechanic. The value isn't in any single profile; it's in the **comparison**. If Asia's POC sits 40 points below London's POC, you're looking at a session that built value at a different level. When the New York session opens and price rejects the London POC, that's a signal you can actually trade.

## Key features worth noting

- **Three independent profiles** with separate color controls. You can mute sessions you don't care about instead of disabling the whole indicator.
- **Per-session POC lines** that extend across the chart, so you can see how price reacts to prior session value areas.
- **Value Area percentage** is configurable — default is 70%, which matches the standard TPO convention, but you can tighten it to 60% for a narrower "high-conviction" zone.
- **Session time inputs** are adjustable, which matters if you trade non-US hours or want a custom split.

The settings panel is more crowded than it needs to be. There are roughly 30 inputs, and several are cosmetic (bar width, transparency, label offsets). If you're the type who wants to open an indicator and go, budget 10 minutes for setup.

## Best settings I landed on

After a lot of fiddling:

- **Value Area: 70%.** The 60% setting looked cleaner but cut out too much of the distribution on thin-volume days.
- **Rows per profile: 24–30.** Below 20, the profile gets chunky and imprecise. Above 40, it's visual noise.
- **POC line width: 2, style: dashed.** Solid POC lines clutter the chart when you've got three of them.
- **Turn off the Asia session** if you're trading the New York open. It rarely adds actionable context unless you're trading the London/Asia overlap.

One quirk: the profile only recalculates on bar close if you're on a lower timeframe. On a 1-minute chart with real-time data, the bars flicker mid-formation. Not a dealbreaker, but it's distracting.

## How I traded it

The logic that worked for me was **POC rejection and cross-session acceptance**:

1. Mark the prior session's POC and value area high/low.
2. If price opens the new session *inside* the prior value area and rejects the POC, fade toward the value area edge.
3. If price *accepts* above the prior value area high (two consecutive closes), treat it as a trend continuation signal — the market has repriced.

As shown in the chart above, the three profiles stack neatly and the POC lines give you clear horizontal reference levels. On trending days, the New York POC often drifted above the London POC, and that drift was a decent trend filter.

This isn't a standalone system. It's a context tool. Pair it with a trend indicator or a momentum read — the volume profile tells you *where* to act, not *when*.

## Pros and cons

**Pros:**
- Genuinely useful cross-session comparison — most volume profile scripts don't do this.
- Configurable sessions and value area, so it adapts to different markets.
- POC lines are clean and don't repaint once the session closes.

**Cons:**
- Heavy settings panel with too much cosmetic filler.
- Can lag or flicker on low timeframes with live data.
- No built-in alerts for POC breaks — you have to set those manually.
- Documentation is thin; you're figuring out session splits by trial and error.

## Who it's for

This is for **intraday traders** — futures, forex, or crypto — who already understand volume profile and want a session-comparison view without paying for a third-party platform. If you're a swing trader holding for days, the session granularity is overkill. If you're brand new to volume profile, start with a simpler single-profile script first.

## Alternatives

If you just want a standard volume profile, **Volume Profile [LuxAlgo]** is cleaner and better documented. If you want session-based levels without the profile bars, **Session Volume Profile** by TradingView's built-in tools covers the basics. Three_Session_Volume_Profile wins specifically when you need *three simultaneous* profiles — that's its niche.

## FAQ

**Does it repaint?**
No. Once a session closes, the POC and value area are locked. Intra-session, the profile updates with each bar, which is expected behavior.

**Can I use it on crypto?**
Yes, but you need to manually set session times. The default sessions assume US equity hours.

**Does it work on the 1-minute chart?**
It works, but expect visual flicker during live bars. Set your rows lower (around 20) to reduce the noise.

**Are alerts included?**
No built-in alerts. You'd need to reference the plotted POC levels in a separate alert condition.

## Final verdict

Three_Session_Volume_Profile does one thing well: it lets you compare value across three sessions at a glance. That's a real edge for intraday traders, and the POC lines are actionable. It loses a star for the cluttered settings, missing alerts, and thin documentation — but if cross-session volume comparison is what you're missing, this fills the gap.

**Rating: ⭐⭐⭐⭐ (4/5)**
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
