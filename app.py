import os
import streamlit as st
import PyPDF2
from docx import Document
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

def extract_text_from_pdf(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_text_from_docx(uploaded_file):
    doc = Document(uploaded_file)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_skills(text):
    prompt = f"""
    Act as a HR manager. Extract technical and professional skills from this text.
    Return only a comma-separated list of skills:
    
    {text}
    """
    response = model.generate_content(prompt)
    return response.text if response else ""

def determine_designation(skills):
    prompt = f"""
    As a senior HR specialist, suggest the three most suitable job designations for these skills:
    {skills}
    Return only three job titles, separated by commas.
    """
    response = model.generate_content(prompt)
    return response.text.strip() if response else ""

# Streamlit UI
st.title("Resume to Job Title")
uploaded_file = st.file_uploader("Upload Resume (PDF or DOCX)", type=["pdf", "docx"])

if uploaded_file:
    try:
        # Extract text
        file_type = uploaded_file.name.split('.')[-1]
        if file_type == 'pdf':
            text = extract_text_from_pdf(uploaded_file)
        elif file_type == 'docx':
            text = extract_text_from_docx(uploaded_file)
        else:
            st.error("Unsupported file format")
            st.stop()

        # Process with Gemini
        with st.spinner("Analyzing resume..."):
            skills = extract_skills(text)
            if not skills:
                st.error("Failed to extract skills")
                st.stop()
                
            designation = determine_designation(skills)
        
        st.subheader("Suggested Job Titles to Apply:")
        for job in designation.split(","):
            st.success(job.strip())


    except Exception as e:
        st.error(f"Error processing file: {str(e)}")