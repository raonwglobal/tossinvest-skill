---
name: fractional-rebalancing
description: Review two separate fractional-share portfolios (Toss Securities and Kakao Pay Securities), starting at KRW 100,000 each. Create daily monitoring reports, twice-monthly candidate lists, and user-approved versioned strategy improvements. No automatic trade execution.
---

# Fractional Rebalancing Strategy

## Objective
Seek attractive risk-adjusted growth for two separately tracked portfolios:
- Toss Securities: initial capital KRW 100,000.
- Kakao Pay Securities: initial capital KRW 100,000. Confirm the exact app/provider and its available fractional-share features before broker-specific guidance.

Profit is not guaranteed. Do not claim to maximize or guarantee returns. Small balances can be materially affected by spread, commission, FX conversion, minimum order size, taxes, and fractional-share restrictions.

## Hard safety rules
1. Do not place, modify, or cancel live orders; do not transfer money or change account settings. Return proposals for the user to review.
2. Never invent prices, holdings, fills, balances, fees, eligibility, or news. Timestamp all market data and cite material sources.
3. Keep each broker's holdings, fees, order rules, eligibility and performance separate.
4. Treat the user-maintained master settings as the active configuration. Validate changes; explain conflicts and the effect before applying.
5. Strategy self-improvement means proposing and testing versioned changes, not silently changing active rules or trading.
6. Do not enable leverage, margin, short selling, options, leveraged/inverse products, or borrowed funds by default.
7. If current data is unavailable/stale, mark the field as unknown and return DATA NEEDED rather than manufacturing a signal.
8. Compare net performance after realistic fees, spread, FX and tax assumptions against an appropriate benchmark and a cash alternative.

## Default hypothesis (not a proven edge)
- Universe: liquid, established listed shares and broad-market ETFs only if each broker confirms fractional eligibility.
- Candidate review: combine trend/momentum, business quality, valuation/context, liquidity, catalysts and downside risk. Do not select on recent price gain or social-media hype alone.
- Positions: up to 3–5 holdings per portfolio only if minimum order sizes and costs make sense. Holding cash or fewer names is acceptable.
- Daily monitoring; formal rebalance reviews twice per month, on the 1st and 15th calendar day or the next trading day.
- Consider rebalance when absolute target-weight drift meets the master setting, thesis changes materially, or a risk limit/corporate action is triggered. A daily review does not imply a daily trade.
- Initial editable defaults: 5 percentage-point drift threshold, 10% cash reserve floor, 35% maximum single-name weight, 50% sector cap. These are starting assumptions, not optimized parameters.

## Daily workflow
1. Read master settings and current version.
2. Gather timestamped prices, holdings, cash, benchmark, FX where relevant, market calendar, corporate actions and material company news from reliable sources.
3. Validate source freshness and broker-specific fractional eligibility.
4. Calculate portfolio value, weights, P/L, target drift, concentration and risk flags from actual user-provided or connected data.
5. Produce a dated daily report with status labels: HOLD, WATCH, REBALANCE CANDIDATE, DATA NEEDED.
6. Explain why action may be warranted or why doing nothing is preferable; include downside scenarios, costs and missing information.
7. Never present a proposal as an order already submitted.

## Twice-monthly candidates
On the 1st and 15th (or next trading day), screen each broker's eligible universe separately. Return up to five candidates with:
- ticker, company, exchange and eligibility evidence/date;
- thesis and valuation/context;
- catalyst and expected holding horizon;
- liquidity and estimated transaction/FX costs;
- key downside risks and thesis invalidation conditions;
- fit versus existing holdings, benchmark and cash;
- proposed target weights only when current portfolio data and constraints are known.
State explicitly that candidates are research proposals, not guaranteed winners.

## Master-sheet changes
- User edits override defaults only after validation.
- Target weights must be 0–100% and sum to no more than 100%; the remainder can be cash.
- Report before/after values, expected benefit, trade-off, date and strategy version.
- Keep a change log and preserve rollback information.
- Ask one focused question only when a conflict prevents a safe interpretation.

## Monthly self-improvement
Evaluate net return vs benchmark/cash, volatility, maximum drawdown, turnover, costs, concentration, win/loss distribution and data quality. Separate realized results from backtests/paper results. Test changes with transaction costs, slippage, out-of-sample periods and survivorship-bias caveats. Propose a versioned change only when evidence is stronger than the current baseline and risk limits remain satisfied. User approval is required to activate a new strategy.

## Report storage
Use the templates in `reports/templates/`. Store dated reports under daily, semi-monthly and monthly directories. Keep source URLs, timestamps, assumptions and version metadata. GitHub is the versioned source for code and strategy documentation; do not commit account statements, private holdings, tokens, API keys or other sensitive personal data. A private Drive master sheet may contain personal portfolio data.

## Commands the user can request
- "Run daily rebalancing check"
- "Prepare this month's 1st/15th candidate list"
- "Compare both broker portfolios against the benchmark"
- "Review master settings and propose changes"
- "Run monthly strategy evaluation"
