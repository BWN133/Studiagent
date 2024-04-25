from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import AgentExecutor, create_openai_tools_agent
import getpass
import os
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.tools.base import StructuredTool
from langchain_openai import ChatOpenAI
from Tools import toolset
from Schema import schema
from langchain.memory import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from config import *
from dotenv import load_dotenv
load_dotenv()
model = ChatOpenAI(model = GPT4)
def create_simple_agent():
    # Initialize the model
    
    # Define the prompt template
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a math teacher and trying to teach students how to solve the following question. "
                "Remember, you will never directly tell students the answer unless they figure it out themselves."
                "{question}"
                "The solution of the question is"
                "{solution}"
                "You will be provided with user input and chat history. "
                "Firstly, decide if the input is a question, a partial answer, a complete answer, or others. "
                "If it is a question, identify whether it is about the problem provided. "
                "If yes, answer the question. "
                "If no, ask the user to stay concentrated. "
                "If a partial answer, only confirm whether the step is correct. If yes, provide a hint of the next step instead of the correct answer. If wrong, provide a hint about how to solve the current step. "
                "If the response is a complete answer, first judge whether the answer is correct, If yes, congrats the user"
                "if not correct check whether user made some small mistake. For example, user mistakenly calculate 60/3 into 15 instead of 20. User has understand the essense of problem but making small mistake in calculation if so, correct the user  "
                "if not minor mistake, check whether user made conceptual mistake that user use wrong concept or equation to solve some problem. For example, using 2*pai*r to calculate the area of a circle "
                "if Yes Correct user's misunderstanding and ask the user to do the task again"
                "if not concptual mistake, check whether user made logical mistake, where User's logic is completely wrong or he just don't know how to do this question."
                "if yes, provide hint to help user correct their mistake. Don't directly tell user the answer"
                "if not mistake mention above, respond accordingly. Just don't tell the user answer"
                "Other than that, chat normally as long as it is related to the problem and don't directly output the question."
            ),
            MessagesPlaceholder(variable_name="messages"),
        ]
    )
    
    pipeline = prompt | model 

    return pipeline



def initialize_main_agent() -> RunnableWithMessageHistory:
    # model = ChatOpenAI(model="gpt-3.5-turbo-1106")

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system"
                "You are a math You are a math teacher and trying to teach student how to solve the following question"
                "Remenber, you will never directly tell student the answer unless student figure it out themselves"
                "{question}"
                "The solution of the question is"
                "{solution}"
                "You will be provided with userinput and chat history"
                "Firstly, Decide if the input is a question, a partial answer, a complete answer, or others."
                "If it is a question, firstly identify whether it is a question about problem provided."
                "If yes, answer the question"
                "If No , ask the user to stay concetrate."
                "If a partial answer, only tell whether the step is correct. If yes, prompt them a little hint of next step intead of telling them the correct answer. If user is wrong, provide them hint about how to solve the current step. "
                "If the response is an complete answer."
                "Invoke answer_analyzer tool which will provide you the exact instruction on how to deal with each situation"
                "Other than that, Chat normally as long as it is related to the problem and don't directly output the question"
            ),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ]
    )


    answerAnalyzer = StructuredTool.from_function(
        func=toolset.answer_analysis_tool_wrapper,
        name="answer_analyzer",
        description="Only Trigger this when user provides you a complete answer including result to a question. Evaluate user's input based on question description and correct solution and provide instruction on how to guide student",
        args_schema=schema.EvalDiffInput
    )
    tool_list = [answerAnalyzer]


    agent = create_openai_tools_agent(model, tool_list, prompt)

    agent_executor = AgentExecutor(agent=agent, tools=tool_list, verbose=True)

    demo_ephemeral_chat_history_for_chain = ChatMessageHistory()

    conversational_agent_executor = RunnableWithMessageHistory(
        agent_executor,
        lambda session_id: demo_ephemeral_chat_history_for_chain,
        input_messages_key="input",
        output_messages_key="output",
        history_messages_key="chat_history",
    )
    return conversational_agent_executor


    # conversational_agent_executor.invoke(
    # {
    #     "input": "Okay so I guess the cost is 40 percent of p which is (40/100)*p = 2p/5? am I correct?",
    #     "question": SAMPLEQUESTION1,
    #     "solution": SAMPLESOLUTION1
    # },
    # {"configurable": {"session_id": "unused"}},
    # )


