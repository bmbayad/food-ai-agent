
# #for testing purpose only##
# import os
# from pydantic import BaseModel, Field
# from langchain_openai import ChatOpenAI



# class EmailMessage(BaseModel):
#     subject :str
#     contents: str
#     invalid_request: bool = Field(default=False)



# #using os.environ
# OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
# OPENAI_BASE_URL = os.environ.get("OPENAI_BASE_URL", None)
# OPENAI_MODEL_NAME = os.environ.get("OPENAI_MODEL_NAME", "gpt-3.5-turbo")

# if not OPENAI_API_KEY:
#     raise NotImplementedError("`OPENAI_API_KEY` environment variable is not set")

# openai_parameters = {
#     "model": OPENAI_MODEL_NAME,
#     "api_key": OPENAI_API_KEY
# }

# if OPENAI_BASE_URL:
#     openai_parameters["base_url"] = OPENAI_BASE_URL
    
    

# llm_base = ChatOpenAI(**openai_parameters)

# llm = llm_base.with_structured_output(EmailMessage)

# messages = [
#     {"role": "system", "content": 
#         "You are a helpful assistant that helps to write email messages.\
#          Do not use markdown in your response, always use plain text."
#      },
#     {"role": "user", "content": 
#         "Write an email to my boss about being late to work today. \
#         Do not use markdown in your response, always use plain text."
     
#      }
# ]


# response = llm.invoke(messages)

# print(response)