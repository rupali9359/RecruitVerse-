from candidate_search import search_candidate

candidates = [

    {
        "resume_name":
        "python_developer.pdf",

        "final_score":
        91
    },

    {
        "resume_name":
        "java_developer.pdf",

        "final_score":
        84
    },

    {
        "resume_name":
        "python_ml_engineer.pdf",

        "final_score":
        95
    }

]

result = search_candidate(
    candidates,
    "python"
)

print(result)