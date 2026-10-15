---
title: "Ichimoku Cloud Axealgo Review — Trend Indicator"
date: 2026-10-16
draft: false
type: reviews
image: "/screenshots/ichimoku-cloud-axealgo.png"
tags:
  - "ichimoku cloud axealgo"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Ichimoku Cloud Axealgo review: a full Ichimoku Kinko Hyo workspace with scored cloud breakouts, Hosoda wave/price/time theory and a plain-language panel."
tv_script_url: "https://www.tradingview.com/script/rxiQ9dvR-Ichimoku-Cloud-Pro-AxeAlgo/"
sources: ["https://www.tradingview.com/script/rxiQ9dvR-Ichimoku-Cloud-Pro-AxeAlgo/"]
---
Most "Ichimoku" scripts on TradingView are five lines and a coloured cloud. Ichimoku Cloud Axealgo is not that. It's an attempt to build the entire Kinko Hyo framework — the five lines, Hosoda's three theories, higher-timeframe context, and a signal checklist — into a single workspace that explains itself in plain language.

That ambition is exactly why it's worth a careful look, and also why you need to read the limitations before you install it.

## What it actually does

The foundation is the classic five lines, but a lot of the value is in the cloud *ahead*. Senkou Span A and B are calculated before they're drawn, so the future cloud is already known. The script marks the candle where Span A crosses Span B — the moment the cloud turns — and the panel counts the bars until the drawn cloud flips colour. If you've ever wished you could see the twist coming rather than react to it, that's the pitch.

On top of that sits the Hosoda layer: wave theory (each confirmed swing labelled I, V, N, P, Y or W), price theory (V, N, E, NT, 2E and 3E targets projected once a pullback C confirms), and time theory (future windows from Hosoda's basic numbers, plus Taito Sūchi). Where two or more time counts agree, you get a gold window. Where a gold window meets an open price target, you get a kasanari box.

Then there's the signal layer: cloud breakouts scored 0–100 against a transparent checklist, perfect alignment (Kanzen), and optional marks for Kijun bounces, Tenkan/Kijun crosses, flat Span B levels and Chikou "open air."

## The breakout score is the interesting part

Instead of a binary "breakout happened" alert, each close-through-the-whole-cloud event gets scored on a checklist: cloud thickness crossed, Chikou clear, Tenkan/Kijun alignment, close-through margin, higher-timeframe agreement, relative volume and RSI, with a chop filter applied. Above your chosen minimum score, you get a badge — hover it for the full breakdown. "CT" flags a breakout against every higher timeframe, "CH" one in choppy conditions.

The honest framing matters here: the author explicitly says the score is **a checklist of classic Ichimoku confirmations, not a probability.** That's a rare and welcome admission.

## How you'd actually use it

Read the panel first. Bias and Cloud rows tell you which side the structure favours, whether the two higher timeframes agree, and whether the cloud is about to turn. From there, treat breakout badges, Kanzen, Hosoda targets and time windows as *structure to plan around* — bias, levels, timing — and combine them with your own entry, risk and exit rules.

Alerts are handled sensibly: tick the events you want and create one "Any alert() function call" alert to catch them all, with score, price and targets in the message.

## Pros and cons

**Pros**
- Genuinely complete Ichimoku workspace — cloud projection, Hosoda theories, HTF context and signals in one script.
- Signals are decided at bar close and don't repaint.
- The breakout score is transparent and hoverable, not a black box.
- Plain-language panel with Simple and Detailed modes.
- The chart key explains every mark, which most multi-feature scripts never bother with.
- Settings are well organised, with everyday options first and fine-tuning tucked into Advanced sections.
- Alerts are flexible and well thought out.

**Cons**
- It's dense. Nine optional mark types, three theory modules and two panel modes is a lot to absorb.
- The author's own checks found no proven edge: breakouts, Kijun bounces and Kanzen each reached +1 ATR before −1 ATR about half the time, and higher-scoring breakouts were only marginally better on too few cases to rely on. Hosoda targets and time windows didn't beat chance either.
- Swings confirm a set number of bars after they form, and a more extreme same-kind swing can replace the last one.
- Higher-timeframe values only update when that bar closes.
- Ichimoku itself struggles in ranges, and the script says so.

## Who it's for

Discretionary traders who already understand Ichimoku and want the full framework — cloud projection, Hosoda theory, HTF agreement — in one place without building it themselves. It suits people who treat signals as *context* rather than entries. It's designed for liquid markets like gold, forex, indices and crypto on intraday to daily charts, and works on any symbol and timeframe.

It is **not** for anyone hunting a mechanical system. If you want an indicator that tells you when to buy, this isn't it, and the author says as much.

## FAQ

**Does it repaint?** No. Every signal is decided at bar close. Projections ahead of price (Hosoda target lines, time windows) update as new swings confirm.

**Is the breakout score a win rate?** No. It's a weighted checklist of classic Ichimoku confirmations. The author states it is not a probability.

**Can I use it on crypto?** Yes — there's a Crypto 24/7 line-length preset, and the design targets liquid markets including crypto.

**Are the cloud colour-change dots reliable?** They're filtered by minimum spacing and a minimum speed of Span A/B convergence, so small back-and-forth crosses in flat markets aren't marked.

**What happens to old price targets?** Open targets expire after 500 bars.

## Verdict

This is one of the more complete and more *honest* Ichimoku tools you'll find. It does real work — future cloud projection, scored breakouts, Hosoda's theories, HTF context — and it tells you plainly that none of it constitutes an edge. That transparency is worth more than a flashy win-rate claim.

The four stars reflect that: excellent execution and scope, with the caveat that the underlying signals are classical reference points, not forecasts. Install it as a charting and planning workspace, not as a system.

**Rating: ⭐⭐⭐⭐ (4/5)**
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
