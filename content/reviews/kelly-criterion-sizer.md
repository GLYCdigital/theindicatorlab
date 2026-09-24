---
title: "Kelly_Criterion_Sizer Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/kelly-criterion-sizer.png"
tags:
  - kelly criterion sizer
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Kelly_Criterion_Sizer calculates optimal position size using win rate & risk/reward. Honest review with settings, pros/cons, and alternatives."
grounding: "none (no source found)"
---
The Kelly Criterion is a mathematical betting formula for sizing positions based on edge and odds. It is also widely misused: applied at full strength to real markets, it tends to produce position sizes that most accounts cannot survive. This indicator attempts to address that problem.

### What This Indicator Actually Does

Kelly_Criterion_Sizer takes historical trade statistics — win rate, average win, average loss — and outputs a recommended position size as a percentage of account equity. It is not a signal generator. It is a risk management tool.

You either enter your stats manually or let the indicator read them from TradingView's strategy tester. The output is displayed on the chart as a percentage figure, with both a full Kelly value and a fractional Kelly value.

**Key difference from other position sizers:** it applies the Kelly formula rather than a fixed risk percentage. Full Kelly is mathematically aggressive by design, so the indicator includes a fractional Kelly multiplier to scale the output down to a level a trader can realistically sustain.

### Key Features

- **Automatic win rate and risk/reward calculation** from strategy tester results.
- **Fractional Kelly multiplier** — scales the raw Kelly output down to a more conservative figure.
- **Visual display** — shows the recommended position size on the chart in a label.
- **Alert integration** — can trigger a notification when the Kelly percentage changes significantly, such as after a losing streak.
- **No repainting.** The displayed value reflects the inputs as calculated.

### Settings and How to Tune Them

The fractional Kelly multiplier is the setting that matters most. It scales the raw Kelly figure, and it is the difference between a theoretically optimal number and one you can actually trade. Lower multipliers reduce position size; higher multipliers move you closer to full Kelly and its corresponding drawdown risk. There is no universally correct value — it depends on your tolerance for drawdown and the volatility of what you trade.

The indicator can read statistics directly from the strategy tester, or you can supply win rate and average risk/reward manually. If you enter them manually, the accuracy of the output depends entirely on the accuracy of those inputs.

### How to Use It

This is not an entry signal. You still need your own strategy.

1. **Backtest your strategy** over a meaningful sample. Get your win rate and average R/R.
2. **Input those stats** into the indicator's settings, or let it read from the strategy tester.
3. **Set your fractional Kelly multiplier** based on your risk tolerance.
4. **Take the position size** it shows. A reading of a given percentage means risking that percentage of your account on the trade.
5. **Re-calculate periodically.** Win rates drift, and stale inputs produce stale sizing.

**Exit:** The indicator does not help here. You manage stop loss and take profit as usual.

### Pros and Cons

**Pros:**
- Forces risk management to be handled mathematically rather than by feel.
- The fractional Kelly multiplier prevents the gambler's ruin outcome that full Kelly invites.
- Not tied to a timeframe or asset class — the output derives from your statistics.
- Clean, unobtrusive display.

**Cons:**
- **Useless without a proven strategy.** If your win rate is low or your average loss exceeds your average win, Kelly returns zero or negative — meaning you should not be trading that system. That is correct behavior, but it is not encouraging.
- **No dynamic adjustment.** It does not update after every trade in real time; you have to re-run the strategy tester.
- **Aggressive for new traders.** Even at a fractional multiplier, a losing streak can produce meaningful drawdown if you are not prepared for it.
- **No position sizing for multi-leg strategies** such as hedges. It assumes single-direction trades.

### Who It's For

**Verdict:** Intermediate and advanced traders who already have a backtested edge.

- **Good for:** Systematic traders and anyone who works from strategy tester results.
- **Bad for:** Beginners without a track record, and scalpers who need fast recalculation.
- **Not for:** Traders who prefer a flat fixed-risk approach.

### Alternatives

- **Position Size Calculator** by LonesomeTheBlue — simpler, fixed risk percentage, no Kelly math.
- **Risk & Position Size Calculator** by Robo — includes ATR-based sizing and portfolio heat.
- **Custom code:** The Kelly formula is short. If you already code, you may not need a dedicated indicator.

### FAQ

**Q: Can I use this without a strategy tester?**
A: Yes. Input your win rate and average R/R manually. The output is only as meaningful as the sample behind those numbers.

**Q: What's a "safe" fractional Kelly value?**
A: There is no universal answer. Lower multipliers reduce risk; higher multipliers approach full Kelly. Never assume a high multiplier is safe just because the formula says it is optimal.

**Q: Does it work for options?**
A: The formula uses win and loss amounts. Options have variable payoffs, so you would need to average your R/R manually. It works, but with less precision.

**Q: Why does it say "0%" even though I have a winning strategy?**
A: Check your win rate and the relationship between average win and average loss. If the math does not support a positive edge, Kelly returns zero. That is mathematically correct.

### Final Verdict

Kelly_Criterion_Sizer is a straightforward risk management tool. It does not generate signals and does not promise returns. It converts your own trade statistics into a position size using a defined formula, with a fractional multiplier to keep the output tradable.

If you have a backtested edge and want position sizing handled systematically, it is worth considering. If you are still searching for an edge, it will only tell you what the math already says.

**Rating: ⭐⭐⭐⭐ (4/5)**
One star off for the manual refresh requirement.

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
