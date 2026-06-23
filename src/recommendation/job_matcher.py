def match_resume_to_job(resume_text, jd_text):

    resume_words = set(
        resume_text.lower().split()
    )

    jd_words = set(
        jd_text.lower().split()
    )

    common = resume_words.intersection(
        jd_words
    )

    score = len(common) / max(
        len(jd_words),
        1
    )

    return round(score, 2)