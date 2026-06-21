import os
import json

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

real_path = os.path.join(
    BASE_DIR,
    "data",
    "raw_resumes",
    "real"
)

synthetic_path = os.path.join(
    BASE_DIR,
    "data",
    "raw_resumes",
    "synthetic"
)

parsed_path = os.path.join(
    BASE_DIR,
    "data",
    "parsed_resumes",
    "raw_text"
)

job_desc_path = os.path.join(
    BASE_DIR,
    "data",
    "job_descriptions"
)

skills_file = os.path.join(
    BASE_DIR,
    "data",
    "skills_dictionary",
    "skills_dictionary.json"
)

print(BASE_DIR)
print("\n===== RECRUITVERSE DATA AUDIT =====\n")

real_count = 0
for root, dirs, files in os.walk(real_path):
    for file in files:
        if file.lower().endswith(".pdf"):
            real_count += 1

synthetic_count = 0
for root, dirs, files in os.walk(synthetic_path):
    for file in files:
        if file.lower().endswith(".pdf"):
            synthetic_count += 1

txt_count = 0
for root, dirs, files in os.walk(parsed_path):
    for file in files:
        if file.lower().endswith(".txt"):
            txt_count += 1

jd_count = 0
for file in os.listdir(job_desc_path):
    if file.endswith(".txt"):
        jd_count += 1

print(f"Real Resume PDFs      : {real_count}")
print(f"Synthetic PDFs        : {synthetic_count}")
print(f"Parsed TXT Files      : {txt_count}")
print(f"Job Descriptions      : {jd_count}")

if os.path.exists(skills_file):

    with open(skills_file, "r", encoding="utf-8") as f:
        skills_data = json.load(f)

    total_skills = sum(
        len(skill_list)
        for skill_list in skills_data.values()
    )

    print(f"Total Skills          : {total_skills}")

else:
    print("Skills file not found")

print("\n==============================")