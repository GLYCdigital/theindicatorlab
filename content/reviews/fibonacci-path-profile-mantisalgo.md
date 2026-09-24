---
title: "Fibonacci_Path_Profile_Mantisalgo Review: Settings, Strategy & How to Use It"
date: 2026-08-29
draft: false
type: reviews
image: "/screenshots/fibonacci-path-profile-mantisalgo.png"
tags:
  - "fibonacci path profile mantisalgo"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest Fibonacci_Path_Profile_Mantisalgo review: tested settings, entry/exit strategy, pros/cons, and who should use this trend indicator."
tv_script_url: "https://www.tradingview.com/script/BU7wGOjd-Fibonacci-Path-Profile-MantisAlgo/"
sources: ["https://www.tradingview.com/script/BU7wGOjd-Fibonacci-Path-Profile-MantisAlgo/"]
---
Let me cut through the name. Fibonacci Path Profile isn't a static Fibonacci retracement tool — it's a historical swing-path analysis study that compares the active market structure against similar Fibonacci swing patterns from the past. The core output is a distribution of where the next D and E swing points have historically formed.

**What This Indicator Actually Does**

The indicator automatically detects alternating swing highs and lows and organizes them into an A-B-C structure. In a bullish ABC, A→B is an upward impulse and B→C is a downward retracement, with the next D swing developing upward from C. In a bearish ABC, the reverse applies. A→B is used as the base swing for all subsequent Fibonacci measurements.

It then measures the B→C movement relative to the A→B impulse and matches historical cases using three filters: ABC direction, B→C Fibonacci range, and live C→Now progress. The result is a set of profiles showing the historical distribution of the next two swing points — the D Path (next swing after C) and the E Path (the swing after D). Both are normalized relative to the B→C range so historical structures of different absolute sizes can be compared on the same basis.

This is not a fixed Fibonacci price target. It's a probabilistic view of the active structure built from historical swing distributions.

**Key Features That Set It Apart**

- **Historical matching, not projection** — The indicator doesn't draw a cone of future price. It pools past cases that matched the current setup and shows how those cases actually resolved. The displayed percentages represent the weighted share of each outcome among currently matched cases.
- **Live refinement** — The active profile recalculates as price develops, updating C→Now progress, matched cases, and both path distributions continuously.
- **Dynamic C handling** — Before a new D swing is confirmed, the B→C retracement may extend to a new extreme. Bullish ABC updates C to a new lower low; bearish ABC updates C to a new higher high. This prevents an unfinished leg from being locked in as a completed swing.
- **E Path structural outcomes** — The E Path is separated into three outcomes: B Break (E moves beyond B), No Break (E remains between B and C), and C Break (E moves beyond C).

**Settings and How to Tune Them**

The indicator exposes a weighting method and a set of Fibonacci matching ranges. The B→C ranges are fixed: 0–23.6%, 23.6–38.2%, 38.2–50%, 50–61.8%, 61.8–78.6%, 78.6–100%, 100–127.2%, 127.2–161.8%, and 161.8%+. Values up to 100% are classified as a Retrace; values above 100% are classified as an Extension. To preserve a usable historical sample, all B→C values above 161.8% are grouped into a single 161.8%+ matching range rather than divided into additional extension classes. Similarly, D and E profile values beyond the displayed ±161.8% range are grouped into the outermost top or bottom bin.

The weighting method has two options:

- **Recent** — More recent historical cases receive greater weight, using Weight = 1 / (1 + Age / 1500), where Age is measured in bars. Use this to emphasize newer market behavior.
- **Equal** — Every matched historical case receives the same weight, giving an unweighted historical distribution.

There is no single correct choice here. Recent biases the sample toward current market behavior; Equal shows the raw distribution. The selection should reflect what the trader wants the sample to represent.

**How to Read It**

Use the indicator to evaluate how similar historical structures developed from the current setup. D Path highlights where the next swing historically tended to form. E Path shows how price developed after that D swing, broken into B Break, No Break, and C Break outcomes. C→Now continuously refines the sample as the active move progresses.

Because D and E represent the active forward path, both profile boxes are always displayed to the right of the current candle.

**Pros & Cons**

**Pros:**
- Grounded in historical swing behavior rather than a single fixed Fibonacci level.
- Continuous refinement as the active move develops, rather than a static snapshot.
- Dynamic C handling keeps an unfinished retracement leg from being treated as confirmed.
- Clear structural framing through the ABC skeleton and the B Break / No Break / C Break breakdown.

**Cons:**
- The profiles represent historical swing distributions, not traded volume. They are not a fixed price target.
- The output is probabilistic and depends on the size and relevance of the matched historical sample.
- Traders who want a single line to trade against will find the distribution format harder to act on.

**Who This Is For**

Traders who already work with Fibonacci structure and market swings and want a historical, probabilistic layer on top of the current ABC setup. It is not designed as a standalone signal generator or a fixed-target tool.

**Alternatives Worth Considering**

- **Static Fibonacci retracement tools** — Simpler, but they draw fixed levels rather than comparing against historical outcomes.
- **Pivot-based swing indicators** — Good for identifying structure, but they don't pool historical analogues.

**FAQ**

**What does the indicator actually measure?**
It detects the current A-B-C structure, measures B→C relative to A→B, filters historical cases by direction, B→C range, and C→Now progress, then shows the historical distribution of the next D and E swing points.

**What are the B→C ranges?**
0–23.6%, 23.6–38.2%, 38.2–50%, 50–61.8%, 61.8–78.6%, 78.6–100%, 100–127.2%, 127.2–161.8%, and 161.8%+. Up to 100% is a Retrace; above 100% is an Extension.

**What do B Break, No Break, and C Break mean?**
They describe the E Path outcome: B Break means E moves beyond the B level, No Break means E remains between B and C, and C Break means E moves beyond the C level.

**Does the profile update in real time?**
Yes. The active profile is continuously recalculated as price develops, which can update C→Now progress, matched cases, and both path distributions.

**Is this a price target?**
No. The profiles represent historical swing distributions, not traded volume, and are designed to provide a probabilistic view of the active structure rather than a fixed Fibonacci price target.

**Final Verdict**

This is a well-defined historical swing-path tool built around a clear ABC structure and a documented matching methodology. The value is in the framing: it shows how similar past structures resolved, broken into D and E path distributions and the three E outcomes. It is not a prediction engine and not a fixed-target indicator, and it should not be treated as one. For traders who already think in terms of Fibonacci swings and market structure, it offers a genuinely different lens. For anyone looking for a single line to trade against, it isn't that.

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
