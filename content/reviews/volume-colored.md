---
title: "Volume_Colored Review: Settings, Strategy & How to Use It"
date: 2026-08-23
draft: false
type: reviews
image: "/screenshots/volume-colored.png"
tags:
  - "volume colored"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Volume_Colored review: color-coded volume bars reveal trend strength and reversals. Settings, entry strategies, pros/cons, and who should use it."
---
Let's be blunt: most volume indicators on TradingView are just the default volume pane with a different paint job. Volume_Colored actually does something useful with that paint job. Instead of showing you raw volume numbers, it colors each bar based on whether volume is expanding or contracting relative to recent averages — and it does this in a way that's immediately readable without cluttering your chart.

I tested this on a MACD chart setup (which pairs surprisingly well with it) across multiple timeframes, and here's what I found.

## What Volume_Colored Actually Does

The indicator takes the standard volume histogram and applies a color logic system. Green bars indicate rising volume with price moving up, red indicates rising volume with price falling, and muted/dimmer colors signal declining volume regardless of direction. That's it — no moving averages, no divergence signals, no overbought/oversold zones. It's deliberately minimal.

What sets this apart from alternatives like Volatility-Based Volume or Volume by Price is the transparency feature. You can adjust the opacity of each bar type independently, which means you can overlay it on your price chart without it obscuring candlesticks. Most volume indicators force you to keep them in a separate pane. I found the overlay mode genuinely useful for spotting volume spikes at key support/resistance levels without flipping between panes.

## Best Settings I Tested

The default settings are decent but not optimal. After running it through several sessions, here's what worked:

- **Lookback period: 14** (default is 9) — smoother volume baseline, fewer false color flips
- **Opacity: 50% for rising volume, 35% for falling** — keeps the chart readable
- **Color scheme: Green/Red** — the default is fine, but I found the teal/orange variant easier on the eyes for long sessions
- **Enable overlay mode** — this is where the indicator shines

If you're day trading, drop the lookback to 7. For swing trading, 20+ filters out noise but lags significantly. The 14 sweet spot worked across 5-minute and 4-hour charts.

## How I Actually Used It

The entry logic is straightforward: wait for a green volume bar that's noticeably larger than the previous five bars. That's your institutional interest signal. I paired this with a simple trendline break on the MACD chart — when the histogram flipped positive and Volume_Colored showed expanding green volume, that was my long entry.

For exits, red expansion bars were my warning signal. If price was still climbing but volume turned red, that meant distribution was happening. I'd tighten my stop or take partial profits. The indicator won't tell you *why* volume is behaving a certain way, but it tells you *when* it's happening faster than waiting for price action alone.

One thing I'll caution: this is a confirmation tool, not a standalone system. If you're looking for buy/sell arrows, this isn't it.

## Pros & Cons

**What works:**
- Instant visual read on institutional participation
- Overlay mode genuinely functional — most volume indicators fail at this
- Clean, uncluttered interface with adjustable opacity per bar type
- Works across all timeframes without recalibration

**What doesn't:**
- No alerts — you have to watch the chart manually
- Color logic can flip frequently in choppy, low-volume markets
- Doesn't distinguish between buyer-initiated and seller-initiated volume (that's a different indicator entirely)
- Limited customization for the color thresholds — you can't set exact volume percentage changes for color shifts

## Who Should Use This

Day traders and swing traders who already have a price-based strategy and need a volume confirmation layer. If you're a scalper, the lookback lag will frustrate you. If you're a long-term investor, this is overkill — you're better off checking weekly volume trends manually.

This is also a solid choice for newer traders learning to read volume because the color coding removes the guesswork. You'll develop a feel for what "rising volume on rising price" looks like, which is a foundational skill.

## Alternatives Worth Considering

- **Volume Profile** — better for identifying exact price levels where volume clusters, but more complex
- **OBV (On-Balance Volume)** — better for divergence spotting, but lags significantly
- **Raw Volume with MA overlay** — the bare-bones approach if you want to do your own analysis

## FAQ

**Does this repaint?**
No. The colors are based on closed bars, so once a bar closes, its color is final. This is a significant advantage over many momentum indicators.

**Can I use it on crypto?**
Yes, and it actually works better on crypto than forex since crypto volume data is more reliable across exchanges.

**Does it work on all TradingView plans?**
Yes, it's available on free and paid plans.

**Can I set alerts on volume spikes?**
Not with this indicator. You'd need to pair it with a separate volume spike alert system.

## Final Verdict

Volume_Colored does one thing and does it well. It makes volume interpretation instant and visual without the bloat that plagues most "all-in-one" indicators on TradingView. It's not revolutionary — it won't replace your primary strategy — but it's a reliable secondary tool that earns its place on your chart.

The lack of alerts and the choppy behavior in low-volume conditions keep it from a perfect score. But for what it costs (free) and what it delivers (clarity), it's an easy recommendation.

**Rating: ⭐⭐⭐⭐ (4/5)** — A solid, honest volume visualization tool that pairs well with trend-following strategies. Install it, set the lookback to 14, and let it confirm your existing setups.
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
