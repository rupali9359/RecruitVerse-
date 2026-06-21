from candidate_ranker import (
    rank_candidates
)

results = [

    {
        "resume_name":
        "resume1.pdf",

        "score":
        75.0
    },

    {
        "resume_name":
        "resume2.pdf",

        "score":
        90.0
    },

    {
        "resume_name":
        "resume3.pdf",

        "score":
        60.0
    }
]

ranked = rank_candidates(
    results
)

for candidate in ranked:

    print(candidate)