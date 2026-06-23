from collections import Counter

def get_top_skills(
        skills_list):

    counter = Counter(
        skills_list
    )

    return counter.most_common(10)