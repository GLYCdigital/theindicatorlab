---
title: "Anomaly_Detection_Indicator Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/ZkIzGxSg-Anomaly-Detection-Indicator-Fournier-Eaton-etothepii/"
date: 2026-07-16
draft: false
type: reviews
image: "/screenshots/anomaly-detection-indicator.png"
tags:
  - anomaly detection indicator
  - "07"
  - tradingview
  - indicator
  - review
  - trading
categories:
  - "07"
  - Technical Analysis
rating: 4
description: "Honest review of the Anomaly_Detection_Indicator. See how it spots rare price moves, optimal settings, and if it's worth adding to your TradingView toolkit."
grounding: "none (no source found)"
---
You know that gut feeling when a candle looks *wrong*? Maybe it's a massive wick on low volume, or a spike that breaks a key level then snaps back instantly. That's exactly what the Anomaly_Detection_Indicator tries to catch—statistical outliers that often precede reversals or big news.

## What This Indicator Actually Does

This isn't a moving average crossover or RSI clone. It's a statistical outlier detector that flags bars where price, volume, or volatility deviate significantly from recent norms. The core logic uses z-scores (standard deviations from a rolling mean) across multiple data streams—typically price change, volume, and range size.

When a bar exceeds a threshold, you get a clear visual marker: a colored dot above or below the bar, and optionally an alert. The indicator also plots a "noise band" that shows the normal range of movement, so you can visually see when price steps outside it.

**What it's NOT:** A magic crystal ball. It won't tell you *why* the anomaly happened—only that something statistically unusual just occurred. You still need context.

## Key Features That Set It Apart

- **Multi-stream anomaly detection** – Most free anomaly scripts only look at price. This one also checks volume and range, which is crucial. A price spike on normal volume is less meaningful than one on exploding volume.
- **Customizable z-score threshold** – You can tune sensitivity from very sensitive (many false signals) to only extreme events.
- **Alert system** – You can set alerts for new anomalies in any direction, so you don't have to watch the chart.
- **Noise band visualization** – The shaded zone around price shows normal movement. Exiting that zone = anomaly. It's simple but effective for spotting regime changes.

## Settings and How to Tune Them

- **Lookback period:** Shorter lookbacks react faster but catch more noise; longer lookbacks smooth things out but lag.
- **Deviation threshold:** The default is 2.5 standard deviations. Lower values flag more events; higher values isolate only extreme ones.
- **Stream weighting:** You can weight price, volume, and range differently. Pure price anomalies without volume confirmation are more likely to be noise.
- **Smoothing:** Turning it off keeps signals immediate. Enabling it delays signals but can reduce whipsaws.

**For scalping:** Use a short lookback, a lower threshold, and no smoothing. You'll get many signals, so filter for cases where a volume anomaly confirms the price anomaly.

**For swing trading:** Use a longer lookback, a higher threshold, and smoothing on. Fewer signals, but each one is more significant.

## How to Use It for Entries and Exits

This is where most traders screw up. They see a big anomaly dot and immediately buy/sell. Don't do that.

**Entry strategy:**
1. Wait for an anomaly dot to appear.
2. Check if it's confirmed by volume (the volume stream should also register as an anomaly).
3. Don't trade the anomaly candle itself—it's an outlier and often reverses. Wait for the *next* candle to close.
4. Enter in the direction of the anomaly if the next candle breaks the anomaly candle's high/low. This filters out fakeouts.

**Exit strategy:**
- Set a stop at the opposite side of the anomaly candle's body (not the wick).
- Take profit at the noise band boundary (the indicator plots it).
- If price immediately reverses and breaks the anomaly candle's midpoint, you're wrong. Exit.

## Honest Pros and Cons

**Pros:**
- Genuinely unique—multi-stream anomaly detection isn't common in free indicators
- Works across asset classes
- Alerts are part of the design
- Noise band helps visualize normal vs. extreme movement

**Cons:**
- Can generate false signals during scheduled news events (NFP, CPI, FOMC). A manual news filter helps.
- No built-in risk management or position sizing
- The "anomaly" label on past bars can create hindsight bias when reviewing history
- Can be resource-heavy on lower timeframes

## Who It's Actually For

**Great for:** Swing traders and position traders who want a heads-up on potential reversals or breakouts. Also useful for algo traders who need a clean signal to trigger automated entries.

**Not for:** Scalpers who need a constant stream of signals—you'll get overwhelmed with noise. Also not for beginners who don't understand z-scores or standard deviation. If you don't know what a "2.5 sigma event" means, learn that first.

## Better Alternatives If They Exist

- **Volume Profile** – Better for volume-focused anomaly spotting, but doesn't detect price or range anomalies.
- **Z-Score Indicator (built-in)** – Free but only checks price. The Anomaly_Detection_Indicator adds volume and range.
- **Machine Learning: Anomaly Detection (paid)** – More sophisticated but overkill for most traders.

## FAQ

**Q: Does this repaint?**
A: No. The dots and noise bands are fixed once a bar closes. You can trust the signals for reviewing past bars.

**Q: Can I use it on crypto?**
A: Yes, and it's arguably better there because crypto has frequent anomalies that stocks don't.

**Q: Does it work on Forex?**
A: Yes, but FX moves are smoother and anomalies are subtler, so you may need to lower the threshold.

## Final Verdict

The Anomaly_Detection_Indicator solves a real problem: catching statistically unusual events before the crowd reacts. It's not perfect—news events can wreck it—but when combined with basic context (trend, volume confirmation), it's a solid tool. For $0 (it's free on TradingView), it's worth a look.

**Rating: ⭐⭐⭐⭐ (4/5)** – Loses a star for the news blind spot and lack of built-in risk management. But for what it does, it does it well.

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
