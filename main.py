# import libs
from fastapi import FastAPI, Query
from BmiCalc import calculate_bmi
from fastapi.middleware.cors import CORSMiddleware

# create app fro api
app = FastAPI()
app.add_middleware(CORSMiddleware,
    allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)

# Define the main path
@app.get("/")

# Define the function for a previous path
def Hi():
    return {"message": "Marhaba Python"}

# Define new path
@app.get("/calculate_bmi")

def bmi_endpoint(
    weight: float = Query(..., gt=20, lt=200, description="the weight in kilograms"),
    height: float = Query(..., gt=1, lt=3, description="the height in metres")
    ):
    return calculate_bmi(weight, height)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)