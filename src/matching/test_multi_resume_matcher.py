from multi_resume_matcher import (
    process_resumes
)

resumes = [

    {
        "resume_name":
        "resume1.pdf",

        "text":
        """
        Python
        SQL
        AWS
        """
    },

    {
        "resume_name":
        "resume2.pdf",

        "text":
        """
        Python
        Machine Learning
        AWS
        """
    },

    {
        "resume_name":
        "resume3.pdf",

        "text":
        """
        Java
        Spring
        """
    }

]

jd_text = """

Python
SQL
AWS
Machine Learning

"""

results = process_resumes(
    resumes,
    jd_text
)

for result in results:

    print(result)