from candidate_filters import (
    get_top_candidates
)

candidates = [

    {
        "resume_name":"resume1.pdf",
        "final_score":95
    },

    {
        "resume_name":"resume2.pdf",
        "final_score":92
    },

    {
        "resume_name":"resume3.pdf",
        "final_score":88
    },

    {
        "resume_name":"resume4.pdf",
        "final_score":80
    }

]

result = get_top_candidates(
    candidates,
    2
)

print(result)