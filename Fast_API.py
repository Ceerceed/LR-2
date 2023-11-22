from fastapi import FastAPI
from pydantic import BaseModel
import wikipedia

app = FastAPI()
wikipedia.set_lang("ru")

class search_from_wiki(BaseModel):
    object: str
    results: int

@app.get("/search/{object}")
async def search_wiki(object1: str, r: int = 3):
    return wikipedia.search(object1, r)

@app.get("/summary/{object}")
async def summary_wiki(object: str):
    return wikipedia.summary(object)

@app.post("/search_wiki")
async def search_wikipedia(s: search_from_wiki):
    return wikipedia.search(s.object, results = s.results)

