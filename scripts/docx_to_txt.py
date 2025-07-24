import sys
from docx import Document

def docx_to_txt(docx_path, txt_path):
    doc = Document(docx_path)
    with open(txt_path, 'w', encoding='utf-8') as f:
        for para in doc.paragraphs:
            f.write(para.text + '\n')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python docx_to_txt.py input.docx output.txt")
        sys.exit(1)
    docx_to_txt(sys.argv[1], sys.argv[2]) 