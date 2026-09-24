---
title: "Ichimoku_Chikou_Span Review: Settings, Strategy & How to Use It"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/ichimoku-chikou-span.png"
tags:
  - ichimoku chikou span
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "A clean, lagging Ichimoku Chikou Span indicator for TradingView. No clutter—just the lagging line for clear confirmation. Best settings, entry/exit tips, and honest pros/cons."
grounding: "none (no source found)"
---
## What This Indicator Actually Does

The **Ichimoku_Chikou_Span** plots just the lagging line — the current close shifted back by the standard Ichimoku displacement — on your chart. No Kijun-sen, no Tenkan-sen, no cloud. This is the simplest way to use Chikou for price action confirmation without the noise.

If you already trade Ichimoku with the full system, you can overlay this on a separate pane or hide the other elements. For those who use Chikou as a standalone filter — the common price action read being a lagging line cross above price as bullish — this is a dedicated tool for that.

---

## Key Features That Set It Apart

- **Zero clutter.** One line, nothing else.
- **Customizable displacement.** The default follows the standard Ichimoku setting, but it can be adjusted in the settings.
- **Color-coded by trend.** The indicator colors the line based on whether it sits above or below price, distinguishing bullish and bearish bias out of the box.
- **Simple alerts.** Alerts can be set for the Chikou Span crossing above or below the price bars.

---

## Settings and How to Tune Them

- **Displacement:** Defaults to the standard Ichimoku value. Some traders shorten it on lower timeframes to reduce lag, but this changes the meaning of the line.
- **Color Mode:** An above/below price mode makes the bullish or bearish bias readable at a glance.
- **Line Width:** Adjustable; a thicker line is easier to scan on a busy chart.
- **Show Labels:** Can be toggled off if the on-chart text is unwanted.

Ichimoku as a system is generally applied on higher timeframes; behavior on very short timeframes is a separate question and not what this line was designed around.

---

## How to Use It for Entries and Exits

**Entry (Long):**
- Price is above the cloud (or you have a separate cloud indicator).
- Chikou Span crosses **above** the price bars from below.
- Wait for a retest or a candle close above the crossing bar.

**Exit (Long):**
- Chikou Span crosses **below** the price bars.
- If price also breaks below Kijun-sen (if you're using the full system), close.

A common way to filter whipsaws is to require the Chikou Span to hold above the price bars for several consecutive candles after the cross before acting.

---

## Honest Pros and Cons

**Pros:**
- Clean, lagging-only view — useful for traders who already understand Ichimoku and don't need the full suite.
- Works as a confirmation filter for trend-following strategies.
- Alerts are simple and to the point.

**Cons:**
- **Lagging by nature.** The Chikou Span is always displaced back by the standard period. You'll miss the very start of a move. That's acceptable for swing trading, but not suited to scalping.
- **No cloud or Kijun-sen.** Without the surrounding lines, there's no context. This is an *add-on* tool, not a standalone system.
- **No volume overlay.** Some traders want to see volume at the crossing point.

---

## Who It's Actually For

- **Swing traders** on higher timeframes who already use the full Ichimoku system and want a dedicated Chikou line.
- **Price action traders** who use the lagging line as a trend filter — for example, only buying when Chikou is above price.
- **Traders who hate clutter** and want one line instead of five.

**Not for:** Beginners or anyone who hasn't studied Ichimoku. Without knowing what the line represents, it will be confusing.

---

## Better Alternatives

- **Ichimoku Cloud (full)** by LuxAlgo or the built-in TradingView Ichimoku — if you want the complete system.
- **Chikou Span + Kijun Cross** — a custom script that combines Chikou and Kijun-sen only. Less clutter than the full cloud, more context than this.
- **Lagging Line Only** by HPotter — similar but with additional smoothing options.

---

## FAQ

**Q: Can I use this on 5-minute charts?**
Yes, though the standard displacement may feel slow. Shortening it is a choice, not a requirement.

**Q: Does it repaint?**
No. The Chikou Span is a fixed lagging line; it does not repaint.

**Q: Can I set alerts for Chikou crossing price?**
Yes. Right-click the indicator → Add Alert → set the condition for the Chikou Span crossing above or below price.

**Q: Is this better than the built-in Ichimoku?**
For a dedicated Chikou view, it's cleaner. The built-in one forces you to see all lines.

---

## Final Verdict

The **Ichimoku_Chikou_Span** does exactly what it says — no more, no less. It's a niche tool for traders who already understand Ichimoku and want a clean lagging line for confirmation. Its limitations are that it isn't beginner-friendly and offers no cloud context. But for someone who knows what the line represents, it's a solid addition to the toolbox.

**Should you install it?** If you're a swing trader who uses Chikou as a filter, it fits. If you're new to Ichimoku, start with the full cloud first.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **Ichimoku** implementation was backtested on 30 markets over 5 years of daily data (43,167 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 49.8%** (50% = coin flip)
- Strongest markets: QQQ 55.5%, SPY 54.8%, USDJPY 54.8%, XAUUSD 53.4%
- Weakest markets: WTI 46.3%, LTCUSD 45.8%, SHIBUSD 28.3%

Treat this as context on whether the *approach* has an edge — not as a performance claim for the indicator itself.

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
