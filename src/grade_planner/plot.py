from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def create_projection_plot(
    current_score: float,
    remaining_weight: float,
    target_score: float,
    output_path: str | Path = "grade_projection.pdf",
) -> None:
    """Create a PDF plot showing possible final grades."""
    remaining_scores = np.linspace(0, 100, 101)

    final_scores = (
        current_score + remaining_weight * remaining_scores
    )

    plt.figure(figsize=(7, 4.5))

    plt.plot(
        remaining_scores,
        final_scores,
        label="Predicted final grade",
    )

    plt.axhline(
        y=target_score,
        linestyle="--",
        label=f"Target grade ({target_score:.0f})",
    )

    plt.xlabel("Score on remaining component")
    plt.ylabel("Final course grade")
    plt.title("Grade Projection")
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()

    plt.savefig(output_path, format="pdf")
    plt.close()