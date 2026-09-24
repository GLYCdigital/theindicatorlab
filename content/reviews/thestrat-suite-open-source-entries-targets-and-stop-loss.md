---
title: "Thestrat_Suite_Open_Source_Entries_Targets_And_Stop_Loss Review: Settings, Strategy & How to Use It"
date: 2026-08-10
draft: false
type: reviews
image: "/screenshots/thestrat-suite-open-source-entries-targets-and-stop-loss.png"
tags:
  - "thestrat suite open source entries targets and stop loss"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest Thestrat Suite review: backtested entries, targets, and stop-loss logic. Settings, pros/cons, and whether it beats manual Strat analysis."
grounding: "none (no source found)"
---
# Thestrat_Suite Review: A Full Implementation of The Strat

This is not another repackaged MACD crossover with a fancy name. Thestrat_Suite is a full implementation of Rob Smith's "The Strat" methodology — the 2/9 EMA ribbon, the 1-2-3-4-5-6 candlestick sequences, and the CDL patterns that Strat traders focus on. As an open-source tool on TradingView, it is one of the more complete Strat implementations available.

## What This Indicator Actually Does

The Strat is a systematic approach to reading price action through consecutive candle sequences and EMA relationships. This suite automates three things: it plots the 2 and 9 EMAs, counts the candle sequences (calling out "1-2-3" or "1-2-3-4-5-6" setups), and generates entry arrows with attached target and stop-loss levels. The open-source nature means the logic is fully visible — no black-box mystery.

The target/stop system is notable. It is not the usual fixed ATR multiplier. The indicator calculates targets based on the sequence length and the distance from the 2 EMA, which aligns with how Strat traders actually think about trade management.

## The Chart Logic

The indicator does two things well. First, it marks entry zones with price labels and horizontal lines for targets — T1, T2, and T3 levels are plotted in advance. Second, the stop-loss placement is structurally sensible: it sits just below the sequence's starting candle, not at some arbitrary percentage that gets you stopped out on noise.

The sequence signals can also be read alongside momentum tools such as the MACD histogram. Confluence between the two is worth watching, though it is not perfect — nothing is. Signals that align with both the Strat setup and momentum direction tend to be the cleaner ones.

## Settings and How to Tune Them

- **Timeframe**: The methodology reads more cleanly on higher timeframes. On lower timeframes, the sequence counting gets noisy.
- **EMA Length**: The default 2 and 9 are part of the methodology itself.
- **Target Count**: Two targets is a reasonable default. A third target often does not get filled unless the session is a strong trend day.
- **Sequence Filter**: A "minimum sequence length" filter exists to cut out weak 1-2 setups that fail more often. Raise it to filter more aggressively.
- **Stop Loss Mode**: The "sequence low/high" option aligns with actual structure. The ATR-based option does not.

## How to Actually Trade It

The entry logic is straightforward: wait for a 1-2-3-4-5-6 sequence in the direction of the 2 EMA slope, then enter on the next candle's open. The indicator marks this with an arrow. Don't chase — if price has already moved two candles past the signal, skip it.

For exits, a common approach is taking partial profits at T1 and letting the rest run to T2 with a trailing stop at the 9 EMA. The stop loss stays at the sequence low until T1 hits, then moves to breakeven. This is a structural way to use the tool rather than an arbitrary one.

## Pros & Cons

**Pros:**
- Fully open-source — every line of logic is verifiable
- Targets and stops are dynamically calculated from structure, not arbitrary
- The sequence labels are clear and don't clutter the chart
- No repainting on confirmed candles (the signal appears on candle close)

**Cons:**
- The indicator does NOT work well in ranging markets. It will generate signals that fail consistently.
- No alert system built-in for the entries — alerts must be set manually
- The 2 EMA is extremely sensitive on lower timeframes, generating false sequence breaks
- No backtesting panel — that has to be done externally

## Who This Is For

This is for traders who already understand The Strat or are willing to learn it. If you're looking for a "set and forget" autopilot, this isn't it — it's a tool that automates the heavy lifting but still requires discretionary judgment. If you've been manually counting sequences and drawing levels, this will save time.

## Alternatives Worth Considering

- **StratAlerts**: More polished alert system but paid and closed-source
- **Nadaraya-Watson Envelope**: Better for mean reversion if that's your style
- **LuxAlgo Premium Suite**: More comprehensive but overkill if you just want Strat signals

## FAQ

**Q: Does this repaint?**
A: No, on confirmed candles. Signals appear at candle close and don't disappear.

**Q: Can I use it for crypto and forex?**
A: Yes, but adjust the sequence filter. Crypto tends to need a higher sequence minimum; forex works with a lower one.

**Q: Is the stop loss calculation reliable?**
A: It is based on the actual sequence structure, not a random ATR multiplier.

## Final Verdict

Thestrat_Suite is a solid tool. It does exactly what it promises — automates Strat analysis with legitimate targets and stops — and does it transparently. It's not going to make you a profitable trader overnight, but if you understand the methodology, it's a genuine time-saver. The lack of alerts and poor ranging-market performance hold it back. For the price (free, open source), it's one of the better Strat implementations on TradingView.

If you're already trading The Strat manually, this is a straightforward install. If you're new to it, start with the daily chart and paper trade before risking capital.

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
