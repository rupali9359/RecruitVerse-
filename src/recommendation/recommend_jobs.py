import os

from job_matcher import match_resume_to_job

def recommend_jobs(resume_text, jd_folder):

    results = []

    for file in os.listdir(jd_folder):

        if not file.endswith(".txt"):
            continue

        with open(
            os.path.join(jd_folder, file),
            "r",
            encoding="utf-8"
        ) as f:

            jd_text = f.read()

        score = match_resume_to_job(
            resume_text,
            jd_text
        )

        results.append(
            {
                "job": file,
                "score": score
            }
        )

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results[:5]