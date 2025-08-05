from docx import Document

def populate_credit_memo(template_path, output_path, context):
    doc = Document(template_path)
    for para in doc.paragraphs:
        for key, value in context.items():
            if key in para.text:
                para.text = para.text.replace(key, value)
    doc.save(output_path)
