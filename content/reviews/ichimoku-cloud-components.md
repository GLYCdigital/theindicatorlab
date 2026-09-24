---
title: "Ichimoku_Cloud_Components Review: Settings, Strategy & How to Use It"
date: 2026-07-28
draft: false
type: reviews
image: "/screenshots/ichimoku-cloud-components.png"
tags:
  - "ichimoku cloud components"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest review of Ichimoku_Cloud_Components. Breaks down Senkou, Kijun, Tenkan, Chikou Spans. Best settings, entry logic, and who should skip it."
grounding: "none (no source found)"
---
# Ichimoku_Cloud_Components Review

Most Ichimoku variants on TradingView either clutter the chart with unnecessary lines or strip out essential components. **Ichimoku_Cloud_Components** sits somewhere in the middle—it's not revolutionary, but it does one thing well: it gives you clean, individual control over each Ichimoku element without the visual noise of a full cloud.

## What It Does

The indicator plots the five core Ichimoku lines—Tenkan-sen (conversion), Kijun-sen (base), Senkou Span A & B (leading spans), and Chikou Span (lagging)—but lets you toggle each on/off independently. You can also adjust the periods and shift values. The default settings match the classic (9, 26, 52) parameters, but you can tweak them. The indicator overlays directly on price, with the cloud shaded between Senkou A and B.

## Key Features

- **Modular toggles** – Need only Kijun-sen and the cloud? Done. No need to hide extras manually.
- **Customizable periods** – Unlike many canned Ichimoku scripts, you can change the Tenkan, Kijun, and Senkou B lookback periods. This makes it adaptable to different timeframes and trading styles.
- **Displacement control** – You can shift Senkou Span A/B forward (default 26) or backward. Useful if you want to align the cloud with price action on non-standard timeframes.
- **Clean labels** – Each line is labeled with its name, which helps beginners distinguish between them quickly.

## Settings and How to Tune Them

- **Periods** – The classic (9, 26, 52) parameters are the defaults. Longer lookbacks smooth the lines and reduce the frequency of cloud twists; shorter lookbacks make the components more responsive to recent price.
- **Chikou Span** – This line lags price by the Kijun period. On lower timeframes that lag is proportionally large relative to the trading session, which makes it less useful for intraday reads. On daily charts it can help identify support/resistance breaks.
- **Cloud shift** – The default displacement is +26. Adjusting it changes where the cloud sits relative to current price, which matters if you're trading instruments with different session or settlement conventions.
- **Cloud visibility** – Both Senkou Span A and B must be enabled for the cloud to render. If the cloud is missing, check the toggles first.

## How to Use It

This isn't a standalone strategy—it's a component builder. Best paired with price action.

- **Long entry** when price is above the cloud, Tenkan-sen crosses above Kijun-sen (TK cross), and the cloud is green (Senkou A > Senkou B).
- **Short entry** when price is below the cloud, TK cross below, and cloud is red.
- **Exit** when price closes inside the cloud or when Chikou Span breaks its prior swing high/low.
- **Filter** – Only take trades when the cloud is flat or expanding. A thinning cloud (narrowing gap) means weak trend—avoid.

## Pros & Cons

**Pros:**
- Extremely lightweight.
- Full control over each component.
- Labels reduce confusion for new Ichimoku users.
- Works on any timeframe with adjusted periods.

**Cons:**
- No built-in alerts for crosses or cloud flips (you'll need to set your own price alerts).
- Doesn't include standard Ichimoku support/resistance levels (like Kumo breakout zones).
- The cloud shading is basic—no gradient or opacity options (minor visual nitpick).
- If you're an Ichimoku purist, you might miss the full cloud thickness calculation.

## Who It's For

- **Intermediate to advanced traders** who already understand Ichimoku and want to fine-tune components.
- **Swing traders on daily and 4H charts** – the classic periods work well here.
- **Traders who hate clutter** – you can strip down to just Tenkan and Kijun for a simple moving average crossover system.

## Who Should Skip It

- Beginners who need an all-in-one Ichimoku indicator with alerts, cloud thickness, and automatic signals.
- Scalpers – the lag on Chikou Span and cloud shift is too slow for 1-minute charts.

## Alternatives

- **Ichimoku Kinko Hyo (built-in)** – If you want the full cloud with standard settings and don't need customization, stick with the native TradingView version.
- **Ichimoku Cloud with Alerts** by LuxAlgo – Adds push notifications for TK crosses and cloud breaks. Better for active traders.
- **Cloud Trader Pro** – More advanced, includes volume-weighted cloud and adaptive periods. Overkill for most.

## FAQ

**Q: Does this indicator repaint?**
A: No. All Ichimoku components are based on fixed historical data. Senkou Spans shift forward, but they don't change once plotted.

**Q: Can I use this for crypto?**
A: Yes. The adjustable periods let you adapt the components to more volatile assets.

**Q: Why is my cloud not showing?**
A: Check that both Senkou A and B are enabled. Also ensure your chart has enough historical bars—Ichimoku needs data going back at least 52 bars.

## Final Verdict

It's not flashy, but it's reliable. If you already know how to read Ichimoku and just want a clean, customizable version of the cloud components, this indicator delivers exactly that. The lack of alerts and advanced features holds it back, but for a no-frills component tool, it's a solid choice. Strip it down to what you need and pair it with price action—you'll get consistent trend reads without the noise.

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
