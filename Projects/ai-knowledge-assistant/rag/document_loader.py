import os
import glob
from pypdf import PdfReader


def load_documents(data_folder="data"):

    documents = []

    pdf_files = glob.glob(
        os.path.join(data_folder, "*.pdf")
    )

    if len(pdf_files) == 0:
        print("No PDF files found.")
        return documents

    print(f"Found {len(pdf_files)} PDF files.\n")

    for pdf in pdf_files:

        print(f"Loading: {pdf}")

        try:

            reader = PdfReader(pdf)

            for page_no, page in enumerate(
                reader.pages,
                start=1
            ):

                page_text = page.extract_text()

                if page_text:

                    documents.append({
                        "file": os.path.basename(pdf),
                        "page": page_no,
                        "text": page_text
                    })

        except Exception:

            print(
                f"Could not read {os.path.basename(pdf)}."
            )

            print(
                "Please check whether the PDF is valid."
            )

            continue

    print("\nAll valid PDF files loaded successfully!")

    return documents