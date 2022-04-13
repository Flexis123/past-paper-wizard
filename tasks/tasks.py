from databse import Examination, Subject
from requests_html import HTMLSession, HTMLResponse
from main import db


def update_subjects(ex: Examination):
    url = "https://www.cambridgeinternational.org/programmes-and-qualifications/"
    url += "cambridge-upper-secondary/cambridge-igcse/subjects/" if ex == Examination.IGCSE else \
        "cambridge-advanced/cambridge-international-as-and-a-levels/subjects/"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    }

    res: HTMLResponse = HTMLSession().get(url, headers= headers)
    res.raise_for_status()

    for subject in res.html.find("ul.emphasized-link li a"):
        subject_code = ""

        name_end = 0
        i = 0
        for char in subject.text:
            if char.isdigit() and len(subject_code) < 4:
                subject_code += char
                if len(subject_code) == 4:
                    name_end = i - 4
                    break
            else:
                subject_code = ""

            i += 1

        subject_obj = Subject(subject.text[0: name_end], subject_code)
        db.session.add(subject_obj)
        db.session.commit()



update_subjects(Examination.IGCSE)
