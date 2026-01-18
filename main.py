from scraper.scrape_jd import scrape_job_description
from llm.analyze_jd import analyze_job_description
from llm.generate_resume import generate_resume_content
from latex_engine.fill_template import fill_latex, compile_pdf

print("=== AI Resume Intelligence System ===")

name = input("Enter your name: ")
email = input("Enter your email: ")
role = input("Enter target role: ")
jd_url = input("Paste job description URL: ")

jd_text = scrape_job_description(jd_url)
jd_analysis = analyze_job_description(jd_text)
experience = generate_resume_content(jd_analysis)

data = {
    "name": name,
    "email": email,
    "skills": role,
    "experience": experience
}

fill_latex(data)
# compile_pdf()  # enable if LaTeX is installed

print("Resume generated successfully.")
