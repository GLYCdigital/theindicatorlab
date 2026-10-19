---
title: "Swing Volume Frequency Profile Review — Volume Indicator"
date: 2026-10-20T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/swing-volume-frequency-profile.png"
tags:
  - "swing volume frequency profile"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "BigBeluga's Swing Volume & Frequency Profile plots volume and time-at-price side by side between the last two swing points. Honest review."
tv_script_url: "https://www.tradingview.com/script/EJhan1MH-Advanced-Swing-Volume-Frequency-Profile-BigBeluga/"
sources: ["https://www.tradingview.com/script/EJhan1MH-Advanced-Swing-Volume-Frequency-Profile-BigBeluga/"]
---
Most volume profile tools anchor to a session, a day, or a fixed lookback. That's convenient, but it means the profile you're reading is often tied to a calendar event rather than to the actual move you care about. BigBeluga's Advanced Swing Volume & Frequency Profile takes a different angle: it anchors the profile to the two most recent swing points and shows you two distributions at once — how much volume traded at each price, and how often price visited each level. That dual view is the whole pitch, and it's a genuinely useful one.

## What it actually does

The indicator finds the most recent highest high and lowest low over a configurable Swing Length lookback and labels them S1 and S2. Everything between those two points becomes the anchor range, extended out to the current bar plus a Profile Offset Bars setting. That range is then sliced into horizontal price rows using ATR(100) multiplied by a Resolution Multiplier — which means the row height adapts to volatility instead of being a fixed tick size you have to babysit.

Once the rows are defined, two things get binned into them. The Volume Profile accumulates traded volume per row across every bar inside the swing. The Frequency Profile counts how many bars touched each row — a proxy for time spent at that price. The row with the highest volume becomes the Volume POC; the row touched the most becomes the Frequency POC.

## The rendering

The layout is mirrored and compact. Volume boxes extend right, with width proportional to volume and color intensity scaled against the maximum. Frequency boxes extend left, same logic applied to visit counts. Dotted horizontal grid lines run across the range, and their intensity follows whichever metric you pick in the Grid Gradient Source toggle. Both POCs get their own highlighted boxes with values labeled on the chart.

As the chart above shows, the MACD panel isn't where this lives — this is a price-panel study, so expect it to occupy chart real estate. The offset setting exists precisely because profiles drawn flush against the current bar get cramped.

## How to use it

The most obvious workflow is treating the Volume POC as a magnet and potential support/resistance — the price where the most size actually changed hands. The Frequency POC is a different animal: it marks where price spent the most time, which usually reads as a consolidation or acceptance level.

The interesting part is when the two POCs separate. Volume POC and Frequency POC sitting at different rows tells you that big trades clustered somewhere price didn't linger, while price spent most of its time somewhere with comparatively little volume. That divergence is information you don't get from a single-metric profile.

From there it's a matter of reading the shape. A balanced swing shows a fairly even distribution; a skewed one shows a clear concentration. You can position entries near the POC rows, or just use the shape as context for whether the swing was trending or rotational. If the grid is too busy, toggle off lines or individual POC boxes.

## Pros and cons

**Pros**
- Anchoring to swings rather than sessions is the right call for swing traders — the profile matches the move you're analyzing.
- ATR-based binning removes the manual resolution guessing that plagues fixed-row profiles.
- Side-by-side volume and frequency is a real analytical upgrade, not a cosmetic one.
- Sensible customization: colors, profile width, offset, gradient source, and display toggles.

**Cons**
- It's a price-panel overlay, so it will crowd a chart that's already busy.
- Swing-based anchoring means the profile shifts as new swings form — that's inherent, but it makes the levels less "fixed" than session profiles.
- ATR(100) is baked in as the volatility base; you get a multiplier, not full control over the row math.
- "Frequency" is a bar-touch count, which is a rough time-at-price proxy rather than a true time-weighted measure.

## Who it's for

Swing traders and range traders who think in terms of where the move happened rather than where the day happened. If you already use volume profile but find session anchoring limiting, this is worth a look. Discretionary traders who want POC levels with context will get more out of it than pure systematic users, since there's no signal generation here — just structure.

## FAQ

**Does it generate buy or sell signals?** No. It's a study that visualizes distribution; interpretation is on you.

**Can I use it on any timeframe?** The source doesn't make timeframe claims. Because resolution is ATR-based, the row sizing adapts to whatever volatility is present.

**What's the difference between the two POCs?** Volume POC = most traded volume. Frequency POC = most bar touches. When they diverge, that's the signal worth studying.

**Can I hide parts of it?** Yes — grid lines and individual POC boxes have display toggles.

## Verdict

A well-reasoned take on volume profile that earns its place through the swing anchoring and the dual-metric view. It's not a signal tool and it won't suit everyone's chart, but the frequency-versus-volume comparison is the kind of nuance most profile indicators skip entirely. Solid, focused, and honest about what it measures.

⭐⭐⭐⭐ (4/5)
## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 123 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $149/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $249/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and the official TradingView script documentation. Always test indicators in a demo environment before live trading.*
