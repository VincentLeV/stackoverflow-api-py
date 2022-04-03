from fastapi import FastAPI
from scraper import extract_data
from data.stackoverflow_python import questions as py
from data.stackoverflow_javascript import questions as js

app = FastAPI()


@app.get("/")
def root():
    return {"hello": "world"}


@app.get("/api/python")
def get_py_questions():
    data = extract_data(tags=["python"], max_pages=1)
    return data


@app.get("/api/javascript")
def get_js_questions():
    data = extract_data(tags=["javascript"], max_pages=1)
    return data
