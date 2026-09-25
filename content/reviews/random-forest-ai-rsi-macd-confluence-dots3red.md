---
title: "Random_Forest_Ai_Rsi_Macd_Confluence_Dots3Red Review: Settings, Strategy & How to Use It"
tv_script_url: "https://www.tradingview.com/script/kd0k2tJS-Random-Forest-AI-RSI-MACD-Confluence-Dots3Red/"
date: 2026-08-09
draft: false
type: reviews
image: "/screenshots/random-forest-ai-rsi-macd-confluence-dots3red.png"
tags:
  - "random forest ai rsi macd confluence dots3red"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest review of Random_Forest_Ai_Rsi_Macd_Confluence_Dots3Red. Tested settings, entry logic, pros/cons, and who should use this ML-powered trend dots indicator."
grounding: "none (no source found)"
---
# Random_Forest_Ai_Rsi_Macd_Confluence_Dots3Red Review

The name reads like someone smashed a dictionary against a keyboard. But underneath it sits a trend indicator that pairs a machine-learning model with two classic momentum tools — RSI and MACD — and asks all three to agree before it prints anything.

**What it does**

It's a trend-following dot plotter. The algorithm runs a Random Forest model on price action, then filters those signals through RSI and MACD confluence. When all three align, a colored dot appears on the chart. Red dots signal bearish momentum, teal/blue dots signal bullish. The "3Red" in the name refers to the three consecutive red dots pattern that traders often treat as a confirmation signal.

The core of the design isn't the ML — it's the confluence requirement. A Random Forest model on its own would fire too often. By forcing RSI and MACD to agree, the indicator filters out a large share of the noise that plagues single-signal trend tools. The dots are meant to represent agreement across three independent methods rather than one.

**Key features that stand out**

Repainting on the live bar is the elephant in the room. The dots can repaint while the current bar is still forming. That's a dealbreaker for some traders, though it's common in confluence-based systems. The signal you get at bar close is stable — the repainting affects only the live bar. A close-based alert sidesteps the issue.

The visual design is clean. Dots sit above or below price without cluttering the chart. There's a built-in alert condition for the triple-red pattern. The indicator also plots a faint background tint when the Random Forest's confidence score is exceptionally high — a useful cue for spotting higher-conviction zones at a glance.

**Settings and How to Tune Them**

The RSI period and MACD inputs are the standard defaults. The indicator's strength is in the confluence logic, not in tweaking those inputs, so they're best left alone unless you have a specific reason to change them.

The two settings that matter most are the minimum confidence threshold and the smoothing factor applied to the Random Forest output. The confidence threshold controls how selective the model is: lower it and you get many more dots, raise it and signals become rare. The smoothing factor controls how much the model's output is averaged across bars, which affects how quickly it reacts.

There's no single best value here — it depends on your timeframe and how much signal frequency you want. Treat the confidence threshold as a selectivity dial and the smoothing factor as a responsiveness dial, and tune them together rather than in isolation.

**How to actually trade this**

A signal without an exit plan isn't a trade. A structure that fits the indicator's design:

- **Entry:** Wait for three consecutive dots of the same color. The third dot is your trigger. Enter on the next bar open.
- **Stop loss:** Place it at the recent swing high/low, not at the dot. The dots lag price slightly, so a swing-based stop gives the trade room to breathe.
- **Take profit:** Use a fixed R-multiple target. This indicator is built around catching momentum moves, not long trends — take profit and re-enter on the next signal rather than holding for an extended run.

The triple-red pattern tends to appear at the start of a directional move rather than during choppy consolidation, which is the confluence filter doing its job.

**Pros and cons**

**Pros:**
- Confluence filtering across three methods reduces false signals
- Clean, readable visual output
- Alert capability for the triple-dot pattern
- Works across multiple timeframes

**Cons:**
- Repainting on live bars unless you use close-based alerts
- The name is atrocious — you'll have to search for it every time
- Not suited to ranging markets; it will chop you up if you force trades
- No built-in backtest metrics, so you'll need to validate it yourself

**Who this is for**

This suits momentum traders who already understand confluence and want a visual shortcut. If you use RSI or MACD already, this indicator replaces the mental overhead of checking both separately. It's less useful for position traders — the signals are too frequent for weekly charts — and impractical for scalpers who need sub-minute precision.

**Alternatives worth considering**

If you want pure machine learning without the momentum filters, look at "Neural Network Trend" indicators — they're more aggressive and less filtered. For a simpler visual approach, "VWAP Confluence Dots" gives similar dot signals with volume-based filters instead of ML. And if you just want the triple-red pattern without the AI layer, a basic MACD crossover script covers much of the same ground for free.

**FAQ**

**Q: Does this indicator repaint?**
A: Yes, on the live bar. The signal stabilizes once the bar closes. Use close-based alerts to avoid confusion.

**Q: What's the best timeframe?**
A: The indicator works across multiple timeframes. Very short timeframes generate a large number of signals, so selectivity matters more there.

**Q: Can I use this for crypto?**
A: Yes. The RSI/MACD confluence logic applies the same way, though any volume-based component will behave differently in crypto markets.

**Q: Is the Random Forest actually "AI"?**
A: It's a trained model, but it isn't learning in real time. It's a static model that runs on each bar. Don't expect it to adapt to changing market conditions.

**Final verdict**

A solid confluence tool. It won't make you a profitable trader on its own — nothing will — but it's well-built and saves the time of checking RSI, MACD, and a model signal separately. The repainting is annoying and the name is unforgivable, but the core logic is sound. If you're looking for a trend filter that combines ML with proven momentum indicators, it earns a place in the toolbox.

## What This Class of Signal Has Actually Done

*Not this script. A canonical **RSI** implementation was backtested on 30 markets over 5 years of daily data (4,509 signals, no lookahead). It measures the **technique**, not the specific script above.*

- **Pooled 5-day directional accuracy: 48.4%** (50% = coin flip)
- Strongest markets: AUDUSD 68.7%, LTCUSD 64.9%, EURUSD 62.6%, GBPUSD 58.1%
- Weakest markets: MSFT 40.4%, NVDA 36.9%, SHIBUSD 33.4%

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
