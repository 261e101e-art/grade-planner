import pytest

from grade_planner.calculator import (
    calculate_current_score,
    calculate_final_score,
    calculate_required_score,
    calculate_weighted_score,
)


def test_calculate_weighted_score() -> None:
    assert calculate_weighted_score(0.4, 80) == pytest.approx(32.0)


def test_calculate_current_score() -> None:
    result = calculate_current_score(
        weights=[0.4, 0.2],
        scores=[64, 85],
    )
    assert result == pytest.approx(42.6)


def test_calculate_required_score() -> None:
    result = calculate_required_score(
        current_score=42.6,
        remaining_weight=0.4,
        target_score=70,
    )
    assert result == pytest.approx(68.5)


def test_calculate_final_score() -> None:
    result = calculate_final_score(
        current_score=42.6,
        remaining_weight=0.4,
        remaining_score=70,
    )
    assert result == pytest.approx(70.6)


def test_invalid_weight() -> None:
    with pytest.raises(ValueError):
        calculate_weighted_score(1.2, 80)


def test_invalid_score() -> None:
    with pytest.raises(ValueError):
        calculate_weighted_score(0.4, 120)


def test_mismatched_lengths() -> None:
    with pytest.raises(ValueError):
        calculate_current_score(
            weights=[0.4, 0.2],
            scores=[64],
        )


def test_invalid_remaining_weight() -> None:
    with pytest.raises(ValueError):
        calculate_required_score(
            current_score=42.6,
            remaining_weight=0,
            target_score=70,
        )