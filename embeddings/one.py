from openai import OpenAI
import os 
from dotenv import load_dotenv

load_dotenv()

api_key  = os.getenv("OPENAI_API_KEY")


client = OpenAI(api_key= api_key)

dog_embedding = client.embeddings.create(
    model= "text-embedding-3-small" , 
    input= "dog"
)

pyppy_embedding = client.embeddings.create(
    model= "text-embedding-3-small" , 
    input= "puppy"
)

print(dog_embedding.data[0].embedding[:5])
print(pyppy_embedding.data[0].embedding[:5])

