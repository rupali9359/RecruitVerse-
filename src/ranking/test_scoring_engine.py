from scoring_engine import (
    calculate_score
)

matched_skills = [

    "Python",
    "SQL",
    "AWS"
]

jd_skills = [

    "Python",
    "SQL",
    "AWS",
    "Machine Learning"
]

score = calculate_score(

    matched_skills,
    jd_skills

)

print(
    f"Candidate Score: {score}%"
)