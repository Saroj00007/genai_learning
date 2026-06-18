import os 
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

message = [
    {
      "role" : "system" , 
      "content" : """
          you are the helpfull ai  assistant who alwyat give answer not more than 2 lines
"""
    }
]

while True:
   user_input = input("you > ")

   message.append(
      {
         "role" : "user" , 
         "content" : user_input
      }
   )

   response = client.chat.completions.create(
      model="gpt-5-nano" , 
      messages= message , 
   )

   assistant_message = response.choices[0].message.content

   message.append(
      {
         "role" : "assistant" , 
         "content" : assistant_message
      }
   )

   print("\n")
   print("assistant > " , assistant_message)
