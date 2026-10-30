---
title: "Machine Learning Fibonacci Feels Review — Momentum Indicator"
date: 2026-10-31T00:00:00+08:00
draft: false
type: reviews
image: "/screenshots/machine-learning-fibonacci-feels.png"
tags:
  - "machine learning fibonacci feels"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest review of Machine Learning Fibonacci [FEELS]: a k-NN weighted fib grid built from a chart's own past pullbacks. What it does, limits, verdict."
tv_script_url: "https://www.tradingview.com/script/4qro0ui0-Machine-Learning-Fibonacci-FEELS/"
sources: ["https://www.tradingview.com/script/4qro0ui0-Machine-Learning-Fibonacci-FEELS/"]
---
Most Fibonacci tools ask you to pick two points and trust the ratios that come out. This one asks a different question: on this chart, where did pullbacks actually stop on legs that looked like the one in play? The answer comes from the past legs themselves, not from convention.

## What it actually does

The script identifies the leg currently in play — the move from the last confirmed swing point — and draws a standard Fibonacci grid on it, 0 at the end and 1 at the start. Then it goes looking through the chart's own history for finished legs that resemble the current one: same direction, similar size, similar length. Each of those past legs is remembered with two features (size in ATR and length in bars) and one answer: how deep its pullback went as a fraction of the leg.

A k-nearest-neighbours model picks the closest matches, and each one votes at the fib level nearest its own pullback depth. The level with the most votes gets marked ML LEVEL. Every level's line is drawn as strong as its vote count — grey where nothing turned.

That's the honest core of it. It's a weighted fib, weighted by the chart's own behaviour.

## How you read it

The grid stays familiar: same orientation as the manual fib tool. What's new is the dots. Each dot next to a number represents one similar past leg that turned at that level. A cluster of dots on one line means those legs agreed; dots smeared across every level mean they didn't. Both readings are informative.

The gold boxes on the chart are the similar past legs themselves, captioned with where they turned. Hovering a caption reveals its rank, size, length and exact depth. That transparency is the feature I'd point to first — the evidence is visible, not buried in a black box. If the chart is too short on history, the script says "ML is learning" and just draws the grid.

The level is redrawn as the leg grows, since a bigger or longer leg has different neighbours. Swings and the learning set are decided on closed bars, which keeps things stable.

## Settings that matter

A swing ends when price moves against it by 4 ATR (ATR 14) by default. On calm markets like stock indices the author suggests 3 for more recent legs to learn from. The model defaults to 9 similar legs, remembers the last 150 finished legs, and compares only same-direction legs unless you turn that off. There's also an "exact view": raw dots, a zone for the middle half, and their median as the level. And three alerts — price reaching a level similar legs turned at, price reaching the ML level, and a new swing point confirming.

## Pros and cons

**Pros:** The reasoning is on the chart, not hidden. Open source, so you can read or change it. The "ML is learning" state is a fair admission that early-chart data is thin. Three useful alerts. Every colour, number and position is adjustable.

**Cons:** The model is k-NN on two features — it's machine learning in the plainest sense, not a neural network, and the name oversells that. It learns only from pullbacks after which the trend continued, so it describes where pullbacks stopped in legs that worked — it can't tell you whether the current pullback will stop at all. Different data feeds carry different history, so the level can differ between them. And votes often disagree; as the BTC example in the source shows, one visible past leg turning at 0.382 while the majority voted 0.5 is not a contradiction, just a reminder.

## Who it's for

Discretionary trend traders who already use fibs and want a data-driven weighting rather than fixed ratios. Swing traders on instruments with plenty of history. Anyone who wants to inspect the evidence rather than accept a level. If you need a signal generator with a scoreboard, this isn't it — the script doesn't score itself, and nothing here is a forecast.

## FAQ

**Is this a neural network?** No. It's k-nearest neighbours on two features. The author is upfront about that.

**Does it predict whether my pullback will reverse?** No. It shows where similar past pullbacks stopped in legs that continued. That's a reference, not a forecast.

**Why does the level move as the leg grows?** Because the leg's size and length change, so its nearest neighbours change too.

**Can I see which legs voted?** Yes — they're framed in gold boxes with captions, and hovering reveals rank, size, length and depth.

## Verdict

A genuinely useful reframing of the fib grid: instead of trusting ratios, it asks your chart what it has done before. The transparency — dots, boxes, captions — is what earns it a recommendation. The limitations are real and the author states them plainly. Four stars: exceptional in concept and honesty, unproven in edge.

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
