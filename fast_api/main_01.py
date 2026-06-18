from fastapi import FastAPI
from model import chat_request
from llm import (get_ai_response , get_stream_response)
from memory import messages
from memory import (
    get_message , 
    add_assistant_message , 
    add_user_message
)
import logging
from fastapi.responses import StreamingResponse

logging.basicConfig(
    level=logging.INFO , 
    format="%(asctime)s - %(levelname)s - %(message)s"
)


app = FastAPI()

@app.get("/")
async def root():
    return {
        "message" : "hi there!"
    }

@app.get("/response")
async def response(request : chat_request):
    return {
        "message" : f"hello your reqest is {request.message}"
    }

@app.get("/chat")
async def chat(request : chat_request):
    user_message = request.message

    logging.info("adding user message to memory")
    add_user_message(user_message)

    logging.info("calling the openai api")
    response =await get_ai_response(messages)

    logging.info("storing the ai message")
    add_assistant_message(response.content)

    

    return {
        "AI : " : response.content
    }

@app.get("/stream-chat")
async def stream_chat(request : chat_request):

    add_user_message(request.message)
    
    print("AI : " , await get_stream_response(messages))

    return {
        "message" : "hi there"
    }

   



