from openai import OpenAI

client = OpenAI(base_url="https://openrouter.ai/api/v1")

BULLET_TEMPLATES = [
    "Implemented an NLP-based pipeline to extract relevant skills from job descriptions using Python.",
    "Integrated a Large Language Model (LLM) to generate structured resume content based on extracted requirements.",
    "Designed prompt constraints to reduce hallucinations and ensure interview-defensible outputs.",
    "Automated resume generation using LaTeX templates to produce ATS-friendly documents.",
    "Built an end-to-end pipeline connecting data ingestion, LLM analysis, generation, and document rendering."
]

def generate_resume_content(jd_analysis):
    prompt = f"""
Select 4–5 bullet points from the list below.
Do NOT invent or modify content.

Bullet options:
{chr(10).join(BULLET_TEMPLATES)}
"""

    response = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0
    )

    return response.choices[0].message.content
