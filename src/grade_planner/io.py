from pathlib import Path

import pandas as pd


def load_grade_data(file_path: str | Path) -> pd.DataFrame:
    """Load grade data from a CSV file."""
    df = pd.read_csv(file_path)

    required_columns = {"component", "weight", "score"}

    if not required_columns.issubset(df.columns):
        raise ValueError(
            "CSV file must contain component, weight, and score columns."
        )

    if (df["weight"] < 0).any() or (df["weight"] > 1).any():
        raise ValueError("Weights must be between 0 and 1.")

    if df["weight"].sum() > 1.000001:
        raise ValueError("Total weight cannot exceed 1.")

    completed_scores = df["score"].dropna()

    if ((completed_scores < 0) | (completed_scores > 100)).any():
        raise ValueError("Scores must be between 0 and 100.")

    return df


def get_completed_score(df: pd.DataFrame) -> float:
    """Calculate the weighted score from completed components."""
    completed = df.dropna(subset=["score"])

    return float((completed["weight"] * completed["score"]).sum())


def get_remaining_weight(df: pd.DataFrame) -> float:
    """Calculate the total weight of components without a score."""
    remaining = df[df["score"].isna()]

    return float(remaining["weight"].sum())