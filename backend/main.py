from fastapi import FastAPI

app = FastAPI(title="Sangturiya Backend API")

@app.get("/")
def read_root():
    return {"message": "Welcome to Sangturiya Backend API"}
