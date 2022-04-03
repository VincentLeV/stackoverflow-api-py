from fastapi import FastAPI
from data.stackoverflow_python import questions as py
from data.stackoverflow_javascript import questions as js


app = FastAPI()


@app.get("/")
def root():
    return {"hello": "world"}


@app.get("/api/python")
def get_py_questions():
    return py


@app.get("/api/javascript")
def get_js_questions():
    return js
