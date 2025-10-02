from dotenv import load_dotenv
load_dotenv()

from langchain_openai import OpenAI
model = OpenAI(model='gpt-3.5-turbo-instruct' ,temperature=0.7)
prompt = 'The sky is'
completion = model.invoke(prompt) 
print(completion)