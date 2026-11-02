---
title: "Winchester 10x1t Double Patterns Review — Chart Patterns"
date: 2026-11-03T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/winchester-10x1t-double-patterns.png"
tags:
  - "winchester 10x1t double patterns"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest review of Winchester 10X1T Double Patterns Pro: an automated double top/bottom detector with neckline confirmation, invalidation and a stats panel."
tv_script_url: "https://www.tradingview.com/script/jRcHrjqv-Winchester-10X1T-Double-Patterns-Pro/"
sources: ["https://www.tradingview.com/script/jRcHrjqv-Winchester-10X1T-Double-Patterns-Pro/"]
---
Double tops and double bottoms are the kind of pattern every trader can spot in hindsight and few can define consistently in real time. Winchester 10X1T Double Patterns Pro is an attempt to take the guesswork out of that: it finds the patterns mechanically, draws them on the candles, and tracks whether they confirm or fail. In the Winchester 10X1T framework it is labelled Condition 3 — the structure check, run after the environment is clear. That positioning matters, and it is the lens through which the whole tool should be judged.

## What it actually does

The core is a swing detector. A bar printing the highest high (or lowest low) of the last 10 bars becomes a swing candidate. A leg flips when the first candidate of the opposite side appears, and within a leg only a more extreme candidate can move the swing. Each swing is then ranked against the previous swing on the same side as HH, LH, HL or LL.

From there a double top is defined as a higher high, a pullback low, then a lower high that stops close to the first top. "Close" is quantified by a risk-share measure: the gap between the two tops divided by that gap plus the depth of the pullback, capped at a maximum. That maximum defaults to 30 percent. A double bottom is the mirror image. It is a clean, rule-based definition, and that is the main thing this script offers over eyeballing the chart.

## Confirmation, invalidation and the panel

A pattern is confirmed when price crosses the neckline — the pullback swing. It is invalidated when price crosses the first top or the first bottom. That distinction is the most useful part of the tool: it turns a shape into a binary outcome you can count.

The panel tallies patterns, confirmations and invalidations, and reports the hit rate for tops and bottoms separately. The source material doesn't specify the lookback window for that hit rate, so treat the figure as a relative guide rather than a precise probability. Still, having tops and bottoms broken out separately is more honest than a single blended number.

## Drawing and visual clarity

An M marks a double top, a W marks a double bottom, and the label sits on the second top or bottom showing the risk per reward. Recent swings carry the HH, LH, HL and LL tags. For the newest pattern, the neckline and the first top are drawn as dashed measuring lines on exact price, with the price shown on the scale. Confirmation and invalidation each get their own dashed line on the bar where they occur. Every element can be switched off, and colours darken on a light chart. It's a tidy, non-cluttered presentation, which is rarer than it should be.

## Continuity with the earlier study

One detail worth highlighting for existing users: with default settings (length 10, max risk per reward 30) the script is stated to find exactly the same patterns, pivots, confirmations and invalidations, and fire alerts on the same bars, as the older Double Patterns study. The authors say they checked this side by side over more than 150,000 bars across several symbols and timeframes. I'm passing that on as a claim from the documentation, not a result I verified. The practical upshot is that the data window keeps the same column names, so anyone reading values programmatically or from a spreadsheet won't have to rebuild anything.

## How to use it

The documentation is refreshingly blunt here: read it after the environment and momentum are clear, and treat the pattern as structure — not an entry signal. In the 10X1T method the entry comes later, after the pressure phase and the cipher dot. If you buy the second top because the M appeared, you are using the tool against its own stated design. Alerts exist for double tops, double bottoms, plus confirmation and invalidation for each, so it can run in the background while you watch the higher-level context.

## Pros and cons

**Pros**
- Objective, rule-based pattern definition with a quantified proximity threshold, so no more "close enough".
- Neckline confirmation and invalidation tracked and counted separately for tops and bottoms.
- Clear drawing with measuring lines on exact price and a risk-per-reward label.
- Full control over every visual element; sensible light-chart colour handling.
- Alerts on patterns, confirmations and invalidations.
- Backward compatible with the earlier study's output and data window.

**Cons**
- It is a structure tool, not a signal generator — by design, which will frustrate anyone wanting entries.
- The hit-rate panel's sample window isn't documented in the source description.
- Pattern logic follows public open-source double top/bottom work by Trendoscope; the value-add here is the counting, panel and drawing rather than the underlying concept.
- If you don't use the 10X1T workflow, the "Condition 3" framing and later entry steps won't mean much to you.

## Who it's for

Discretionary traders who already identify double tops and bottoms manually and want a consistent, auditable version of that process. It suits swing and position traders on higher timeframes more than scalpers, given the 10-bar swing structure. It is clearly built for students of the Winchester 10X1T method, but the pattern detection stands on its own for anyone who wants structure marked and scored.

## FAQ

**Does it give buy or sell signals?** No. The pattern is structure; entries are taken later in the 10X1T sequence.

**What counts as "close" for a valid double top?** The gap between the tops divided by that gap plus the pullback depth must stay under the maximum, 30 percent by default.

**What invalidates a pattern?** Price crossing the first top (or first bottom).

**Can I hide the labels and lines?** Yes — every element can be switched off in settings.

**Will my existing alerts and data columns change?** Per the documentation, the defaults reproduce the same patterns and alerts as the earlier study, and the data window keeps the same column names.

## Verdict

Four stars. This is a well-scoped tool that does one job properly: it defines double tops and bottoms rigorously, draws them cleanly, and — crucially — tracks whether they confirm or fail instead of pretending every pattern is a winner. The ceiling is that it isn't an entry system, and the underlying pattern concept isn't novel. But as a structure filter inside a broader method, it earns its place on the chart.

⭐⭐⭐⭐
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
