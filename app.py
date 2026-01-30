from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from tools.converter import Converter
import os
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI(title="Selenium to Playwright Converter")

# Enable CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

converter_tool = Converter()

class ConversionRequest(BaseModel):
    source_code: str
    target_lang: str = "typescript"

class ConversionResponse(BaseModel):
    converted_code: str
    status: str

@app.post("/convert", response_model=ConversionResponse)
async def convert_code(request: ConversionRequest):
    try:
        converted = converter_tool.convert(request.source_code, request.target_lang)
        
        # Save to .tmp/output/ for record
        os.makedirs(".tmp/output", exist_ok=True)
        filename = f"conversion_{os.urandom(4).hex()}.{ 'ts' if request.target_lang == 'typescript' else 'js' }"
        filepath = os.path.join(".tmp/output", filename)
        with open(filepath, "w") as f:
            f.write(converted)
            
        return ConversionResponse(converted_code=converted, status="success")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def read_index():
    return FileResponse("static/index.html")

# Mount static directory to serve CSS and JS
app.mount("/static", StaticFiles(directory="static"), name="static")

# Create static directory if not exists
os.makedirs("static", exist_ok=True)
