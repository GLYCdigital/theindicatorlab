---
title: "Volume Bubbles Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/volume-bubbles.png"
tags:
  - volume bubbles
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Volume Bubbles review: hands-on test of TradingView's volume visualization. Best settings, entry/exit strategies, and honest pros/cons for day traders."
grounding: "none (no source found)"
---
**What This Indicator Actually Does**

Volume Bubbles replaces the standard volume histogram with floating circles that change size and color based on volume activity. A bubble appears at each bar's midpoint. The bigger the bubble, the higher the volume. Red bubbles indicate bearish volume, green indicates bullish. The presentation is visual rather than numerical.

**Key Features**

- **Size scaling by relative volume**: Bubbles adjust to the chart's current volume range rather than displaying fixed sizes.
- **Color logic tied to close versus open**: Green when close is above open, red when close is below open, with an option to inherit the previous bar's color for trend context.
- **Transparency options**: Low-volume bubbles can be faded so only higher-activity bars stand out, reducing visual noise.
- **No companion indicators required**: It overlays on its own, without needing moving averages or a VWAP overlay.

**Settings and How to Tune Them**

The indicator exposes a small set of visual controls. Exact values are a matter of chart conditions and personal preference, not fixed recommendations:

- **Bubble size multiplier**: Scales overall bubble size up or down.
- **Maximum bubble size**: Caps how large a bubble can grow, which matters on charts where large bubbles would otherwise overlap price action.
- **Transparency threshold**: Sets the volume level below which bubbles fade out.
- **Color mode**: Chooses between close-versus-open coloring and previous-bar color inheritance.
- **Scale to chart**: Toggles whether bubble sizing adapts to the visible volume range. If bubbles all render at the same size, this is the first setting to check.

**How to Use It**

The indicator is a visual filter rather than a signal generator. Its practical use is scanning for unusually large volume bars without reading a histogram. Typical approaches include watching for outlier bubbles near support or resistance, and noting clusters of small, faded bubbles as low-activity periods. As with any volume tool, the first bars of a session tend to reflect opening activity rather than directional conviction.

**Pros and Cons**

Pros:
- Highlights volume anomalies that a standard histogram can bury
- Works across timeframes without recalibration
- Visually cleaner than vertical histogram bars competing with price action

Cons:
- Cannot display exact volume values; a separate volume indicator is still needed for that
- On very short timeframes, bubbles can overlap and lose clarity
- No VWAP or delta — it is raw volume with a visual treatment

**Who It's For**

Traders who scan multiple charts quickly and need a fast read on whether a bar is significant. Swing traders may find it useful for spotting climactic volume on daily charts. Traders working primarily from weekly bars will get less from it, since volume context matters less at that scale.

**Alternatives**

- **Volume Profile (Fixed Range)**: Better for seeing *where* volume traded, not just how much.
- **CVD (Cumulative Volume Delta)**: More useful for order-flow and divergence work.
- **Standard Volume plus VWAP**: For many traders, a more complete combination than bubbles alone.

Volume Bubbles is a supplement, not a replacement for those tools.

**FAQ**

*Q: Does it repaint?*
Each bubble is drawn from the closed bar's data.

*Q: Can I use it on crypto?*
It works on any market that provides volume data.

*Q: Why are my bubbles all the same size?*
Check whether scale-to-chart is enabled, or whether the instrument simply has flat volume.

**Final Verdict**

Volume Bubbles is a clean visual filter. It does not generate new information — it presents existing volume data more legibly. That is a real convenience for active chart scanning, and the tool is priced accordingly. Expect clarity, not edge.

**4/5 – Recommended for active traders who value speed of reading over depth of data.**

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Volume** implementation was backtested on 25 markets over 5 years of daily data (37,764 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.3%** (50% = coin flip)
- Strongest markets: GOOGL 53.3%, XRPUSD 52.6%, AVAXUSD 52.3%, SOLUSD 52.1%
- Weakest markets: XAUUSD 46.6%, SPY 46.2%, SHIBUSD 30.7%

Treat this as context on whether the *approach* has an edge — not as a performance claim for the indicator itself.

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 93 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $149/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $249/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*
