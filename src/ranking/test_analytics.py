from analytics import (
    generate_analytics
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

analytics = generate_analytics(
    results
)

print(analytics)