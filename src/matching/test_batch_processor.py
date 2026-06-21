from batch_processor import (
    load_resumes
)

resumes = load_resumes()

print(
    f"Total Resumes Loaded: "
    f"{len(resumes)}"
)

print(
    resumes[0]["resume_name"]
)