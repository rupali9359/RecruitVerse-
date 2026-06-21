import fitz
import os

INPUT_FOLDER = "data/raw_resumes/real"
OUTPUT_FOLDER = "data/parsed_resumes/raw_text"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def extract_text_from_pdf(pdf_path):

    text = ""

    try:

        pdf = fitz.open(pdf_path)

        for page in pdf:
            text += page.get_text()

        pdf.close()

    except Exception as e:

        print(f"Error: {e}")

    return text


def process_pdfs(limit=50):

    pdf_files = [
        file
        for file in os.listdir(INPUT_FOLDER)
        if file.endswith(".pdf")
    ]

    print(f"Found {len(pdf_files)} PDFs")

    for pdf_file in pdf_files[:limit]:

        pdf_path = os.path.join(
            INPUT_FOLDER,
            pdf_file
        )

        text = extract_text_from_pdf(
            pdf_path
        )

        output_file = os.path.join(
            OUTPUT_FOLDER,
            pdf_file.replace(
                ".pdf",
                ".txt"
            )
        )

        with open(
            output_file,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(text)

        print(
            f"Processed: {pdf_file}"
        )

    print("\nDone")


if __name__ == "__main__":

    process_pdfs(limit=50)
