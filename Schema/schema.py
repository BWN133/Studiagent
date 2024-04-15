from langchain_core.pydantic_v1 import BaseModel, Field
from enum import Enum
from typing import Optional

class Eval_Output(BaseModel):
    """Output format for each input math word problem mistake analysis"""
    Correct:str  = Field(..., description="True if user answered correctly")
    Minor_Mistake: Optional[str] = Field(..., description="True if Careless trival mistake. For example, user mistakenly calculate 60/3 into 15 instead of 20. User has understand the essense of problem but making small mistake in calculation")
    Conceptual_Mistake: Optional[str] = Field(...,description="True if If the user use wrong concept or equation to solve some problem. For example, using 2*pai*r to calculate the area of a circle")
    Logical_Mistake: Optional[str] = Field(..., description="User's logic is completely wrong or he just don't know how to do this question. For example, user think there are 60 enum in a farm because there are 60 heads and legs")
    Reasoning: str = Field(..., description="Why you categorize the user's mistake in such category")



class EvalDiffInput(BaseModel):
    question: str = Field(description="Description of a math problem")
    solution: str = Field(description="Correct solution to input question")
    answer: str = Field(description="User's answer towards the question")

class EvalCompInput(BaseModel):
    question: str = Field(description="Description of a math problem")
    answer: str = Field(description="User's answer towards the question")

class EvalCompletion(BaseModel):
        if_answer: str = Field(..., description="True if it is an answer for the question")
        incomplete: str = Field(..., description="True if the answer has either the process or the result but not both.")
        complete: str = Field(..., description="True if the answer includes both the solving process and the final result.")
        input_type: str = Field(..., description="Which input type? Complete, incomplete? If in complete, only has result or process?")

