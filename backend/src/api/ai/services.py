
from api.ai.llms import get_openai_llm
from api.ai.schemas import EmailMessageSchema

def generate_email_message(query:str) -> EmailMessageSchema:
    llm = get_openai_llm()
    llm  = llm.with_structured_output(EmailMessageSchema)

    messages = [
        {"role": "system", "content": 
            "You are a helpful assistant that helps to write email messages.\
            Do not use markdown in your response, always use plain text."
        },
        {"role": "user", "content": 
            f"{query}. \
            Do not use markdown in your response, always use plain text."
        
        }
    ]
    
    return llm.invoke(messages)
    