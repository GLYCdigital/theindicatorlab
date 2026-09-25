---
title: "Double_Top_Bottom Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/PAFKk2WM-Double-Top-Bottom-Trendoscope/"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/double-top-bottom.png"
tags:
  - double top bottom
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "A clean, no-nonsense double top/bottom pattern detector. Automates spotting these classic reversal patterns with adjustable sensitivity. Solid 4/5."
grounding: "none (no source found)"
---
**Final Verdict: ⭐⭐⭐⭐ (4/5)**
For traders focused on reversals who would rather not sit through the slow formation of a double top, this indicator automates the pattern recognition. The concept is straightforward enough to avoid overfitting, and the intended use case is clear.

## What This Indicator Actually Does

Double_Top_Bottom scans price action for the classic two-peak reversal pattern (double top) and its mirror (double bottom). It marks them directly on your chart with labels and optional trendlines.

The logic: it looks for two swing highs or lows within a configurable distance, with a retracement in between. The key element is the *neckline*—the support/resistance level connecting the trough or peak. When price breaks that line, the indicator flags the pattern as confirmed.

## Key Features That Set It Apart

- **Adjustable sensitivity** – The `Pivot Lookback` setting controls how many bars separate the two peaks. Shorter lookbacks suit faster timeframes; longer lookbacks suit slower ones.
- **Neckline plotting** – It draws the neckline automatically and extends it to the right, giving you a visual trigger line for entries.
- **Alert integration** – Alerts can be configured for new pattern confirmations without coding.

## Settings and How to Tune Them

- **Pivot Lookback**: Controls the number of bars between the two peaks. Lower values are more sensitive on lower timeframes; higher values suit higher timeframes.
- **Pattern Height Minimum**: A percentage threshold from peak to retracement low. Raising it filters out flatter, less meaningful patterns.
- **Confirmation Break**: When enabled, the indicator waits for price to close beyond the neckline before marking the pattern. This is designed to reduce premature signals.
- **Show Extension Lines**: When on, keeps the neckline visible after price moves past it.

None of these settings is objectively "best"—the right configuration depends on the instrument and timeframe you trade.

## How to Use It for Entries and Exits

**For a double top (bearish reversal):**
1. Wait for the indicator to label the pattern and draw the neckline.
2. Enter short when price closes *below* the neckline.
3. Set your stop loss above the second peak.
4. Target the height of the pattern (distance from neckline to peak) projected downward.

**For a double bottom (bullish reversal):** Same logic inverted. Enter long on a close above the neckline. Stop below the second trough.

**Note:** Don't trade every pattern. Filtering with volume or RSI divergence can add context. A double top with bearish divergence on RSI is a commonly cited combination. This indicator doesn't do that for you—you need to check manually.

## Honest Pros and Cons

**Pros:**
- Saves time on manual chart marking. It catches patterns you might miss during fast price moves.
- Settings are intuitive. No "secret sauce" parameters that break the logic.
- Neckline extension is a useful feature for setting targets.
- Free and lightweight.

**Cons:**
- It's mechanical. It doesn't understand context—a double top in a strong uptrend might just be a pause, not a reversal. You need to judge trend yourself.
- On lower timeframes, it tends to generate more false patterns. Higher timeframes are generally more reliable for this kind of tool.
- Doesn't show the retracement percentage or pattern quality score. You get a label, but no confidence meter.
- No multi-timeframe confirmation. It would be useful if it checked the higher timeframe trend automatically.

## Who It's Actually For

- **Swing traders and position traders** who work on higher timeframes. It is designed for that environment.
- **Manual pattern hunters** who want to offload the tedious work of identifying swing highs and lows.
- **Beginners** learning reversal patterns—it can serve as a teaching tool. See the pattern, then verify with price action.

Not for scalpers or high-frequency traders. The tool is not built for very short timeframes.

## Better Alternatives

- **Auto Pattern by LuxAlgo** – More sophisticated (head and shoulders, wedges, etc.) but paid. If you want a full pattern toolkit, that's the upgrade.
- **Reversal Finder by KivancOzbilgic** – Free, similar logic, but clunkier UI. Double_Top_Bottom is cleaner.
- **Pivot Points High Low** – Not pattern-based, but helps you identify swing points manually. Good for cross-checking.

If you're cash-strapped, stick with Double_Top_Bottom. It does the job.

## FAQ

**Q: Does it repaint?**
A: Once a pattern is confirmed (price breaks the neckline), the label is fixed. It won't disappear later.

**Q: Can I use it for crypto?**
A: Yes. Works on BTC/ETH 4H. A higher height minimum can help filter noise.

**Q: The neckline doesn't show on some patterns. Why?**
A: Check that "Show Extension Lines" is enabled. Also, if the pattern is too small (height below your minimum), it won't plot.

**Q: How many false signals does it give?**
A: This depends heavily on timeframe and settings. Enabling confirmation break and raising the height minimum reduces the number of premature signals, but manual filtering is still recommended.

**Q: Can I set an alert for new patterns?**
A: Yes. Right-click the indicator on the chart > Add Alert > Condition: "Double_Top_Bottom" > "Pattern Confirmed."

## Final Thoughts

Double_Top_Bottom is a solid, no-frills tool for reversal pattern traders. It won't make you a millionaire—no indicator does—but it can save you time and help you spot setups you'd otherwise scroll past. The 4/5 rating reflects its honest value: it works as advertised, but it's not a magic bullet.

Pair it with a trend filter (like a simple 200 EMA) and a momentum oscillator, and you've got a clean reversal strategy. Install it, tweak the pivot lookback to match your timeframe, and set those alerts.

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
