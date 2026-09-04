---
title: "Ttp_Imb_Unfilled_Imbalances Review: Settings, Strategy & How to Use It"
date: 2026-09-05
draft: false
type: reviews
image: "/screenshots/ttp-imb-unfilled-imbalances.png"
tags:
  - "ttp imb unfilled imbalances"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Ttp_Imb_Unfilled_Imbalances review: a practical look at how this ICT-style imbalance tool spots unfilled gaps, best settings, entry logic, and who should use it."
tv_script_url: "https://www.tradingview.com/script/V27gem2X-TTP-IMB-Unfilled-Imbalances/"
---
Let me be straight with you: there's no shortage of imbalance indicators on TradingView. Most of them just draw a few boxes and call it a day. Ttp_Imb_Unfilled_Imbalances is different — it specifically tracks *unfilled* imbalances, which is a subtle but crucial distinction that most retail traders miss.

### What This Indicator Actually Does

The core premise comes from ICT/SMC concepts: when price moves aggressively, it leaves behind an imbalance (a one-way price range where few trades occurred). These zones act like magnets — price often returns to "fill" them before continuing the trend. The twist here is that this indicator filters out already-filled imbalances and only displays the ones still lurking in the market.

What you get on your chart is a series of boxes (or shaded zones, depending on your settings) marking these unfilled areas. As the chart above shows, the indicator plots these zones in relation to price action, and you can see how price often respects them on pullbacks.

### Key Features That Set It Apart

The unfilled-only filter is the headline feature. Most imbalance tools clutter your chart with every historical imbalance, making it nearly impossible to spot the relevant ones. This one keeps things clean.

Another strong point: the indicator tracks imbalances across multiple timeframes. You can load the daily imbalances on your 15-minute chart and see where the bigger players are likely to step in. That multi-timeframe awareness is genuinely useful for aligning your intraday bias with higher timeframe structure.

The alert system is solid, too. You can set alerts for when price enters an imbalance zone, which saves you from staring at the chart all day.

### Best Settings (Tested)

I ran this on BTCUSD and EURUSD across multiple sessions. Here's what worked:

- **Lookback period:** 200 bars is a good default. Going longer than that just fills your chart with stale zones that rarely get revisited.
- **Minimum imbalance strength:** I'd set this to 2–3. Anything lower gives you too many false signals, and anything higher becomes too restrictive.
- **Display mode:** The "boxes" mode is easier to visualize than the "lines" mode. You want to see the full zone, not just the edge.
- **Timeframe:** For day trading, use the 15-minute chart with the 4H and Daily imbalances loaded. For swing trading, use the 4H chart with Daily and Weekly.

### How to Use It: Entry and Exit Logic

The most reliable setup I found was the *imbalance sweep*:

1. Wait for price to enter an unfilled imbalance zone.
2. Look for a candlestick rejection pattern (pin bar, engulfing) at that level.
3. Enter on the close of the rejection candle.
4. Set your stop loss just beyond the imbalance zone's edge.
5. Take profit at the next major structural level or at the opposite side of the range.

For trend trading, the indicator works best when you combine it with a basic trend filter — a 200 EMA or a simple higher-high/lower-low structure check. Only take long entries when the higher timeframe imbalance is below price and acting as support, not resistance.

### Pros & Cons

**Pros:**
- The unfilled filter genuinely reduces chart clutter.
- Multi-timeframe capability is well implemented.
- Alerts are practical and easy to set up.
- Clean, honest visual presentation — no misleading signals.

**Cons:**
- Like all imbalance tools, it's *reactive*, not predictive. It tells you where price *might* react, not where it *will*.
- The boxes can lag slightly on fast-moving markets.
- No backtesting engine built-in, so you'll need to do that manually or with another tool.
- On lower timeframes (1m–5m), the zones can be noisy unless you adjust the minimum strength setting.

### Who It's For

This is for traders who already understand order flow and market structure concepts. If you're new to the idea of imbalances and fair value gaps, you might find the zones confusing without additional context. But if you've been trading supply/demand or ICT-style concepts, this tool will fit right into your workflow.

It's particularly strong for:
- Intraday traders who want to align with higher timeframe structure
- Swing traders who want to know where price is likely to pause or reverse
- Traders who are tired of clutter-heavy imbalance indicators

### Alternatives Worth Considering

If this doesn't quite fit your style:
- **Smart Money Concepts by LuxAlgo** — more comprehensive if you want the full ICT toolkit (order blocks, FVGs, liquidity zones) in one package.
- **Fair Value Gaps by LonesomeTheBlue** — simpler and lighter if you just want the basic FVG without the unfilled filter complexity.
- **Volume Imbalance by TradingView (built-in)** — good enough for quick analysis if you don't want to pay for an external indicator.

### FAQ

**Does this indicator repaint?**
No, the zones are drawn based on historical data and don't change once formed. The unfilled status only updates when price actually fills the zone.

**Can I use it for crypto?**
Yes, I tested it on BTC and ETH. It works well on crypto's 24/7 markets, though you'll want to use the 4H and Daily imbalances rather than lower timeframes for swing setups.

**Is it good for scalping?**
Not really. The unfilled zones are too wide on lower timeframes, and you'll get too many signals. It's better suited for intraday and swing trading.

### Final Verdict: ⭐⭐⭐⭐ (4/5)

Ttp_Imb_Unfilled_Imbalances earns its four stars because it solves a real problem — filtering out the noise of filled imbalances — without overcomplicating things. It's not a magic bullet (no indicator is), but it gives you a clear map of where institutional money is likely waiting. The multi-timeframe support and clean alerts make it genuinely useful for daily trading.

I'm docking one star because it lacks a built-in backtester and can feel slightly redundant if you already have a comprehensive SMC suite. But if you're looking for a dedicated unfilled imbalance tool that's precise and doesn't clutter your chart, this is one of the better options I've tested.

**Rating: ⭐⭐⭐⭐ (4/5) — Recommended with confidence.**
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
