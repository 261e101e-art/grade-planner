from pathlib import Path

import pandas as pd
import pytest

from grade_planner.io import (
    get_completed_score,
    get_remaining_weight,
    load_grade_data,
)


def test_load_grade_data(tmp_path: Path) -> None:
    csv_file = tmp_path / "grades.csv"

    csv_file.write_text(
        "component,weight,score\n"
        "midterm,0.4,64\n"
        "assignments,0.2,85\n"
        "final,0.4,\n"
    )

    df = load_grade_data(csv_file)

    assert list(df.columns) == ["component", "weight", "score"]
    assert len(df) == 3


def test_get_completed_score() -> None:
    df = pd.DataFrame(
        {
            "component": ["midterm", "assignments", "final"],
            "weight": [0.4, 0.2, 0.4],
            "score": [64.0, 85.0, None],
        }
    )

    result = get_completed_score(df)

    assert result == pytest.approx(42.6)


def test_get_remaining_weight() -> None:
    df = pd.DataFrame(
        {
            "component": ["midterm", "assignments", "final"],
            "weight": [0.4, 0.2, 0.4],
            "score": [64.0, 85.0, None],
        }
    )

    result = get_remaining_weight(df)

    assert result == pytest.approx(0.4)


def test_missing_columns(tmp_path: Path) -> None:
    csv_file = tmp_path / "invalid.csv"

    csv_file.write_text(
        "name,weight\n"
        "midterm,0.4\n"
    )

    with pytest.raises(ValueError):
        load_grade_data(csv_file)