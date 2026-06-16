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

assemblies = {
    "screw-jack": {
        "title": "Screw Jack",
        "github_url": "https://github.com/mohanevs/solid-modeling-catia-v6/tree/main/Assembly/1.screw%20jack",
        "description": "A mechanical device used to lift heavy loads by applying a small force. Converts rotary motion into linear motion through a screw mechanism.",
        "image": "resources/Assembly/1. Screw Jack/screw jack assmbled.png",
        "components": [
            {"name": "Body", "image": "resources/Assembly/1. Screw Jack/body.png"},
            {"name": "Cup", "image": "resources/Assembly/1. Screw Jack/cup.png"},
            {"name": "Nut", "image": "resources/Assembly/1. Screw Jack/nut.png"},
            {"name": "Screw", "image": "resources/Assembly/1. Screw Jack/screw.png"},
            {"name": "Screw Spindle", "image": "resources/Assembly/1. Screw Jack/screwSpindle.png"},
            {"name": "Tommy Bar", "image": "resources/Assembly/1. Screw Jack/tommyBar.png"},
            {"name": "Washer", "image": "resources/Assembly/1. Screw Jack/washer.png"},
        ]
    },
    "knuckle-joint": {
        "title": "Knuckle Joint",
        "github_url": "https://github.com/mohanevs/solid-modeling-catia-v6/tree/main/Assembly/2.knuckle%20joint",
        "description": "A pin-based mechanical joint that connects two rods end-to-end, allowing angular movement in one plane.",
        "image": "resources/Assembly/2. Knuckle Joint/knuckle joint assembled.png",
        "components": [
            {"name": "Collar", "image": "resources/Assembly/2. Knuckle Joint/collar.png"},
            {"name": "Eye End", "image": "resources/Assembly/2. Knuckle Joint/eye end.png"},
            {"name": "Fork End", "image": "resources/Assembly/2. Knuckle Joint/fork end.png"},
            {"name": "Pin", "image": "resources/Assembly/2. Knuckle Joint/pin.png"},
            {"name": "Taper Pin", "image": "resources/Assembly/2. Knuckle Joint/taper pin.png"},
        ]
    },
    "pipe-vice": {
        "title": "Pipe Vice",
        "github_url": "https://github.com/mohanevs/solid-modeling-catia-v6/tree/main/Assembly/3.pipe%20vice",
        "description": "A clamping tool used to hold cylindrical pipes securely during cutting, threading, or bending operations.",
        "image": "resources/Assembly/3. Pipe Vice/pipe vice assembled.png",
        "components": [
            {"name": "Base", "image": "resources/Assembly/3. Pipe Vice/base.png"},
            {"name": "Handle Screw", "image": "resources/Assembly/3. Pipe Vice/handle screw.png"},
            {"name": "Handle", "image": "resources/Assembly/3. Pipe Vice/handle.png"},
            {"name": "Movable Jaw", "image": "resources/Assembly/3. Pipe Vice/movable jaw.png"},
            {"name": "Screw", "image": "resources/Assembly/3. Pipe Vice/screw.png"},
        ]
    },
    "plummer-block": {
        "title": "Plummer Block",
        "github_url": "https://github.com/mohanevs/solid-modeling-catia-v6/tree/main/Assembly/4.plummer%20block",
        "description": "A pedestal bearing housing that supports a rotating shaft, absorbing radial and axial loads.",
        "image": "resources/Assembly/4. Plummer Block/plummer block assembled.png",
        "components": [
            {"name": "Bolt", "image": "resources/Assembly/4. Plummer Block/bolt.png"},
            {"name": "Brasses", "image": "resources/Assembly/4. Plummer Block/brasses.png"},
            {"name": "Cap", "image": "resources/Assembly/4. Plummer Block/cap.png"},
            {"name": "Casting", "image": "resources/Assembly/4. Plummer Block/casting.png"},
            {"name": "Lock Nut", "image": "resources/Assembly/4. Plummer Block/lock nut.png"},
            {"name": "Nut", "image": "resources/Assembly/4. Plummer Block/nut.png"},
        ]
    },
    "press-tool": {
        "title": "Press Tool",
        "github_url": "https://github.com/mohanevs/solid-modeling-catia-v6/tree/main/Assembly/5.press%20tool",
        "description": "A precision tool used in sheet metal operations to cut, bend, or form metal sheets using a press machine.",
        "image": "resources/Assembly/5. Press Tool/@press tool assembled.png",
        "components": [
            {"name": "Bottom Plate", "image": "resources/Assembly/5. Press Tool/bottom plate.png"},
            {"name": "Guide Bush", "image": "resources/Assembly/5. Press Tool/guide bush.png"},
            {"name": "Guide Pillar", "image": "resources/Assembly/5. Press Tool/guide pillar.png"},
            {"name": "Top Plate", "image": "resources/Assembly/5. Press Tool/top Plate.png"},
        ]
    },
    "tool-head-of-shaper": {
        "title": "Tool Head of Shaper",
        "github_url": "https://github.com/mohanevs/solid-modeling-catia-v6/tree/main/Assembly/6.tool%20head%20of%20shaper",
        "description": "The cutting tool holding mechanism of a shaper machine, allowing angular adjustment for precise machining.",
        "image": "resources/Assembly/6. Tool Head of Shaper/@tool head of shaper assembled.png",
        "components": [
            {"name": "Back Plate", "image": "resources/Assembly/6. Tool Head of Shaper/back plate.png"},
            {"name": "Bush Washer", "image": "resources/Assembly/6. Tool Head of Shaper/bush washer.png"},
            {"name": "Clamping Screw", "image": "resources/Assembly/6. Tool Head of Shaper/clamping screw.png"},
            {"name": "Drag Plate", "image": "resources/Assembly/6. Tool Head of Shaper/drag plate.png"},
            {"name": "Handle", "image": "resources/Assembly/6. Tool Head of Shaper/handle.png"},
            {"name": "Handle Br", "image": "resources/Assembly/6. Tool Head of Shaper/handle br.png"},
            {"name": "Nut", "image": "resources/Assembly/6. Tool Head of Shaper/nut.png"},
            {"name": "Pivot Pin", "image": "resources/Assembly/6. Tool Head of Shaper/pivot pin.png"},
            {"name": "Small Washer", "image": "resources/Assembly/6. Tool Head of Shaper/small washer.png"},
            {"name": "Space Bush", "image": "resources/Assembly/6. Tool Head of Shaper/space bush.png"},
            {"name": "Swivel Plate", "image": "resources/Assembly/6. Tool Head of Shaper/swivel plate.png"},
            {"name": "Swivel Screw Pin", "image": "resources/Assembly/6. Tool Head of Shaper/swivel screw pin.png"},
            {"name": "Tool Fixing Screw", "image": "resources/Assembly/6. Tool Head of Shaper/tool fixing screw.png"},
            {"name": "Tool Holder", "image": "resources/Assembly/6. Tool Head of Shaper/tool holder.png"},
            {"name": "Vertical Slide", "image": "resources/Assembly/6. Tool Head of Shaper/vertical slide.png"},
            {"name": "Washer", "image": "resources/Assembly/6. Tool Head of Shaper/washer.png"},
        ]
    },
    "motor-blower": {
        "title": "Motor Blower",
        "github_url": "https://github.com/mohanevs/solid-modeling-catia-v6/tree/main/Assembly/7.motor%20blower",
        "description": "A motor-driven blower assembly used to circulate air in cooling or ventilation systems.",
        "image": "resources/Assembly/7. Motor Blower/@motor blower assemled.png",
        "components": [
            {"name": "Blower", "image": "resources/Assembly/7. Motor Blower/blower.png"},
            {"name": "Cover", "image": "resources/Assembly/7. Motor Blower/cover.png"},
            {"name": "Lower Housing", "image": "resources/Assembly/7. Motor Blower/lower housing.png"},
            {"name": "Motor", "image": "resources/Assembly/7. Motor Blower/motor.png"},
            {"name": "Shaft", "image": "resources/Assembly/7. Motor Blower/shaft.png"},
            {"name": "Upper Housing", "image": "resources/Assembly/7. Motor Blower/upper housing.png"},
        ]
    },
}

@app.get("/details/{slug}", response_class=HTMLResponse)
async def details(request: Request, slug: str):
    assembly = assemblies.get(slug)
    if not assembly:
        return HTMLResponse(content="Not found", status_code=404)
    return templates.TemplateResponse("details.html", {
        "request": request,
        "assembly": assembly
    })