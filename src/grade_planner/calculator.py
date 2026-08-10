def calculate_weighted_score(weight: float, score: float) -> float:
    """Calculate the weighted contribution of one course component."""
    if not 0 <= weight <= 1:
        raise ValueError("Weight must be between 0 and 1.")

    if not 0 <= score <= 100:
        raise ValueError("Score must be between 0 and 100.")

    return weight * score


def calculate_current_score(
    weights: list[float],
    scores: list[float],
) -> float:
    """Calculate the total weighted score of completed components."""
    if len(weights) != len(scores):
        raise ValueError("Weights and scores must have the same length.")

    return sum(
        calculate_weighted_score(weight, score)
        for weight, score in zip(weights, scores)
    )


def calculate_required_score(
    current_score: float,
    remaining_weight: float,
    target_score: float,
) -> float:
    """Calculate the score required on the remaining component."""
    if not 0 < remaining_weight <= 1:
        raise ValueError("Remaining weight must be between 0 and 1.")

    if not 0 <= target_score <= 100:
        raise ValueError("Target score must be between 0 and 100.")

    required = (target_score - current_score) / remaining_weight

    return required


def calculate_final_score(
    current_score: float,
    remaining_weight: float,
    remaining_score: float,
) -> float:
    """Calculate the final course grade."""
    if not 0 <= remaining_score <= 100:
        raise ValueError("Remaining score must be between 0 and 100.")

    return current_score + remaining_weight * remaining_score