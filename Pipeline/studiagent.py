from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.tools import tool
from langchain.agents import AgentExecutor, create_openai_tools_agent
import getpass
import os
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import ChatOpenAI
from Tools import tools

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


prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a math You are a math teacher and trying to teach student how to solve the following question",
            "{question}"
            "The solution of the question is"
            "{solution}"
            "You will be provided with userinput and chat history, identify it based on following logic"
            "If it is a question, firstly identify whether it is a question about problem provided."
            "If yes, answer the question"
            "If No , ask the user to stay concetrate."
            "If the response is an answer or user's claim on this question."
            "Invoke Eval-Difference tool which will provide you the exact instruction on how to deal with each situation"
            "If the user are illustrating their idea, only tell whether the step is correct. If yes, prompt them a little hint of next step intead of telling them the correct answer. If user is wrong, provide them hint about how to solve the current step. "
            "If users are stuck, provide them a hint on the next step they are stuck at"
            "Other than that, tell the user to concentrate"
        ),
        MessagesPlaceholder(variable_name="messages"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

tool_list = [tools.eval]
agent = create_openai_tools_agent(model, tools, prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)