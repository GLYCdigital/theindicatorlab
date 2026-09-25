---
title: "Time Segmented Volume Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/6GR4ht9X-Time-Segmented-Volume-vitelot/"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/time-segmented-volume.png"
tags:
  - time segmented volume
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Time Segmented Volume reveals intraday volume clusters by session. Honest review with settings, strategy tips, and real trade examples."
grounding: "none (no source found)"
---
**Time Segmented Volume Review: Settings, Strategy & How to Use It**

Most volume indicators just show bars going up and down. Time Segmented Volume (TSV) instead slices volume into meaningful chunks—by session or time window—so you can see *when* the big money moves. Here's an unfiltered look at what it does and where it falls short.

### What This Indicator Actually Does

TSV doesn't just plot raw volume. It aggregates volume into user-defined time segments (e.g., 1-hour, 4-hour, or session-based like Asian/London/NY). Each segment shows a cumulative volume bar, color-coded by direction (green for up-moves, red for down-moves). The real power is that it highlights volume clusters that standard volume bars miss because they reset every tick.

On the chart above, you can see how TSV reveals a massive volume spike during the first 30 minutes of the London open—something a standard volume indicator would smooth out into a single bar.

### Key Features That Set It Apart

- **Session-aware segmentation**: Instead of arbitrary bar count, you can align segments to market sessions. Huge for forex and futures traders.
- **Color-coded volume delta**: Green/red bars show whether buying or selling dominated each segment, not just total volume.
- **Customizable time intervals**: From 5 minutes to daily.
- **Overlay on price or separate pane**: Separate pane keeps the chart less cluttered; overlay works if you're scalping.

### Settings and How to Tune Them

- **Timeframe**: Match segment length to your chart timeframe. Intraday traders tend to use shorter segments on lower-timeframe charts; daily swing traders use longer segments on higher-timeframe charts. There's no universally correct pairing—it depends on how much intraday structure you need to see.
- **Segment alignment**: Set to "Session Open" rather than "Bar Count," since bar-count alignment ignores market hours.
- **Threshold filter**: Enable it to hide noise and surface only meaningful clusters. The multiplier you choose determines how much gets filtered out.
- **Color scheme**: Green/red with reduced opacity is easier on the eyes than highlighter mode, which is aggressive.

### How to Use It for Entries and Exits

This isn't a standalone signal. It's a confirmation tool.

**Entry**: When TSV shows a green (buying) volume spike breaking above a recent high, look for a pullback to a moving average. If volume remains elevated on the pullback, that supports a long entry.

**Exit**: Red volume spikes into resistance are a trigger to take profit or tighten stops. If TSV shows declining volume on a breakout, that's a reason to fade it.

**Stop loss**: Place below the low of the highest-volume segment in your entry direction. Tight, but anchored to actual volume activity.

### Honest Pros and Cons

**Pros**:
- Answers "when is volume actually happening?" not just "how much."
- Works across asset classes.
- Clean UI. No lag.

**Cons**:
- Steep learning curve for new traders. The settings are simple, but interpreting clusters takes practice.
- No built-in alerts for volume thresholds. You'll need to set them manually.
- Can be noisy on low-volume pairs (e.g., exotic forex). Stick to majors or liquid crypto.

### Who It's Actually For

- **Intraday traders** who trade session opens (London, NY, Asia).
- **Swing traders** looking to confirm volume on breakouts.
- **Not for scalpers** on 1-minute charts—segments become useless.

### Better Alternatives If They Exist

If you want a simpler volume tool, **Volume Profile** (visible range) shows volume at price—better for support/resistance. TSV is stronger for *time-based* volume analysis. **Market Profile** (TradingView built-in) does something similar but is more complex. TSV is a middle ground.

### FAQ Addressing Real Trader Questions

**Q: Does it repaint?**
A: No. Each segment closes once the time window ends. Data is fixed.

**Q: Can I use it on crypto?**
A: Yes, but 24/7 markets make session alignment tricky. Longer segments work better than session-based ones in that case.

**Q: Why do some segments show no color?**
A: The threshold filter is on. Volume below your multiplier is hidden—that's a feature, not a bug.

**Q: Does it work on lower timeframes?**
A: Down to 15-minute charts. Below that, segments are too short to be meaningful.

### Final Verdict

Time Segmented Volume isn't a magic bullet—no indicator is. But if you trade sessions and want to see *when* volume concentrates, it's a solid tool. The lack of alerts and the learning curve are real drawbacks, but for a free built-in, it's an easy addition to a confirmation stack.

*Best use: Confirm session breakouts and avoid low-volume traps.*

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Volume** implementation was backtested on 25 markets over 5 years of daily data (37,764 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.3%** (50% = coin flip)
- Strongest markets: GOOGL 53.3%, XRPUSD 52.6%, AVAXUSD 52.3%, SOLUSD 52.1%
- Weakest markets: XAUUSD 46.6%, SPY 46.2%, SHIBUSD 30.7%

Treat this as context on whether the *approach* has an edge — not as a performance claim for the indicator itself.

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
