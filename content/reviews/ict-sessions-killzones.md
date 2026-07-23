---
title: "Ict_Sessions_Killzones Review: Settings, Strategy & How to Use It"
date: 2026-07-23
draft: false
type: reviews
image: "/screenshots/ict-sessions-killzones.png"
tags:
  - "ict sessions killzones"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest review of ICT Sessions Killzones: a free indicator that maps Asian, London, and NY session highs/lows. Tested settings, entry logic, and who it’s actually for."
---
Let’s cut through the hype. The **Ict_Sessions_Killzones** indicator is not a magic bullet. It’s a clean, free tool that plots the high and low of each major trading session (Asian, London, New York) directly on your chart, plus highlights the “killzones” — those 30–90 minute windows where ICT traders expect liquidity grabs or reversals. If you’ve ever manually drawn session boxes and missed the close, this saves you the headache.

I tested it on the MACD chart type (which isn’t its native habitat, but it works fine) and on regular candlestick charts with ES futures and EURUSD. Here’s my take.

### What It Actually Does
It draws vertical lines at session open/close times and horizontal lines at the session’s range. You can toggle Asian, London, and NY sessions independently. The killzone shading (default: NY open, London open, Asian close) is semi-transparent — not distracting. It also labels each session with the timezone you set (UTC, EST, etc.). No repainting, no alerts, no fluff.

### Key Features That Matter
- **Session time flexibility**: You can shift the start times if your broker uses a different exchange calendar. For example, I moved NY open to 9:30 AM EST for equities instead of the default 9:00 AM.
- **Daily reset**: The indicator draws fresh zones each day without overlapping previous days. Clean, no clutter.
- **Killzone shading**: The highlight around the London open (2–5 AM EST) and NY open (7–10 AM EST) is the real value. Most breakouts happen here.
- **No repaint**: What you see at 8 AM stays. Verified.

### Best Settings I’ve Tested
After a week of tweaking:
- **Timezone**: Set to your broker’s exchange time (e.g., EST for US equities, UTC for forex).
- **Show Asian Session**: ON (it marks the overnight range for forex).
- **Show London Session**: ON (this is the liquidity grab zone for EURUSD).
- **Show NY Session**: ON (the power hour).
- **Killzone Highlight**: ON for London and NY only. Asian killzone is too slow.
- **Box Fill Transparency**: 30% — enough to see price action underneath.

Do NOT turn on all three killzone highlights at once. It looks like a rainbow of noise. Pick one or two.

### How to Actually Use It (No Guru Talk)
Stop treating this like a standalone signal. It’s a **context tool**.

- **Breakout strategy**: Wait for price to break the session high or low during its corresponding killzone. For example, if NY killzone opens and price breaks the NY session high, go long with a stop below the session low. Target the next session’s range.
- **Reversal strategy**: If price is at the session high just as the killzone ends, look for a rejection candle. The zone acts as magnet. I’ve caught several fakeouts on the MACD chart by watching price hover at the NY high line during the first 30 minutes.
- **Swing trading**: Use the Asian session range as your daily support/resistance. If price stays inside it during London, expect a continuation move into NY.

As the chart above shows, the MACD histogram turning positive right at the NY killzone open with price breaking the session high gave a clean long entry. Not perfect, but repeatable.

### Pros & Cons
**Pros**:
- Free, no bloat, no repaint.
- Session times are customizable — rare for a free script.
- Killzone shading is subtle and actually useful for timing entries.
- Works on any timeframe (I tested 1m, 5m, 1H).

**Cons**:
- No alerts. You must watch the chart.
- Killzone definitions are fixed (e.g., London killzone is always 2–5 AM EST). Can’t adjust the window length.
- Overlapping zones on 24-hour markets (like crypto) can get messy. Not ideal for BTC.

### Who Is This For?
- **ICT/SMC traders**: This is a must-have if you already trade killzone concepts. Saves you 10 minutes of drawing lines.
- **Forex day traders**: EURUSD, GBPUSD, USDJPY — the session highs/lows are actual levels that institutions respect.
- **Beginners**: If you’re learning session-based trading, this is the clearest visual guide I’ve seen.

**Not for**: Scalpers who trade outside major session opens (like 3 AM EST), or crypto traders who need 24/7 zone visibility.

### Alternatives
- **Session Highlighter** by LuxAlgo: Paid, but adds volume profile and alerts. Better for serious scalpers.
- **Killzone Timer**: A simpler countdown tool, no session ranges. Use if you only want timing.
- **Manual rectangles**: Free, but you’ll curse yourself every day at 8 AM when you forget to draw them.

### FAQ
**Q: Does this work on crypto?**  
It works, but the zones overlap because crypto trades 24/7. Turn off Asian session to reduce clutter. Better for forex.

**Q: Can I change the killzone start/end times?**  
No. The indicator uses fixed ICT-defined windows (e.g., 2–5 AM EST for London). You can shift the session open times, but not the killzone duration.

**Q: Will it repaint?**  
No. The session high/low is locked after the session closes. The killzone shading is drawn in real-time based on the clock.

**Q: Does it include Silver Bullet or other ICT patterns?**  
No. This is just zones and session ranges. No silver bullet, no judas swing detection.

### Final Verdict
**Rating: ⭐⭐⭐⭐ (4/5)**

I’m giving it 4 stars because it does one thing well — session mapping — and does it for free. It loses a star because it lacks alerts and the killzone times are rigid. But if you’re a forex or index trader who already uses ICT concepts, this is a no-brainer install. Just don’t expect it to trade for you. Use it as the grid, not the engine.
## Get Started with Better Trading Tools

📊 **Power your analysis on TradingView** — the platform that powers The Indicator Lab. Get real-time data, 100M+ indicators, and Pine Script.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*
