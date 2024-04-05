# Import things that are needed generically
from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool, StructuredTool, tool
from langchain_openai.chat_models import ChatOpenAI
from config import *
from typing import Optional
from typing import Literal
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI


from typing import Optional

from langchain_core.pydantic_v1 import BaseModel, Field


class Diff(BaseModel):
    """Information about a person."""

    # ^ Doc-string for the entity Person.
    # This doc-string is sent to the LLM as the description of the schema Person,
    # and it can help to improve extraction results.

    # Note that:
    # 1. Each field is an `optional` -- this allows the model to decline to extract it!
    # 2. Each field has a `description` -- this description is used by the LLM.
    # Having a good description can help improve extraction results.
    category: Literal['Correct', 'Minor Mistake', 'Conceptual Mistake', 'Logical Mistake']

class EvalDiffInput(BaseModel):
    question: str = Field(description="Description of a math problem")
    solution: str = Field(description="Correct solution to input question")
    answer: str = Field(description="User's answer towards the question")



# @tool("Eval-Difference", args_schema=EvalDiffInput, return_direct=True)
def eval(question: str, solution:str, answer: str) -> str:
    """Evaluate user's input based on question description and correct solution"""
    prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an expert in analyzing primary school student's math mistake"
            "You will be provided with a question, the solution, and user's approach"
            "Categorize User's approach in to categories: Logical Mistake, Conceptual Mistake, Minor Mistake, Correct"
            "If multiple mistakes is inside a question, output in order of Logical Mistake, Conceptual Mistake, Minor Mistake, Correct"
            "Here is an example"
            "Question: Farmer Brown raises emus, large birds. His flock has a total of 60 heads and legs. How many emus are in his flock?"
            "Correct Answer For question: Each emu has 1+2=<<1+2=3>>3 heads and legs.\nThen the flock has 60/3=<<60/3=20>>20 animals."
            "Judge user's input based on folloing categories "
            "Correct: If the user answer the question correctly"
            "Minor Mistake: Careless trival mistake. For example, user mistakenly calculate 60/3 into 15 instead of 20. User has understand the essense of problem but making small mistake in calculation"
            "Conceptual Mistake: If the user use wrong concept or equation to solve some problem. For example, using 2*pai*r to calculate the area of a circle"
            "Logical Mistake: User's logic is completely wrong or he just don't know how to do this question. For example, user think there are 60 enum in the farm because there are 60 heads and legs"
        ),
        (
            "system","Fewshot Examples:"
            "Question: TJ ran a 10K race last Saturday. He ran the first half in 20 minutes. He completed the second half in 30 minutes. What was his average time per kilometer?"
            "Solution: He ran the 10 kilometers in a total of 20 + 30 = <<20+30=50>>50 minutes.\nTherefore, he ran at a pace of 50 minutes / 10 kilometers = <<50/10=5>>5 minutes per kilometer.\n#### 5<|endoftext|>"
            "User Input: The total time TJ ran is 20 + 30 = 50 minutes, the average time per kilometer is 10 / 50 = 0.2"
            "Output: Conceptual Error"
         ),
        # Please see the how-to about improving performance with
        # reference examples.
        # MessagesPlaceholder('examples'),
        ("system", "{question}"),
        ("system","{solution}"),
        ("human","{userInput}")
    ]
)
    model = ChatOpenAI(model=EVALUTAIONMODEL)
    runnable = prompt | model
    output = runnable.invoke({"question": question, "solution":solution, "userInput": answer})
    return output