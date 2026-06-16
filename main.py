from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import json

BASE_DIR = Path(__file__).resolve().parent
PUBLIC_DIR = BASE_DIR
RESOURCE_DIR = BASE_DIR / "resources"

app = FastAPI()

app.mount("/static", StaticFiles(directory=PUBLIC_DIR / "static"), name="static")
app.mount("/images", StaticFiles(directory=PUBLIC_DIR / "images"), name="images")
app.mount("/resources", StaticFiles(directory=RESOURCE_DIR), name="resources")

templates = Jinja2Templates(directory=PUBLIC_DIR / "templates")

@app.get("/",response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html",{"request": request})

@app.get("/search", response_class=HTMLResponse)
async def search(request: Request):
    data_path = BASE_DIR / "data.json"
    with open(data_path, encoding="utf-8") as f:
        items = json.load(f)
    return templates.TemplateResponse("search.html", {"request": request, "items": items})