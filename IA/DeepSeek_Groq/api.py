from fastapi import FastAPI
from pydantic import BaseModel
from langchain_groq import ChatGroq
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

llm = ChatGroq(model="openai/gpt-oss-120b")
app = FastAPI()

messages = []

class MessageRequest(BaseModel):
    message: str


@app.post("/chat")
async def chat_with_ai(request: MessageRequest):
    messages.append(("human", request.message))
    response = llm.invoke(messages).content
    messages.append(("ai", response))
    return {"response": response}

@app.get("/messages")
async def get_messages():
    return {"messages": [{"type": msg[0], "content": msg[1]} for msg in messages]}