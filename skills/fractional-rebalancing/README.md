# Fractional Rebalancing Strategy Skill

This skill complements the root Toss Securities API skill. It handles portfolio-level monitoring, target-weight rebalancing proposals, twice-monthly candidate research and versioned strategy evaluation. It does not execute orders.

## Suggested use
Install or copy this directory into the agent's skills directory, then ask the agent to run a daily check or a semi-monthly candidate review. Follow the host agent's skill discovery rules.

## Project layout
- `SKILL.md`: operating policy
- `master/MASTER_STRATEGY.csv`: editable defaults and parameter definitions (use as a text-based starter; the local package also includes an XLSX workbook)
- `src/strategy_rules.py`: deterministic weight/drift helpers
- `tests/test_strategy_rules.py`: unit tests
- `reports/templates/`: daily, semi-monthly and monthly templates

## Portfolio defaults
- Toss Securities: KRW 100,000 initial capital
- Kakao Pay Securities: KRW 100,000 initial capital (verify exact provider and app support)
- Review every day; formal candidate/rebalance reviews twice monthly
- No automatic live order execution

## Important
Market data, authenticated holdings, broker eligibility, fees and FX costs must be connected or provided by the user. Missing data must be reported, not guessed. Strategy changes and all live orders require user approval.
