from explainer import (
    generate_explanation
)

result = {

    "matched_skills": [
        "Python",
        "SQL",
        "AWS"
    ],

    "missing_skills": [
        "Machine Learning"
    ],

    "score": 75.0
}

explanation = (
    generate_explanation(
        result
    )
)

print(explanation)