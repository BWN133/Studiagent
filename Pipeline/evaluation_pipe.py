from langchain_openai.chat_models import ChatOpenAI
from langchain_core.tools import tool
import getpass
import os

from dotenv import load_dotenv
load_dotenv()
# os.environ["OPENAI_API_KEY"] = getpass.getpass()

# If you'd like to use LangSmith, uncomment the below
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()
model = ChatOpenAI(model="gpt-3.5-turbo-1106")


@tool
def print_message(first_int: int, second_int: int):
    """Print message. hahah you bitch"""
    print(first_int,second_int)


print(print_message.name)
print(print_message.description)
print(print_message.args)

print_message.invoke({"first_int": 4, "second_int": 5})
