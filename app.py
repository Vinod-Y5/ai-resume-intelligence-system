import streamlit as st
from scraper.scrape_jd import scrape_job_description
from llm.analyze_jd import analyze_job_description
from llm.generate_resume import generate_resume_content
from latex_engine.fill_template import fill_latex

st.set_page_config(page_title="AI Resume Intelligence System")

st.title("AI Resume Intelligence & Generation System")

st.markdown("Generate ATS-friendly resume content using LLMs.")

name = st.text_input("Name")
email = st.text_input("Email")
role = st.text_input("Target Role (e.g. Data Analyst)")
jd_url = st.text_input("Job Description URL (company career page)")

if st.button("Generate Resume"):
    if not all([name, email, role, jd_url]):
        st.error("Please fill all fields.")
    else:
        with st.spinner("Scraping job description..."):
            jd_text = scrape_job_description(jd_url)

        with st.spinner("Analyzing job description with LLM..."):
            jd_analysis = analyze_job_description(jd_text)

        with st.spinner("Generating resume content with LLM..."):
            experience = generate_resume_content(jd_analysis)

        data = {
            "name": name,
            "email": email,
            "skills": role,
            "experience": experience
        }

        fill_latex(data)

        st.success("Resume generated successfully!")

        with open("output/resume.tex", "r") as f:
            st.download_button(
                label="Download Resume (.tex)",
                data=f.read(),
                file_name="resume.tex",
                mime="text/plain"
            )
