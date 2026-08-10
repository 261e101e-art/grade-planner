import argparse
from grade_planner.plot import create_projection_plot
from grade_planner.calculator import calculate_required_score
from grade_planner.io import (
    get_completed_score,
    get_remaining_weight,
    load_grade_data,
)

import argparse

from grade_planner.calculator import calculate_required_score
from grade_planner.io import (
    get_completed_score,
    get_remaining_weight,
    load_grade_data,
)
from grade_planner.plot import create_projection_plot


def main() -> None:
    """Run the Grade Planner command-line interface."""
    parser = argparse.ArgumentParser(
        description="Calculate the score required to reach a target course grade."
    )

    parser.add_argument(
        "csv_file",
        help="Path to the CSV file containing grade components.",
    )

    parser.add_argument(
        "--target",
        type=float,
        default=70.0,
        help="Target final grade. Default: 70.",
    )

    args = parser.parse_args()

    df = load_grade_data(args.csv_file)

    current_score = get_completed_score(df)
    remaining_weight = get_remaining_weight(df)

    if remaining_weight <= 0:
        print("All course components already have scores.")
        print(f"Final grade: {current_score:.2f}")
        return

    required_score = calculate_required_score(
        current_score=current_score,
        remaining_weight=remaining_weight,
        target_score=args.target,
    )

    create_projection_plot(
        current_score=current_score,
        remaining_weight=remaining_weight,
        target_score=args.target,
    )

    print("\nGrade Planner")
    print("=" * 40)
    print(f"Current weighted score : {current_score:.2f}")
    print(f"Remaining weight       : {remaining_weight:.2f}")
    print(f"Target final grade     : {args.target:.2f}")
    print("-" * 40)

    if required_score < 0:
        print("Target already achieved.")
    elif required_score > 100:
        print(
            f"Required remaining score: {required_score:.2f}"
        )
        print(
            "The target cannot be reached "
            "with a maximum score of 100."
        )
    else:
        print(
            f"Required remaining score: {required_score:.2f}"
        )

    print("\nProjection plot saved as grade_projection.pdf")


if __name__ == "__main__":
    main()