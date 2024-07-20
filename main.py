from fastapi import FastAPI, Query, Request
from BmiCalc import calculate_bmi
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# create app for API
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# perp folder directory
templates = Jinja2Templates(directory="templates")

# Define the main path
@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Define new path
@app.get("/calculate_bmi")
def bmi_endpoint(
    weight: float = Query(..., gt=20, lt=200, description="the weight in kilograms"),
    height: float = Query(..., gt=1, lt=3, description="the height in metres")
):
    return calculate_bmi(weight, height)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)