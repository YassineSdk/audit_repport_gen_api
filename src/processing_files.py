from processing_pdf import exctract_text_from_pdf
import json

pdfs = ["audit_report.pdf","financial_repport.pdf"]
def process_files(paths = list)-> dict:
    folders = {}
    for file in pdfs :
        file_name = file.split(".")[0]
        text = exctract_text_from_pdf(file)
        if text.strip():
            folders[file_name] = text
    with open("text.json","w",encoding="utf-8") as f:
        json.dump(folders,f,indent=4,ensure_ascii=False)
    return folders

folders = process_files(pdfs)
print(folders)