from fastapi import FastAPI

from routes import chat

app = FastAPI()

app.include_router(chat.router)

@app.get('/')
def hello_world():
    return "Hello World!"