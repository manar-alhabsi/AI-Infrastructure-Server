from fastapi import FastAPI

app = FastAPI(
    title="AI Infrastructure Server",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "status": "running",
        "project": "AI Infrastructure Server"
    }
