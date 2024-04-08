from langchain_core.pydantic_v1 import BaseModel, Field
from enum import Enum


class Eval_Output(BaseModel):
    """Output format for each input math word problem mistake analysis"""
    Correct:str  = Field(..., description="True if user answered correctly")
    Reading_Mistake: str = Field(..., description="True if user understand the question in a wrong way")
    Minor_Mistake: str = Field(..., description="True if Careless trival mistake. For example, user mistakenly calculate 60/3 into 15 instead of 20. User has understand the essense of problem but making small mistake in calculation")
    Conceptual_Mistake: str = Field(...,description="True if If the user use wrong concept or equation to solve some problem. For example, using 2*pai*r to calculate the area of a circle")
    Logical_Mistake: str = Field(..., description="User's logic is completely wrong or he just don't know how to do this question. For example, user think there are 60 enum in a farm because there are 60 heads and legs")
    Reasoning: str = Field(..., description="Why you categorize the user's mistake in such category")

