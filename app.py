import streamlit as st

st.title("GenAI Credit Memo Generator")

company_name = st.text_input("Company Name")
sector = st.text_input("Sector")
loan_amount = st.number_input("Loan Amount (USD)", min_value=0.0)

uploaded_template = st.file_uploader("Upload Credit Memo Template (.docx)", type="docx")
uploaded_data = st.file_uploader("Upload Financial/Market Data", type=["txt", "csv", "pdf"])

if st.button("Generate Credit Memo"):
    st.success("Credit memo generation initiated...")
