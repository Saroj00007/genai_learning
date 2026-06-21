from config import OPENAI_API_KEY
from openai import OpenAI
from openai import AsyncOpenAI

client = AsyncOpenAI(api_key=OPENAI_API_KEY)

async def get_ai_response(message):

    response = await client.chat.completions.create(
        model = "gpt-5-nano" , 
        messages= message 
    )

    return response.choices[0].message

async def get_stream_response(message):

   streams = await client.chat.completions.create(
        model = "gpt-5-nano" , 
        messages= message , 
        stream= True
    )
   
   async for chunk in streams:
       content = chunk.choices[0].delta.content

       if content : 
           yield content
