print("TEST FILE STARTED")
from jd_matcher import (
    match_resume_jd
)

resume_text = """

Python
SQL
AWS
Power BI

"""

jd_text = """

Python
SQL
AWS
Machine Learning

"""

result = match_resume_jd(
    resume_text,
    jd_text
)

print("Matching Result:")
print(result)