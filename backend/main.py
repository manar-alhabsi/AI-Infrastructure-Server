from fastapi import FastAPI
from pydantic import BaseModel
from ollama import Client

client = Client(host="http://ollama:11434")

app = FastAPI(
    title="AI Infrastructure Server",
    version="1.0.0"
)


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def root():
    return {
        "status": "running",
        "project": "AI Infrastructure Server"
    }


@app.post("/chat")
def chat_with_ai(request: ChatRequest):
    response = client.chat(
        model="gemma3:latest",
        messages=[
            {
                "role": "user",
                "content": request.message
            }
        ]
    )

    return {
        "reply": response["message"]["content"]
    }
