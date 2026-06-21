from candidate_filters import (
    filter_by_skill
)

candidates = [

    {
        "resume_name":"resume1.pdf",

        "matched_skills":[
            "Python",
            "SQL"
        ]
    },

    {
        "resume_name":"resume2.pdf",

        "matched_skills":[
            "Java",
            "Spring"
        ]
    },

    {
        "resume_name":"resume3.pdf",

        "matched_skills":[
            "Python",
            "AWS"
        ]
    }

]

result = filter_by_skill(
    candidates,
    "python"
)

print(result)