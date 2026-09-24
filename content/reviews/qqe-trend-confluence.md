---
title: "Qqe_Trend_Confluence Review: Settings, Strategy & How to Use It"
date: 2026-08-31
draft: false
type: reviews
image: "/screenshots/qqe-trend-confluence.png"
tags:
  - "qqe trend confluence"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Qqe_Trend_Confluence combines QQE signals with trend filters. Tested settings, entry logic, pros/cons, and who should use it."
tv_script_url: "https://www.tradingview.com/script/Yg0CNk0R-QQE-Trend-Confluence-MarkitTick/"
sources: ["https://www.tradingview.com/script/Yg0CNk0R-QQE-Trend-Confluence-MarkitTick/"]
---
# Qqe_Trend_Confluence Review

Most QQE variations on TradingView are repackaged versions of the same oscillator with a fresh coat of paint. The question with any new one is whether it adds something structural or just re-skins the same math. Qqe_Trend_Confluence is a dual-engine QQE confluence oscillator, and its architecture is worth understanding before you load it.

## What This Indicator Actually Does

At its core, the script runs the classic QQE concept: an RSI reading smoothed with an EMA, with the average magnitude of bar-to-bar changes in that smoothed RSI used to build a ratcheting trailing envelope around the smoothed RSI line. A cross of the smoothed RSI over or under that trailing level marks a momentum shift.

What separates this script from a stock QQE is that it restructures the calculation into a layered decision pipeline. A raw crossover is only the first step — a signal must pass through several independent, user-toggleable filters before it qualifies. The source price can be routed through a selectable pre-smoothing stage, a second independently parameterized QQE pair runs in parallel as a confirmation gate, and an ADX/DMI strength filter plus a non-repainting higher-timeframe bias filter can each veto a signal. The publisher's stated intent is deliberate: the pre-smoothing stage shapes what "signal" means, the dual-QQE and filter stack decides which signals are trustworthy, and the trade planner and alert system decide what to do once a signal is accepted.

## Key Features That Actually Matter

**Adaptive pre-smoothing engine.** Before price reaches the QQE math, it can optionally be passed through one of eight smoothing or prediction methods selected from a dropdown. These include standard Simple, Exponential and Wilder (RMA) moving averages; a double weighted moving average that applies a WMA to the result of a first WMA pass; a triple volume-weighted moving average that chains three successive VWMA passes; a Hull Moving Average using Alan Hull's weighted-difference technique; a proprietary LLAMA method; and a Kalman Filter option.

The LLAMA method computes an SMA baseline over the lookback window, measures the linear slope of price across that same window (the difference between the current source and the value from "length" bars back, divided by length), projects that slope forward by half the lookback length, and adds it to the SMA baseline. The practical effect is a moving average that leans ahead of price during a steady trend and collapses back toward a standard SMA when price is flat.

The Kalman Filter option treats price as a noisy observation of an unobserved underlying trend state, maintains an internal estimate and error variance, computes a Kalman gain each bar from a length-derived process-noise assumption and a fixed measurement-noise assumption, and blends the new observation into the estimate proportionally to that gain — producing a curve that adapts its own responsiveness over time.

**Dual QQE core.** Two QQE instances run simultaneously: a faster primary pair that generates the raw crossover, and an optional slower secondary pair whose sole purpose is confirmation. A signal from the primary pair is only accepted if the secondary pair's RSI-to-trail relationship already agrees with the same direction.

**Confirmation filters.** An optional ADX/DMI filter built on Wilder's Average Directional Index requires trend strength to be above a user-defined threshold before a signal is allowed through. An optional higher-timeframe bias filter pulls the same smoothed-RSI-versus-trailing-level relationship from a user-selected higher timeframe and requires it to agree with the current-timeframe signal. That request is built using the previous, already-confirmed value on the higher timeframe combined with lookahead-on merging — the standard non-repainting pattern for higher-timeframe data, where the value shown on any historical bar is the same value that would have been available in real time.

