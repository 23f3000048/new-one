from fastapi import FastAPI, Query # type: ignore
from fastapi.responses import JSONResponse # type: ignore
from fastapi.middleware.cors import CORSMiddleware # type: ignore
import json
import os

app = FastAPI()

# Enable CORS for all origins and GET method
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load the data once at startup
with open(os.path.join(os.path.dirname(__file__), "q-vercel-python.json")) as f:
    data = json.load(f)

# Create a name-to-marks mapping for quick lookup
name_to_marks = {entry["name"]: entry["marks"] for entry in data}

@app.get("/api")
async def get_marks(name: list[str] = Query(...)):
    marks = [name_to_marks.get(n, None) for n in name]
    return JSONResponse(content={"marks": marks})
