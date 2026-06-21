from skill_extractor import (
    extract_skills
)

sample_resume = """

Python
SQL
Power BI
Machine Learning
AWS

"""

skills = extract_skills(
    sample_resume
)

print(
    "Extracted Skills:"
)

print(skills)