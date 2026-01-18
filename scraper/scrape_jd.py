import requests
from bs4 import BeautifulSoup

def scrape_job_description(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    elements = soup.find_all(["p", "li"])

    jd_text = "\n".join(e.get_text(strip=True) for e in elements)
    return jd_text
