# AI Resume Intelligence & Generation System

🔗 **Live App**: https://ai-resume-intelligence-system-3capeucupawa5uk9zoappqu.streamlit.app/  
📦 **Tech Stack**: Python, Large Language Models (OpenRouter), Streamlit, LaTeX, Web Scraping

---

## Overview

The AI Resume Intelligence & Generation System is an end-to-end, LLM-driven application that analyzes job descriptions and generates ATS-friendly resume content aligned to a target role.

Rather than fabricating work experience, the system focuses on honest, project-backed resume generation using Large Language Models with strict constraints to control hallucinations and ensure interview-defensible output.

The application is deployed using Streamlit Cloud and generates downloadable LaTeX (.tex) resumes, which can be compiled into PDFs offline.

---

## Key Features

### Job Description Ingestion
- Scrapes public company career pages (HTML text only)
- Extracts human-readable job requirements safely and legally
- Avoids restricted platforms like LinkedIn

### LLM-Based Job Analysis
- Uses an instruction-tuned LLM to analyze job descriptions
- Extracts core skills, role focus, and responsibility themes

### LLM-Based Resume Generation
- Generates resume experience bullets using structured templates
- Applies prompt constraints to prevent hallucinations
- Ensures all output is interview-defensible and code-backed

### ATS-Friendly Resume Output
- Generates LaTeX (.tex) resumes
- Cloud-safe file handling
- PDF compilation supported offline

### Deployed Web Application
- Interactive UI built with Streamlit
- Real-time resume generation
- Downloadable resume output

---

## System Architecture

User Inputs (Name, Email, Target Role)
↓
Job Description URL
↓
Web Scraper (HTML → Text)
↓
LLM #1 — JD Analysis
↓
LLM #2 — Resume Generation
↓
LaTeX Resume Rendering
↓
Downloadable .tex File


---

## How the System Runs (End-to-End)

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/ai-resume-intelligence-system.git
cd ai-resume-intelligence-system

# 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux / macOS

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set environment variables (OpenRouter)
setx OPENAI_API_KEY "your_openrouter_api_key"
setx OPENAI_BASE_URL "https://openrouter.ai/api/v1"

# 5. Run CLI version
python main.py

# OR

# 6. Run Streamlit web app
streamlit run app.py
## Output

output/
 └── resume.tex   # ATS-friendly LaTeX resume (PDF compilable offline)

