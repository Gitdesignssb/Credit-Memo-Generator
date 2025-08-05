import streamlit as st
import os
from docx import Document

# Title of the app
st.title("GenAI Credit Memo Generator")

# Input fields
company_name = st.text_input("Company Name")
sector = st.text_input("Sector")
loan_amount = st.number_input("Loan Amount (USD)", min_value=0.0)

# Upload template
uploaded_template = st.file_uploader("Upload Credit Memo Template (.docx)", type="docx")

# Generate memo button
if st.button("Generate Credit Memo") and uploaded_template is not None and company_name:
    # Save uploaded template to a temporary path
    template_path = f"templates/{uploaded_template.name}"
    with open(template_path, "wb") as f:
        f.write(uploaded_template.getbuffer())

    # Define output path
    output_path = f"data/{company_name}_Credit_Memo.docx"

    # Context for placeholder replacement
    context = {
        "{{CompanyName}}": company_name,
        "{{Sector}}": sector,
        "{{LoanAmount}}": str(loan_amount)
    }

    # Function to populate the credit memo
    def populate_credit_memo(template_path, output_path, context):
        doc = Document(template_path)
        for para in doc.paragraphs:
            for key, value in context.items():
                if key in para.text:
                    para.text = para.text.replace(key, value)
        doc.save(output_path)

    # Generate the document
    populate_credit_memo(template_path, output_path, context)
    st.success("Credit memo generated successfully.")

# Download button if file exists
output_path = f"data/{company_name}_Credit_Memo.docx"
if os.path.exists(output_path):
    with open(output_path, "rb") as file:
        st.download_button(
            label="Download Credit Memo",
            data=file,
            file_name=f"{company_name}_Credit_Memo.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
