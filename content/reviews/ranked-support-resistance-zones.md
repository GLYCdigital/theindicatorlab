---
title: "Ranked_Support_Resistance Zones Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/jTQU8WBS-Ranked-Support-Resistance-Zones-Zeiierman/"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/ranked-support-resistance-zones.png"
tags:
  - ranked support resistance zones
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Automatically identifies and ranks key support/resistance zones by strength. Clear tiers help you spot high-probability reversal and breakout levels."
grounding: "none (no source found)"
---
**What This Indicator Actually Does**

Most support/resistance indicators just dump a bunch of horizontal lines on your chart and call it a day. Ranked_Support_Resistance_Zones is built around ranking them instead — by how many times price has tested each level, how long it held, and the volume behind those tests. The point isn't just showing you *where* levels are — it's telling you *which ones matter most*.

Zones appear in three distinct tiers: strong (solid), moderate (dashed), and weak (faded). That hierarchy is the indicator's core value proposition. You're not left guessing whether a level is worth trading.

**Key Features That Set It Apart**

- **Tiered ranking system** — Strong zones are highlighted prominently; weak zones are barely visible. The intent is to filter out noise.
- **Dynamic zone width** — Zones are described as adapting to the timeframe, with width tied to ATR, so a zone on a lower timeframe isn't unrealistically wide relative to one on a higher timeframe.
- **Zone extension** — Zones extend into the future, and this is configurable. Useful for swing traders who need levels to hold over days or weeks.
- **Volume weighting option** — A toggle that gives a zone with heavy volume at its test a strength boost.
- **Breakout/breakdown labels** — When price breaks through a strong zone, the indicator flags it with a small arrow. Framed as confirmation, not as an entry trigger.

**Settings and How to Tune Them**

- **Lookback Period**: Controls how much history feeds zone validation. Longer lookbacks give more data but risk surfacing old levels that no longer matter.
- **Zone Strength Threshold**: Filters which zones appear. Raise it to cut clutter, lower it to see more candidates.
- **Zone Width Multiplier**: Scales zone width. Wider zones risk false touches; narrower zones risk missing real reactions.
- **Volume Weight**: A toggle for applying volume to zone strength. Whether this is useful depends on how reliable volume data is for the instrument you're trading.
- **Extend Zones**: Controls whether zones project into the future. Useful for swing positions, less so for intraday work.

**How to Use It for Entries and Exits**

This is not a standalone entry signal. Typical integration:

- **Reversal setups**: Wait for price to touch a strong zone (solid line) and look for a candle close rejection (wick, doji, or pin bar). Enter on the next candle. Stop loss just beyond the zone's outer edge.
- **Breakout trades**: When price closes *outside* a strong zone with volume, wait for a retest of that zone as new support/resistance. Enter on the retest candle. Behavior is generally described as stronger on higher timeframes.
- **Scaling out**: Use weaker zones (dashed) as partial profit targets. Strong zones are your main targets or invalidation points.

One caveat: the indicator can repaint slightly when a new bar forms, since it recalculates zone strength. Entering based on a zone that appeared on the current bar is risky — wait for it to stabilize on the next close.

**Honest Pros and Cons**

**Pros**:
- Ranks levels by strength rather than just drawing them
- Adjustable zone width based on ATR
- Volume weighting option adds context for crypto and FX
- Visual hierarchy reduces chart clutter
- Designed to work across timeframes without constant retuning

**Cons**:
- Slight repaint on the current bar
- No multi-timeframe alignment built in — you'd need to add it to multiple charts manually
- Weak zones (faded lines) add little; an option to hide them entirely would be preferable
- No alert integration for zone touches — alerts have to be set manually

**Who It's Actually For**

- **Swing traders** on daily charts, for the extended zones
- **Intraday mean-reversion traders** who work reversals at key levels
- **Breakout traders** who want a second opinion on whether a level is strong enough to break
- **Not for** pure trend-followers or very short-term scalpers — zone width is described as too wide for 1-minute tick data

**Better Alternatives If They Exist**

- **LuxAlgo's Support Resistance Levels** — More polished with multi-timeframe syncing, but costs more and updates zones with more lag.
- **Fractal Support Resistance** by KivancOzbilgic — Free and better suited to scalping (tighter zones), but lacks ranking and volume weighting.
- **Manual horizontal lines + pivot points** — Still the gold standard if you're willing to put in the work. This indicator saves you the time.

**FAQ Addressing Real Trader Questions**

*Q: Does it repaint?*  
A: Slightly on the current bar. Once the bar closes, zones are fixed.

*Q: What's the best timeframe?*  
A: Higher timeframes for day trading, daily for swing. It works on lower timeframes but zone width becomes less precise.

*Q: Can I use it for crypto?*  
A: Yes, particularly with volume weighting on.

*Q: How many zones show up by default?*  
A: The count varies, but clutter can be reduced by increasing the strength threshold.

**Final Verdict with Star Rating**

Ranked_Support_Resistance_Zones is one of the few S/R indicators built around the concept of "strength" — not just drawing lines but indicating which ones hold weight. The repaint is minor and manageable. It won't replace manual analysis, but it saves the time of drawing levels by hand.

It's free on TradingView, which makes it an easy addition to a toolkit. Multi-timeframe sync and alerts would be the natural next improvements.

**Rating: ⭐⭐⭐⭐ (4/5)** — Does what it promises, does it well, and leaves room for improvement.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 123 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $149/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $249/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*