**ATR-based trade planner.** Once a signal clears every enabled filter, the script computes a stop-loss using the 14-period Average True Range multiplied by a user-defined multiple, anchored to the prior bar's close. Three take-profit levels are derived from that risk distance using independently configurable risk:reward ratios. These are drawn as extending price lines with labels and shaded risk/reward zone fills, and the script checks bar by bar whether price has touched each target or the stop, retiring the plan once the final target or the stop is hit. A lock control can freeze the displayed plan so it isn't replaced by a new signal while a trade is managed.

**Signal confirmation behavior.** The crossover state driving every signal is always evaluated using the prior, already-completed bar's smoothed RSI and trailing-level relationship rather than the still-forming current bar. A BULL or BEAR marker only prints once the underlying cross is confirmed, and it does not shift position or disappear on subsequent price updates within the same bar.

**Automation-ready alerts.** Every entry, exit, and trade-management event — long entry, short entry, close-long, close-short, and each of the three take-profit levels plus stop-loss — is wrapped in its own alert condition and also emits a structured JSON message through a single dynamic alert call, gated to fire only once per confirmed bar close for entries. Each payload includes the instrument, timeframe, and an editable action keyword.

## Visual Guide

In the indicator's own pane, the blue RSI MA line is the primary smoothed-RSI reading, the yellow Smoothed Trail line is its dynamic trailing envelope, and the histogram plotted around the zero line reflects the distance between the two — teal on the bullish side, red on the bearish side. Dashed reference lines at 70 and 30 mark overbought and oversold zones with a light shaded fill between each level and the 50 midline when enabled.

On the price chart, candles can be recolored using a four-tone scheme — strong bullish teal and weak bullish dark teal, or strong bearish red and weak bearish dark red — with neutral gray used whenever the current QQE distance is smaller than its own running average, giving an at-a-glance read on momentum strength as well as direction. BULL and BEAR labeled arrows print just below or above the triggering candle when a fully confirmed signal fires. When trade levels are enabled, dashed lines and small labels for the stop-loss, entry, and three take-profit levels extend to the right from the signal bar, with the risk zone shaded between entry and stop and the reward zone between entry and the furthest target.

An optional multi-row dashboard, placeable in any chart corner, summarizes the instrument and timeframe, lock status, current bias, the raw RSI MA and Trail Level values, an ASCII progress-bar style RSI strength meter, the secondary confluence state, the higher-timeframe bias, the ADX reading and pass/fail color, the active pre-smoothing method, the ATR value, the DI+/DI- readings, a momentum strength bar, and the active trade's direction and price levels.

## Settings and How to Tune Them

**Core Settings.** RSI Length and RSI EMA Smoothing control the primary QQE's momentum lookback and responsiveness. QQE Factor scales how wide the trailing envelope sits from the smoothed RSI. Source selects the price series feeding the whole calculation. The secondary QQE toggle, along with its own EMA smoothing and factor, controls the confirmation pair.

**Filters.** The ADX toggle, length, and threshold control the trend-strength gate. The Adaptive Filter dropdown and length select which of the eight pre-smoothing methods — including LLAMA and the Kalman Filter — is applied to price before the QQE math runs. The HTF filter toggle and timeframe control the higher-timeframe bias confirmation.

**Trade Tools.** Toggles for showing trade levels and locking the current signal, an ATR multiple for stop-loss distance, and three independent risk:reward ratios for the three take-profit targets. Adjust the ATR stop multiple and the three risk:reward ratios to match your own risk tolerance before relying on the drawn levels.

**Visuals.** Independent toggles for the overbought/oversold zone fill, the histogram, the crossover arrows, and the color-matched candles.

**Dashboard.** A toggle to show or hide the panel and a dropdown to choose which chart corner it docks to.

**Alerts.** Editable text fields defining the action keyword sent in the JSON payload for each of the eight tracked events, letting the output match whatever automation platform is receiving it.

