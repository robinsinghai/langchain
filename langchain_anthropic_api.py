from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model_name="claude-3-5-sonnet-20241022", timeout=None, stop=None)
result = model.invoke("Write a sonnet about the sea.")
print(result.content)