---
title: "Market_Structure_Flow_Map_Boswaves Review: Settings, Strategy & How to Use It"
date: 2026-09-13
draft: false
type: reviews
image: "/screenshots/market-structure-flow-map-boswaves.png"
tags:
  - "market structure flow map boswaves"
  - "trend"
  - "tradingview"
  - "indicator"
  - "review"
  - "trading"
categories:
  - "Trend"
  - Technical Analysis
rating: 4
description: "Market_Structure_Flow_Map_Boswaves review: how this BOS and wave-mapping trend indicator works, its settings, entry logic, and honest pros and cons."
tv_script_url: "https://www.tradingview.com/script/fdGNrwvp-Market-Structure-Flow-Map-BOSWaves/"
sources: ["https://www.tradingview.com/script/fdGNrwvp-Market-Structure-Flow-Map-BOSWaves/"]
---
Market Structure Flow Map [BOSWaves] does one thing well: it renders the skeleton of a trend and encodes it with conviction information rather than treating every structural break as equivalent. If you have scrolled through a chart full of identical BOS labels and thought there is no way to tell which breaks actually mattered, this indicator is the response to that complaint. It identifies swing highs and lows, flags Break of Structure (BOS) and Change of Character (CHoCH) events, and renders each one as a curved three-layer ribbon whose width, glow, and arc curvature are driven by a composite strength score. It is a structure visualization tool first, a signal tool second — and that distinction matters for how you should use it.

## What it actually plots

The core of the indicator is a swing engine. It identifies confirmed pivot highs and lows using a configurable lookback, tracks the most recent unbroken high and low with their bar indices and prices, and detects breaks when the current bar crosses a level the previous bar had not, provided the level has not been broken since its last registration. Depending on the break mode, either the close price or the bar's high and low extremes serve as the break source.

What separates this from single-BOS indicators is the ribbon rendering. Each structural break is drawn as a curved polyline ribbon connecting the broken swing pivot to the break bar, built from three chart points: the origin swing bar, the temporal midpoint, and the break bar. The midpoint arc height is calculated from ATR, the arc ATR multiplier, a distance factor derived from the bar span, and the composite strength. For bullish breaks the arc curves above both endpoints; for bearish breaks below.

Ribbon thickness is the primary strength indicator. Displacement strength is the distance from the broken level to the break source, normalized against an ATR multiple and capped at the configured maximum. Volume strength is the excess of the break bar's volume above average relative to the configured maximum ratio, with below-average volume bars receiving zero volume strength. These are combined using configurable displacement and volume weights, normalized by their sum, producing a 0-1 composite score that drives all ribbon visual properties.

The three-layer rendering gives each ribbon depth: a glow layer at the body width plus five with high transparency, a body layer at the strength-scaled width with low transparency, and a core layer at the body width minus two with a near-white color at low transparency. Circular node markers anchor each ribbon origin to its precise swing price, and directional event labels sit at each break bar.

## Settings and How to Tune Them

The indicator exposes swing length, break confirmation mode, volume average period, displacement weight, volume weight, ribbon arc ATR multiplier, maximum event count, and independent visibility toggles for BOS, CHoCH, structure nodes, and candle coloring. The source material suggests a baseline configuration of Swing Length 8, Break Confirmation set to Close, Volume Average 20, Displacement Weight 0.6, Volume Weight 0.4, Ribbon Arc (ATR×) 0.7, Maximum Events 35, with BOS and CHoCH shown, structure nodes shown, and candle coloring disabled. These are presented as a starting point, not an optimum; the source notes that effectiveness depends on the instrument's swing frequency, typical displacement characteristics, and preferred structural event density.

The calibration notes offer directional guidance rather than fixed values. If too many structural events fire, increase swing length to demand more significant pivot confirmation, or switch break confirmation to Close to filter out wick-based marginal breaks. If events are too infrequent, decrease swing length for more sensitive pivot detection, or switch to Wick mode to capture breaks that close below the level but print a wick through it. If all ribbons appear similar in width, adjust the maximum displacement ATR and maximum volume ratio to calibrate scoring thresholds to the instrument — if most breaks exceed the maximum thresholds, the scoring range collapses and ribbons cluster near maximum width. If volume scoring is not contributing, decrease the maximum volume ratio or increase volume weight. If ribbons are too flat or too curved, adjust the ribbon arc ATR multiplier. If ribbons clutter the chart, reduce the maximum event count.

Adjustments should be incremental and evaluated across multiple session types rather than isolated market conditions.

## How to interpret it

The indicator presents four event types. Bullish BOS is a cyan ribbon arcing upward from a broken swing high during an established bullish structural state, confirming continuation. Bearish BOS is a red ribbon arcing downward from a broken swing low during a bearish state. Bullish CHoCH is a green ribbon arcing upward from a broken swing high during a bearish state, signaling a potential reversal. Bearish CHoCH is an amber ribbon arcing downward from a broken swing low during a bullish state.

The source material frames interpretation around several readings. Ribbon width is the primary strength indicator: thick ribbons represent high composite strength with strong displacement and above-average volume, while thin ribbons represent weak breaks that barely cleared the level with low participation. Arc height reflects both ATR-relative volatility and the temporal distance between swing origin and break bar — tall arcs indicate breaks that developed over many bars or occurred during high-volatility conditions, flat arcs indicate quick breaks between adjacent swings. The glow layer scales with ribbon width, making the strongest ribbons identifiable across the full chart view. Structure nodes anchor each event to its precise swing price. Optional candle coloring reflects the current structural state, coloring cyan during bullish structure and red during bearish structure regardless of individual bar direction.

