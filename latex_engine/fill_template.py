from jinja2 import Template
import subprocess
import os

def fill_latex(data):
    # Ensure output directory exists (important for Streamlit Cloud)
    os.makedirs("output", exist_ok=True)

    with open("latex_engine/template.tex") as f:
        template = Template(f.read())

    filled = template.render(
        name=data["name"],
        email=data["email"],
        skills=data["skills"],
        experience=data["experience"]
    )

    with open("output/resume.tex", "w") as f:
        f.write(filled)

def compile_pdf():
    subprocess.run(
        ["pdflatex", "-output-directory=output", "output/resume.tex"],
        check=True
    )
