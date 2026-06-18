from openai import OpenAI ;
import os 
from dotenv import load_dotenv

import logging

load_dotenv()

logging.basicConfig(
    level= logging.INFO
)

client = OpenAI(api_key= os.getenv("OPENAI_API_KEY"))


while True:

    try:
        logging.info("calling the open ai and staring chat")
        user_input = input("you: ");

        

        response = client.chat.completions.create(
        model= "gpt-5-nano" , 
        messages=  [
            {"role" : "system" , "content" : "you are an help full ai assistance who give short and sweet answer"} , 
            {"role" : "user" , "content": user_input}
        ] , 
        stream = True
        )
        print("\n")
        print("assitant ==> " , end="")
        for chunk in response : 
            print(chunk.choices[0].delta.content , end="")
        
    except Exception as e: 
        print("error  " , e)

# just remember that llm are stateless and we must provide it the context