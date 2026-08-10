from pathlib import Path
from time import perf_counter

import matplotlib.pyplot as plt
import numpy as np


CURRENT_SCORE = 42.6
REMAINING_WEIGHT = 0.4
REPEATS = 20000


def python_loop_projection() -> list[float]:
    """Calculate 101 possible final grades using a Python loop."""
    results = []

    for score in range(101):
        final_score = CURRENT_SCORE + REMAINING_WEIGHT * score
        results.append(final_score)

    return results


def numpy_projection() -> np.ndarray:
    """Calculate 101 possible final grades using NumPy."""
    scores = np.arange(101)

    return CURRENT_SCORE + REMAINING_WEIGHT * scores


def measure_time(function) -> float:
    """Measure average execution time in microseconds."""
    start = perf_counter()

    for _ in range(REPEATS):
        function()

    end = perf_counter()

    return (end - start) / REPEATS * 1_000_000


def main() -> None:
    python_time = measure_time(python_loop_projection)
    numpy_time = measure_time(numpy_projection)

    print(f"Python loop: {python_time:.3f} microseconds")
    print(f"NumPy      : {numpy_time:.3f} microseconds")

    methods = ["Python loop", "NumPy"]
    times = [python_time, numpy_time]

    plt.figure(figsize=(6, 4))
    plt.bar(methods, times)

    plt.ylabel("Average execution time (microseconds)")
    plt.title("Grade Projection Performance")
    plt.tight_layout()

    output_path = Path("benchmark.pdf")
    plt.savefig(output_path, format="pdf")
    plt.close()

    print(f"Benchmark figure saved as {output_path}")


if __name__ == "__main__":
    main()