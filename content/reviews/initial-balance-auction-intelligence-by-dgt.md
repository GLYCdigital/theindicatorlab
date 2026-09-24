---
title: "Initial_Balance_Auction_Intelligence_By_Dgt Review: Settings, Strategy & How to Use It"
date: 2026-08-31
draft: false
type: reviews
image: "/screenshots/initial-balance-auction-intelligence-by-dgt.png"
tags:
  - "initial balance auction intelligence by dgt"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Honest Initial_Balance_Auction_Intelligence_By_Dgt review. Tested settings, entry logic, pros/cons, and who should use this auction-based trend indicator."
tv_script_url: "https://www.tradingview.com/script/ks2QGulb-Initial-Balance-Auction-Intelligence-by-DGT/"
sources: ["https://www.tradingview.com/script/ks2QGulb-Initial-Balance-Auction-Intelligence-by-DGT/"]
---
# Initial_Balance_Auction_Intelligence_By_Dgt Review

Initial_Balance_Auction_Intelligence_By_Dgt is an Auction Market Theory framework built around the Initial Balance (IB) — the range established during a selected opening session. Rather than treating the IB as static support or resistance, it tracks how price develops after the IB completes, using configurable post-IB auction windows to classify market states.

## What This Indicator Actually Does

The tool anchors on the Initial Balance, with IBH and IBL as the boundaries and IBM as the midpoint. Session and timezone are configurable (chart Exchange timezone or a range of predefined markets), so the framework can adapt to different markets and sessions.

Once the IB completes, the indicator evaluates each subsequent auction window against it. The available states are:

- **PROBING ABOVE/BELOW** — live, tentative; price beyond a boundary while the window is still forming
- **ACCEPTED ABOVE/BELOW** — a completed window closes outside the IB
- **FAILED ABOVE/BELOW** — price extends beyond a boundary but closes back inside
- **CONTINUATION** — after acceptance, a retest of that boundary holds
- **REJECTION** — after acceptance, a retest fails and price moves back through it
- **TWO-SIDED AUCTION** — both IB extremes tested and rejected, a more rotational, conflicted read

Only completed windows confirm a state transition. Probing states are live, developing information.

The framework also produces Regime, Bias, Phase, Auction State, cumulative Pressure, Quality, Maturity, and Invalidation levels.

## Key Features That Stand Out

**Decision Candles** (optional) visualize the developing auction window's High/Low and Open/Close, highlighted when the window interacts with IBH or IBL. This is live information until the window completes.

**Initial Balance Projections** (optional) extend reference levels above IBH and below IBL at 0.5×, 1.0×, and 1.5× the IB range. These are reference levels for evaluating potential range extension — not predicted or guaranteed targets.

**Pressure** is a bounded −100..+100 reading, accumulated across the whole session from confirmed transitions. **Bias** reflects only the current event. These are deliberately different questions and can disagree. Pressure is not order-flow, volume, or a probability.

**Regime** (session character: Balanced / Rotational / Expansion / Failed Expansion / Trend Auction) and **Phase** (lifecycle stage: Balance → Probe → Acceptance → Retest → Expansion/Rotation → Exhaustion) provide higher-level context on top of the raw auction state.

**Quality/Conviction** combines close strength, IB-relative extension, and retest behavior to grade confirmed events — Acceptance/Continuation use acceptance criteria, while Failed/Rejection/Two-Sided use failure criteria. **Maturity** tracks how long a state has held (Early → Developing → Mature → Exhausted).

The optional **dashboard** shows Regime, Bias, Phase, Auction State, Pressure, Quality, and Next (the next structural event or retest level plus its invalidation price), each with a contextual tooltip.

## Settings and How to Tune Them

- **Session and timezone:** Configurable to chart Exchange timezone or a range of predefined markets. The session and timezone should match the market being analyzed.
- **Auction window length:** Configurable — the documentation lists 5/10/15/30 min as options. This is the post-IB window the engine evaluates against the IB.
- **Decision Candles:** Optional toggle.
- **Initial Balance Projections:** Optional toggle for the 0.5×, 1.0×, and 1.5× IB range reference levels.
- **Dashboard:** Optional toggle.

## How to Read It

The script is a contextual framework, not a standalone signal. Read Regime, Bias, Phase, Pressure, Quality, and Invalidation together — acceptance can support continuation, failed auctions can signal reversion toward balance, and two-sided auctions can favor rotation.

Alerts fire on confirmed transitions (Accepted/Failed Above/Below, Two-Sided, Continuation, Rejection) and include the relevant level, instrument, and IB session context.

## Important Notes

- Designed for intraday timeframes ≤ 30 minutes; the engine operates only when this condition is met.
- Session and timezone should match the market being analyzed.
- Uses 1-minute lower-timeframe data on higher intraday charts for precise auction-window construction.
- Live probes and Decision Candles are developing information; state transitions confirm only when the selected auction window completes.

## Pros & Cons

**Pros:**
- Tracks auction development after the IB rather than treating the IB as static support/resistance
- Configurable session and timezone to adapt to different markets
- Distinguishes confirmed transitions from live probing states
- Pressure and Bias are deliberately separate readings and can disagree, which is disclosed rather than hidden
- Alerts fire on confirmed transitions

**Cons:**
- Contextual framework, not a standalone signal — requires the user to interpret multiple outputs together
- Only operates on intraday timeframes ≤ 30 minutes
- Requires session and timezone to be configured correctly to be meaningful

## Who It's For

Traders already familiar with Auction Market Theory concepts — acceptance, failed auction, rotation, and balance — who want a systematic way to track post-IB development. It is not a plug-and-play signal tool, and it is not intended for timeframes above 30 minutes.

## FAQ

**Does this work on crypto?** The documentation does not make market-specific claims. Session and timezone are configurable so the framework can adapt to different markets and sessions, but the session and timezone should match the market being analyzed.

**What timeframe should I use?** The script is designed for intraday timeframes ≤ 30 minutes; the engine operates only when this condition is met.

**Does this indicator repaint?** Live probes and Decision Candles are developing information. State transitions confirm only when the selected auction window completes.

## Final Verdict

Initial_Balance_Auction_Intelligence_By_Dgt is a well-structured Auction Market Theory framework. Its strength is that it treats the Initial Balance as a starting point for reading auction development rather than as a fixed level, and it is explicit about the difference between live probing states and confirmed transitions. It is not a standalone signal and it is scoped to intraday timeframes ≤ 30 minutes, so it will not suit every trader. For those who already read session structure and want it systematized, it is a coherent addition to a toolkit.

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
