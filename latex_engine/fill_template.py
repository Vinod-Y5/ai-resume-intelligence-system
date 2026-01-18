from jinja2 import Template
import subprocess

def fill_latex(data):
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
