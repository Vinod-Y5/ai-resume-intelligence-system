from openai import OpenAI

client = OpenAI(base_url="https://openrouter.ai/api/v1")

def analyze_job_description(jd_text):
    prompt = f"""
Analyze the following job description.

Extract:
- Core technical skills
- Main responsibilities
- Role focus

Return concise bullet points only.

Job Description:
{jd_text}
"""

    response = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content
