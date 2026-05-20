from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"massage":"Hello Fast API"}







