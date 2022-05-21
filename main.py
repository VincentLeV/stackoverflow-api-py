from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from scraper import extract_data
# from data.stackoverflow_python import questions as py
# from data.stackoverflow_javascript import questions as js

app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "Information": {
            "API URL Prefix": "/api",
            "Endpoints": "Any available stackoverflow tag should work",
            "Timestamp": "GMT+2 Timezone"
        }
    }


# @app.get("/api/python")
# def get_py_questions():
#     data = extract_data(tags=["python"], max_pages=1)
#     return data
#
#
# @app.get("/api/javascript")
# def get_js_questions():
#     data = extract_data(tags=["javascript"], max_pages=1)
#     return data

@app.get("/api/{language}")
def get_questions(language: str):
    data = extract_data(tags=[language], max_pages=1)
    return data
