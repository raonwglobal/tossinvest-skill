"""Deterministic helpers for fractional-share rebalancing. No broker access or order execution."""
from typing import Dict, Iterable


def portfolio_weights(values: Dict[str, float]) -> Dict[str, float]:
    total = sum(max(0.0, float(v)) for v in values.values())
    if total <= 0:
        return {key: 0.0 for key in values}
    return {key: max(0.0, float(value)) / total for key, value in values.items()}


def target_drift(current_weight: float, target_weight: float) -> float:
    """Current minus target as a decimal; 0.05 means +5 percentage points."""
    return float(current_weight) - float(target_weight)


def needs_rebalance(current_weight: float, target_weight: float, threshold: float = 0.05) -> bool:
    if threshold < 0:
        raise ValueError("threshold must be non-negative")
    return abs(target_drift(current_weight, target_weight)) >= threshold


def target_amount(total_value: float, target_weight: float) -> float:
    if total_value < 0:
        raise ValueError("total_value must be non-negative")
    if not 0 <= target_weight <= 1:
        raise ValueError("target_weight must be between 0 and 1")
    return total_value * target_weight


def validate_target_weights(weights: Iterable[float]) -> bool:
    vals = [float(weight) for weight in weights]
    return all(0 <= weight <= 1 for weight in vals) and sum(vals) <= 1.0000001
