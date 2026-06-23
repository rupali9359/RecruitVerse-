def candidate_distribution(scores):

    result = {

        "Excellent": 0,

        "Good": 0,

        "Average": 0,

        "Poor": 0

    }

    for score in scores:

        if score >= 90:

            result["Excellent"] += 1

        elif score >= 75:

            result["Good"] += 1

        elif score >= 60:

            result["Average"] += 1

        else:

            result["Poor"] += 1

    return result