BOS and CHoCH events can be independently toggled, allowing the chart to focus on continuation signals, reversal signals, or both. Alert generation covers bullish and bearish structural breaks.

## Strategy integration

The source material outlines several approaches. Ribbon width prioritization assigns greater analytical weight to thick ribbons representing high-strength breaks, while thin ribbons from marginal low-volume breaks carry reduced significance and warrant more caution before acting on the direction signal. The CHoCH reversal framework treats green and amber CHoCH ribbons as primary reversal identification signals, with subsequent BOS ribbons in the new direction providing continuation confirmation. The BOS continuation framework treats cyan and red BOS ribbons as trend continuation evidence within established structural regimes.

Arc length serves as temporal context: short low arcs between adjacent swings indicate rapid structural progression, while tall arcs spanning many bars indicate breaks that required extended time to develop. Ribbon density and direction consistency provide a visual structural momentum reading — a sequence of uniformly wide same-direction ribbons indicates sustained structural conviction, while a mix of widths and directions indicates contested structure. The source also suggests applying higher-timeframe structural state as directional bias context while using lower-timeframe BOS ribbons to time continuation entries.

Integration guidance emphasizes confluence with volume flow tools, order flow analysis, or momentum indicators. A single CHoCH ribbon is not sufficient confirmation of a reversal in isolation; the source recommends waiting for a subsequent BOS ribbon in the new direction before treating the CHoCH as a completed reversal. State discipline means maintaining structural bias aligned with the most recent CHoCH until an opposing CHoCH confirms a shift, interpreting individual BOS ribbons within an established trend as continuation rather than reversal evidence.

## Pros and cons

**Pros:**
- Encodes structural conviction into visual weight rather than presenting all breaks as equivalent events
- The composite strength score combines displacement and volume into a single 0-1 measure driving all ribbon properties
- Three-layer ribbon rendering with glow, body, and core provides visual depth and hierarchy
- Independent toggles for BOS and CHoCH allow focused analysis
- Object management trims all arrays to a configurable maximum event count, maintaining a clean rolling window

**Cons:**
- Event classification is state-dependent, so CHoCH versus BOS labeling relies on the tracked structural state at the time of the break
- Volume scoring produces zero contribution on instruments where volume is consistently below average, suppressing ribbon differentiation
- Arc height can render ribbons either too flat to read or dramatically dominant depending on the instrument's typical ATR range
- Choppy, range-bound markets produce dense mixed-color ribbon clusters without a clear structural narrative
- The strength scoring range collapses if most breaks exceed the maximum displacement and volume thresholds, making all ribbons appear similar in width

## Who it's for

Discretionary traders who already understand market structure and want a conviction-weighted visual of it. The source material positions this for momentum-validated market structure and conviction-weighted structural analysis approaches, with timeframe guidance spanning intraday structural flow mapping through swing-level visualization. It is not a plug-and-play signal generator — the source explicitly states it does not predict future price movements and recommends deploying it within a broader analytical framework incorporating order flow context, volume analysis, and risk management.

## Alternatives

The source material does not name specific competing products. General guidance: if you want raw BOS and CHoCH labeling without the strength-scoring layer, standard market structure indicators will suffice. If you want conviction weighting combined with momentum or order flow confirmation, pairing a structure tool with a separate momentum or volume analysis will provide broader context than any single indicator.

## FAQ

**Does it repaint?**
The source material does not make a repainting claim. It describes real-time execution on each confirmed bar with polyline and label objects created at event time, and states that a qualifying break requires the current bar to have crossed the level while the previous bar had not.

**What timeframe is best?**
The source offers guidance by bracket rather than a single answer. Lower intraday timeframes suit structural flow mapping with shorter swing length for faster detection on smaller swings. Mid-range timeframes suit session-level structural analysis with balanced swing length. Higher timeframes suit swing-level visualization with longer swing detection for broader structural events.

**Can I use it for entries alone?**
The source presents it as a visualization and structural event analysis tool that does not predict future price movements, and recommends deploying it within a broader analytical framework.

**Does it work on crypto and forex?**
The source material does not make market-specific claims. It notes that low-liquidity instruments where volume is consistently below average will suppress volume strength scores, and that instruments with consistent volume participation produce more meaningful differentiation.

**Is it worth it over free structure indicators?**
The source material does not make a comparative value claim. The differentiator it describes is the strength-scored ribbon rendering — width, glow, and arc curvature scaled by a composite displacement and volume score — rather than uniform visual treatment of every break.

## Final verdict

Market Structure Flow Map [BOSWaves] is a structure visualization tool built around a defensible premise: not all structural breaks carry equal significance, and visual weight should reflect that. The composite strength scoring, three-layer ribbon geometry, and distance-adaptive arc height combine to produce a chart where the structural history reads as a conviction hierarchy rather than a flat sequence of identical events. The limitations are inherent to the design — volume scoring depends on participation, arc rendering depends on the instrument's ATR characteristics, and choppy conditions produce cluttered output regardless of the scoring layer. The source material is explicit that this is a visualization and analysis tool, not a predictive system, and treats it as one component within a broader framework. For traders who already read structure and want the conviction dimension made visible, it addresses a real gap.

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
