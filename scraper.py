import os
from datetime import datetime
import requests
from requests_html import HTML
import time

cwd = os.getcwd()
now = datetime.now()
timestamps = now.strftime("%d/%m/%Y %H:%M:%S")
BASE_DIR = os.path.dirname(cwd)
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

base_url = "https://stackoverflow.com/questions/tagged/"


def clean_scraped_data(text, keyname=None):
    if keyname == "votes":
        return text.replace("\nvotes", "")
    elif keyname == "tags":
        return text.replace("\n", ", ")
    elif keyname == "summary":
        return text
    return text


def parse_tagged_page(html):
    question_summaries = html.find(".s-post-summary")

    key_names = ["question", "summary", "answers", "votes", "tags", "links"]
    classes_needed = [".s-link", ".s-post-summary--content-excerpt", ".s-post-summary--stats-item.has-answers",
                      ".s-post-summary--stats-item-number", ".tags"]
    datas = []

    for q_el in question_summaries:
        question_data = {}
        for i, cls in enumerate(classes_needed):
            keyname = key_names[i]
            question_summary_id = q_el.attrs["id"].split("-")[2]
            sub_el = q_el.find(cls, first=True)
            if keyname == "answers":
                if sub_el is None:
                    question_data["answers"] = 0
                else:
                    a_sub_el = sub_el.find(".s-post-summary--stats-item-number", first=True)
                    question_data["answers"] = a_sub_el.text
            else:
                question_data[keyname] = clean_scraped_data(sub_el.text, keyname=keyname)
                question_data["links"] = f"https://stackoverflow.com/questions/{question_summary_id}"

        datas.append(question_data)

    return datas


def extract_data_from_url(url):
    r = requests.get(url)
    if r.status_code not in range(200, 299):
        return []
    html = HTML(html=r.text)
    datas = parse_tagged_page(html)

    return datas


def scrape_tag(tag="python", query_filter="Unanswered", max_pages=1):
    datas = []

    for p in range(max_pages):
        url = f"{base_url}{tag}?tab={query_filter}&page={p + 1}"
        print(url)
        datas += extract_data_from_url(url)
        time.sleep(1.2)

    return datas


def extract_data(tags=None, max_pages=1):
    if tags is None:
        tags = ["python"]
    scraped_data = []
    for tag in tags:
        datas = scrape_tag(tag=tag, max_pages=max_pages)
        datas.insert(0, {"timestamps": timestamps})
        scraped_data = datas

    return scraped_data
