---
title: "Mynd_Risk_Based_Position_Size_Calculator_5 Review: Settings, Strategy & How to Use It"
date: 2026-09-02
draft: false
type: reviews
image: "/screenshots/mynd-risk-based-position-size-calculator-5.png"
tags:
  - "mynd risk based position size calculator 5"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest Mynd_Risk_Based_Position_Size_Calculator_5 review: tested settings, honest pros/cons, and whether this position sizing tool beats manual risk math."
tv_script_url: "https://www.tradingview.com/script/dyQbUVmQ-MYND-Risk-Based-Position-Size-Calculator-v1-5/"
sources: ["https://www.tradingview.com/script/dyQbUVmQ-MYND-Risk-Based-Position-Size-Calculator-v1-5/"]
---
**The short version:** the position-sizing calculator space on TradingView is crowded with near-identical scripts, and the MYND Risk-Based Position Size Calculator [v1.5] doesn't reinvent the math. What it does differently is treat sizing as a decision framework rather than a single formula — three selectable risk philosophies, a dashboard that shows its work, and trade-management features layered on top. That earns it a look, though the value depends entirely on inputs you supply yourself.

**What it actually does**

At its core, this is a calculator, not a signal generator. It answers one question: given your account, your entry, your stop, and your chosen risk philosophy, how many shares or contracts should you put on.

The baseline mode, Fixed % Risk, uses the industry-standard formula — (Account Equity × Risk%) / Stop Distance. Nothing unusual there. The two alternative modes are where it diverges. Van Tharp R-Multiple/Expectancy uses the same sizing math but gates it on a positive Expectancy first, computed from your own supplied Win Rate, Average Win (R), and Average Loss (R) via Van Tharp's textbook formula. Kelly Criterion derives a dynamic risk percentage from your supplied Win Rate and Win/Loss Ratio using the classic f* = p − q/b formula, then applies that within the same stop-distance sizing formula — a disclosed practitioner adaptation rather than a literal full-bankroll wager — with a Kelly Fraction Multiplier (Half-Kelly by default) on top.

That last point matters. The script is explicit that it has no access to your actual trade history. It is not a strategy backtester. The Van Tharp, Kelly, and Losing-Streak Survivability inputs are numbers you supply from your own trading record, and the output is only as good as those numbers.

**Key features that stand out**

The dashboard is the main draw. It shows every step of the calculation live, including status tags and a P&L row, so you can see where a number came from instead of trusting a black box. A Max Position Size safety cap is always applied on top of whichever mode's raw output — a sensible guardrail when Kelly or a high risk percentage spits out something aggressive.

Up to seven reference lines can be plotted directly on the chart, each with an optional price label. There's a full theme system (Light/Dark/Custom) plus a Colorblind-Safe Okabe-Ito palette, tooltip coverage on every non-obvious setting, and Combo Alert Bundling.

The trade-management layer is optional but notable: a Break-Even Trigger, a three-tier Partial Profit-Taking Ladder, a Losing-Streak Survivability estimate, a Risk:Reward Ratio readout, and a ladder allocation check.

**Settings and How to Tune Them**

The settings the author flags as worth tuning first:

- **Account Equity and Risk % of Equity Per Trade** — the two inputs everything else is built on.
- **Max Position Size (% of Equity)** — the safety cap applied on top of raw output.
- **Entry Price** — fixed versus live close. For an actual open trade, set a fixed entry price so Live P&L and the [REACHED] tags mean something.
- **Risk % Warning Threshold** — triggers the High Risk % alert.
- **Partial Ladder Tier R-Multiples/%** — configures the scaling-out ladder.
- **Milestone Status Lookback (bars)** — increase for trades held longer than 100 bars.

The author's own guidance on mode selection is to start with Fixed % Risk if you don't have reliable win-rate and R-multiple stats yet. That's the honest framing: the more sophisticated modes are gated on data quality, not on preference.

**How it's meant to be used**

Set account equity, direction, entry price, and stop method. Check the Risk:Reward Ratio and Ladder Allocation Check rows as quick sanity checks. Turn on the Partial Ladder if you scale out of positions, and the Break-Even Trigger if you follow a move-to-break-even habit.

Worth repeating: this will not tell you where to enter or where to place your stop. It only answers "how much do I buy?" If you need entries, this isn't that tool.

**Pros and cons**

Pros: Three distinct risk philosophies in one script, with the Expectancy and Kelly modes properly gated rather than blindly applied. A dashboard that exposes the full calculation chain. A Max Position Size cap applied unconditionally. Optional break-even and partial-ladder management. A colorblind-safe palette and thorough tooltips — small things that suggest the author actually uses the tool.

Cons: It's not standalone. The Van Tharp and Kelly modes are only as good as the historical stats you feed them, and the script says so plainly. There's no volatility-based (ATR) sizing mode. Every number is a mechanical consequence of your inputs — the tool doesn't evaluate whether a trade is a good idea, and it isn't trying to.

**Who should install this**

Traders who already have a defined strategy with clear stop levels and need position size computed without a spreadsheet. Prop firm traders or disciplined retail traders working under risk limits are the natural fit. It's also reasonable for newer traders learning proper risk sizing, provided they understand the advanced modes require real stats to mean anything.

If you eyeball position sizes or trade full margin, skip it. And if you're looking for entries rather than sizing, look elsewhere.

**Alerts**

Eleven individual alert conditions: Negative Expectancy Warning, No Kelly Edge Warning, Position Capped by Max Size, Zero Stop Distance Warning, High Risk % Warning, Ladder Over-Allocated Warning, Break-Even Trigger Reached, Take-Profit Target Reached, and Partial Ladder Tier 1/2/3 Reached. Plus two combo bundles — ALL Risk Warnings and ALL Trade Management Milestones.

**Final verdict**

The MYND Risk-Based Position Size Calculator is a focused tool that does one job and is upfront about its limits. The three-mode structure, the always-on max size cap, and the optional trade-management ladder give it more depth than the typical sizing script. It won't make you a better trader, but it will stop you from making one of the most common mistakes in the game — risking too much on a single trade. The script itself carries the standard disclaimer: informational and educational purposes only, not financial advice, and past performance does not guarantee future results.

## Frequently Asked Questions

### What does this indicator actually calculate?

Position size — shares or contracts — based on account equity, risk percentage, and stop distance. Three modes are available: Fixed % Risk, Van Tharp R-Multiple/Expectancy, and Kelly Criterion. The latter two require you to supply your own win rate and R-multiple or win/loss ratio statistics.

### Does this indicator repaint?

The source material does not make any claim about repainting. What it does state is that the tool is a calculator, not a backtester — it has no access to your trade history, and every output is a mechanical consequence of the inputs you provide.

### Can I use it without supplying my own trade statistics?

Yes, in Fixed % Risk mode, which the author recommends starting with if you don't have reliable win-rate or R-multiple stats yet. The Van Tharp and Kelly modes are gated on those inputs by design.

### Is it free?

The source material does not state pricing or access terms. Check the TradingView listing for current status.

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
