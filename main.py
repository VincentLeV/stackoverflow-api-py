from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from scraper import extract_data

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {
        "Information": {
            "API URL Prefix": "/api",
            "Endpoints": "Any available stackoverflow tag should work",
            "Examples": {
                "Python": "/api/python",
                "JavaScript": "/api/javascript",
                "ReactJS": "/api/reactjs",
                "C#": "/api/csharp",
                "C++": "/api/c++",
                "Go": "/api/go",
            },
            "Timestamp": "GMT+2 Timezone"
        }
    }

@app.get("/api/{language}")
async def get_questions(language: str):
    data = extract_data(tags=[language], max_pages=1)
    return data
