# Resume Analyzer: Resume to Job Title

A Streamlit web application that analyzes resumes (PDF or DOCX) to extract skills and suggest three relevant job titles using Google's Gemini AI.

## Features

- **Resume Upload**: Supports PDF and DOCX file formats.
- **Text Extraction**: Extracts text content from uploaded resumes.
- **Skill Extraction**: Uses Gemini AI to identify technical/professional skills.
- **Job Title Suggestions**: Recommends three suitable job titles based on extracted skills.

## Installation

1. **Clone the repository**
   ```bash
   git clone [https://github.com/Babaji-B/resume-classification-using-GenAI.git]
   cd resume-analyzer


2. **Install dependencies**
    ```
    pip install streamlit PyPDF2 python-docx google-generativeai python-dotenv
    ```

3. **Set up environment variables**
    ```
    #Create .env file
    GEMINI_API_KEY=your_api_key_here
    Get API key from Google AI Studio
    ```

# How It Works
**File Upload:** User uploads resume through Streamlit interface

# Text Extraction
**PDF:** Uses PyPDF2 for text extraction
**DOCX:** Uses python-docx for text extraction


# AI Processing
First prompt extracts skills from resume text
Second prompt suggests job titles based on skills


**Results Display:** Shows three suggested job titles in the UI

