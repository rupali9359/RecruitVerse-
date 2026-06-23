from recommend_jobs import recommend_jobs

resume_text = """
Python
SQL
Machine Learning
Data Analysis
"""

results = recommend_jobs(
    resume_text,
    "data/job_descriptions"
)

print(results)