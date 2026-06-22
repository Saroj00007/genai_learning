documents = [
    "Many autistic children experience auditory sensitivity.",
    "Speech therapy can improve communication skills.",
    "Visual schedules help establish routines."
]

from one import client

import math
def dot_product(a, b):
    total = 0

    for x,y in zip(a, b):
        total += x*y

    print(total)
    return total

def magnitude(vector):
    total = 0

    for value in vector :
        total  += value**2
    
    print(math.sqrt(total))
    return math.sqrt(total)


def cosine_similariyt(a , b):

    dotproduct = dot_product(a , b)

    magnitudeA =magnitude(a) 
    magnitudeB = magnitude(b)

    return ((dotproduct) / (magnitudeA * magnitudeB))



def get_embeddings(text : str):
    
    embeddings = client.embeddings.create(
        model= "text-embedding-3-small" , 
        input = text
    )

    return embeddings.data[0].embedding


document_vector = []

for document in documents : 

    doc_embedding = get_embeddings(document)

    document_vector.append({
        "text" : document , 
        "embedding" : doc_embedding
    })

user_input = input("> ")
query_embedding = get_embeddings(user_input)

score = []


for document in document_vector : 

    docs_score = cosine_similariyt(document["embedding"]  , query_embedding)

    score.append({
        "text" : document["text"] , 
        "score" : docs_score
    })

score.sort(
    key=lambda x: x["score"],
    reverse=True
)

best_documents = score[0]

print(best_documents)