import fitz 
import os

SUPPORTED_TYPE="application/pdf"

def exctract_text_from_pdf(file_path: str)->str:
    """Extract raw text from a PDF file , page by page"""

    doc = fitz.open(file_path)
    collection = []
    for page_num, page in enumerate(doc, start=1):
        text = page.get_text("text")
        if text.strip():
            collection.append(f"---Page {page_num} ---\n{text.strip()}")
    doc.close()
    if not collection:
        raise ValueError("No text could be extrated from this doc ")

    return "\n\n".join(collection)