**Colors.** A full set of color pickers covering the oscillator lines, histogram, zones, arrows, candle tones, trade-planning lines and fills, and dashboard styling. Purely cosmetic, with no effect on calculations.

## How to Use It

Treat a BULL or BEAR arrow as the point where every enabled filter — the primary cross, the secondary QQE confirmation, the ADX gate, and the higher-timeframe bias — has already agreed on a direction. Use candle color intensity and histogram height as a secondary read on how strong the current momentum reading is relative to its own recent average, rather than as a standalone signal. Scan the dashboard's Bias, Confluence, and HTF Bias rows for a fast multi-factor summary without inspecting the oscillator pane directly.

Enable the trade levels option to have the script draw a stop-loss and three take-profit targets automatically on each qualifying signal, and use the lock control to freeze that plan while managing an open position. For automation, create a TradingView alert using the "Any alert() function call" option to receive the full JSON payload stream, or use the individual named alert conditions if only a single event type is needed.

The publisher is explicit that this is a momentum and confluence framework, not a complete trading system on its own. Combine it with your own market structure, support/resistance, or volatility context before acting on any signal.

## Pros & Cons

**Pros:**
- The layered pipeline — pre-smoothing, dual QQE, ADX gate, HTF bias — means a signal only qualifies after passing several independent checks, rather than firing on a raw momentum flip
- Eight selectable pre-smoothing algorithms give real control over the responsiveness and noise profile of every downstream signal
- The higher-timeframe bias filter uses the standard non-repainting pattern, so historical values match what was available in real time
- Signal confirmation is evaluated on the prior completed bar, so markers do not shift or disappear intra-bar
- Built-in ATR trade planner and JSON alert payloads make it usable as a signal engine for external automation without manual message formatting
- Dashboard consolidates bias, confluence, HTF state, ADX, DI readings, and active trade levels in one panel

**Cons:**
- The stack of components makes the learning curve steeper than a plain QQE — understanding what each layer contributes takes screen time
- No standalone position-sizing or portfolio-level risk logic beyond the ATR stop and R:R targets
- The tool does not supply market structure or support/resistance context, so it can feel incomplete if you already run a multi-timeframe workflow
- Because eight pre-smoothing options change the responsiveness of every signal, misconfiguring that stage will materially alter behavior

## Who Should Use This

This is for traders who understand that confluence means layered agreement, not more indicators. If you already read price action and want a momentum tool whose signals respect a higher-timeframe bias and trend strength, it fits that role. The trade planner and JSON alerts make it a reasonable candidate for anyone wiring signals into an external workflow. Traders who don't understand what QQE is measuring will find the number of moving parts overwhelming, and the publisher's own guidance applies: treat it as a framework, not a complete system.

## Alternatives Worth Considering

For a pure baseline, the standard QQE by Glaz remains a solid reference point. For more aggressive trend following, SuperTrend combined with an RSI gives similar confluence without the layered filter stack. For crypto specifically, VWAP plus QQE is a simpler combination.

## FAQ

**Is this indicator repainting?**
The higher-timeframe bias filter uses the previous, already-confirmed value on the higher timeframe combined

## Go Deeper with The Indicator Lab

🔬 **The Lab Report** — 123 indicators. 20 markets. One consensus verdict every 15 minutes. Stop guessing which indicator to trust.

[Subscribe $49/mo →](https://theindicatorlab.com/the-lab-report/)

📈 **The Lab Edge** — Time-Series Momentum across 166 markets. The same framework institutions use. Weekly signals to your phone.

[Subscribe $79/mo →](https://theindicatorlab.com/lab-edge/)

📊 **Prefer to trade on your own?** Power your analysis on TradingView — the platform behind every review on this site.

[Try TradingView Free →](https://www.tradingview.com/?aff_id=166324)
*Affiliate link · We earn a commission at no extra cost to you*

---
*Data source: TradingView. This review is based on publicly available indicator information and hands-on testing. Always test indicators in a demo environment before live trading.*
