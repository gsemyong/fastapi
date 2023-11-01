from fastapi import FastAPI
from pydantic import BaseModel

from yt_dlp import YoutubeDL

URLS = ["https://www.youtube.com/watch?v=BaW_jenozKc"]

app = FastAPI()


class Msg(BaseModel):
    url: str


@app.post("/")
async def root(inp: Msg):
    with YoutubeDL() as ydl:
        ydl.download(inp.url)

    return {"message": "Hello World. Welcome to FastAPI!"}


@app.get("/path")
async def demo_get():
    return {
        "message": "This is /path endpoint, use a post request to transform the text to uppercase"
    }


@app.post("/path")
async def demo_post(inp: Msg):
    return {"message": inp.msg.upper()}


@app.get("/path/{path_id}")
async def demo_get_path_id(path_id: int):
    return {
        "message": f"This is /path/{path_id} endpoint, use post request to retrieve result"
    }
