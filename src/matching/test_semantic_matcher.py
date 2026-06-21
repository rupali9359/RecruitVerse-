from semantic_matcher import (
    semantic_match
)

resume_skills = [

    "Python",
    "ML",
    "PySpark"
]

jd_skills = [

    "Python",
    "Machine Learning",
    "Spark"
]

result = semantic_match(
    resume_skills,
    jd_skills
)

print(result)