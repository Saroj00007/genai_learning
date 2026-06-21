#  just conversation history nothing else

messages = [
    {
        "role": "system",
        "content": """
        You are an autism support assistant.
        """
    }
]

def add_user_message(user_message):
    
    messages.append({
        "role" : "user" , 
        "content" : user_message
    })

def add_assistant_message(assistant_message):
    
    messages.append({
        "role" : "assistant" , 
        "content" : assistant_message
    })

def get_message():
    return messages