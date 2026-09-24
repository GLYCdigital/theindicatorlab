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
grounding: "none (no source found)"
---
Let's be blunt: most volume indicators on TradingView are just the default volume pane with a different paint job. Volume_Colored actually does something useful with that paint job. Instead of showing you raw volume numbers, it colors each bar based on whether volume is expanding or contracting relative to recent averages — and it does this in a way that's immediately readable without cluttering your chart.

## What Volume_Colored Actually Does

The indicator takes the standard volume histogram and applies a color logic system. Green bars indicate rising volume with price moving up, red indicates rising volume with price falling, and muted/dimmer colors signal declining volume regardless of direction. That's it — no moving averages, no divergence signals, no overbought/oversold zones. It's deliberately minimal.

What sets this apart from alternatives like Volatility-Based Volume or Volume by Price is the transparency feature. You can adjust the opacity of each bar type independently, which means you can overlay it on your price chart without it obscuring candlesticks. Most volume indicators force you to keep them in a separate pane. Overlay mode is genuinely useful for spotting volume spikes at key support/resistance levels without flipping between panes.

## Settings and How to Tune Them

The indicator exposes a handful of inputs worth understanding:

- **Lookback period** — controls how many bars feed the volume baseline. A shorter lookback makes the color logic more reactive; a longer one smooths the baseline and produces fewer color flips but reacts more slowly.
- **Opacity per bar type** — rising and falling volume bars can be set to different opacities, which is what makes overlay mode usable without hiding candles.
- **Color scheme** — a small set of preset palettes, including a green/red default and a teal/orange variant.
- **Overlay mode** — lets the indicator sit on the price chart rather than in a separate pane.

There's no single "best" configuration here; the right lookback depends on your timeframe and how much noise you're willing to tolerate. Shorter settings favor faster reaction, longer settings favor stability. The color thresholds themselves are not user-configurable, so you can't set exact volume percentage changes to trigger a color shift.

## How It's Typically Used

The common reading is straightforward: a green volume bar that's noticeably larger than the preceding bars suggests institutional interest. Pairing that with a separate trend or momentum signal — a histogram flip, a trendline break — is a typical way to frame entries. On the exit side, red expansion bars while price is still climbing can be read as distribution, prompting a tighter stop or partial profit-taking. The indicator won't tell you *why* volume is behaving a certain way, but it tells you *when* it's happening faster than waiting for price action alone.

One caution: this is a confirmation tool, not a standalone system. If you're looking for buy/sell arrows, this isn't it.

## Pros & Cons

**What works:**
- Instant visual read on participation
- Overlay mode genuinely functional — many volume indicators struggle with this
- Clean, uncluttered interface with adjustable opacity per bar type
- Adapts across timeframes without recalibration

**What doesn't:**
- No alerts — you have to watch the chart manually
- Color logic can flip frequently in choppy, low-volume markets
- Doesn't distinguish between buyer-initiated and seller-initiated volume (that's a different indicator entirely)
- Limited customization for the color thresholds — you can't set exact volume percentage changes for color shifts

## Who Should Use This

Traders who already have a price-based strategy and need a volume confirmation layer. Scalpers may find the lookback lag frustrating. For long-term investors, checking weekly volume trends manually is often sufficient.

It's also a reasonable choice for newer traders learning to read volume, because the color coding removes some of the guesswork. It helps develop a feel for what "rising volume on rising price" looks like, which is a foundational skill.

## Alternatives Worth Considering

- **Volume Profile** — better for identifying exact price levels where volume clusters, but more complex
- **OBV (On-Balance Volume)** — better for divergence spotting, but lags significantly
- **Raw Volume with MA overlay** — the bare-bones approach if you want to do your own analysis

## FAQ

**Does this repaint?**
No. The colors are based on closed bars, so once a bar closes, its color is final. This is a significant advantage over many momentum indicators.

**Can I use it on crypto?**
Yes, and it tends to work better on crypto than forex since crypto volume data is more reliable across exchanges.

**Does it work on all TradingView plans?**
Yes, it's available on free and paid plans.

**Can I set alerts on volume spikes?**
Not with this indicator. You'd need to pair it with a separate volume spike alert system.

## Final Verdict

Volume_Colored does one thing and does it well. It makes volume interpretation instant and visual without the bloat that plagues most "all-in-one" indicators on TradingView. It's not revolutionary — it won't replace your primary strategy — but it's a reliable secondary tool that earns its place on your chart.

The lack of alerts and the choppy behavior in low-volume conditions keep it from a perfect score. But for what it delivers — clarity — it's an easy recommendation.

**Rating: ⭐⭐⭐⭐ (4/5)** — A solid, honest volume visualization tool that pairs well with trend-following strategies.

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
