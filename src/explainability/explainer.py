def generate_explanation(
        result):

    explanation = []

    explanation.append(
        f"Match Score: "
        f"{result['score']}%"
    )

    explanation.append(
        "\nMatched Skills:"
    )

    for skill in result[
        "matched_skills"
    ]:

        explanation.append(
            f"✔ {skill}"
        )

    explanation.append(
        "\nMissing Skills:"
    )

    for skill in result[
        "missing_skills"
    ]:

        explanation.append(
            f"✘ {skill}"
        )

    return "\n".join(
        explanation
    )