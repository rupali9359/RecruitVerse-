def generate_analytics(results):

    scores = [

        candidate["score"]

        for candidate in results
    ]

    analytics = {

        "total_candidates":
        len(scores),

        "average_score":
        round(
            sum(scores) / len(scores),
            2
        ),

        "highest_score":
        max(scores),

        "lowest_score":
        min(scores)
    }

    return analytics