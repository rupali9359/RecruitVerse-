from candidate_filters import filter_by_score

candidates = [

    {
        "resume_name":
        "resume1.pdf",

        "final_score":
        95
    },

    {
        "resume_name":
        "resume2.pdf",

        "final_score":
        76
    },

    {
        "resume_name":
        "resume3.pdf",

        "final_score":
        88
    }

]

result = filter_by_score(
    candidates,
    80
)

print(result)
