from docx import Document

def read_docx_para(file_path):
    doc = Document(file_path)
    paragraphs = []
    for paragraph in doc.paragraphs:
        if paragraph.text:
            paragraphs.append(paragraph.text)
    return paragraphs

def main(file_path):
    paragraphs = read_docx_para(file_path)
    for i, paragraph in enumerate(paragraphs):
        if paragraph:
            print(f"Paragraph {i}: {paragraph}")

if __name__ == "__main__":
    print(main("Diary/Week 14.docx"))