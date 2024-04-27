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
from langchain.output_parsers import PydanticOutputParser
from Schema import schema
from util import util
import json
from langchain_core.pydantic_v1 import BaseModel, Field

def eval_completion(question: str, answer: str) -> str:
    """Evaluate if a student's answer is complete, incomplete, or absent."""
    parser = PydanticOutputParser(pydantic_object=schema.EvalCompletion)
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "You are a teacher evaluating a student's written answer to a question."
                "You will be provided with a question and user's approach"
                "Determine if the student's answer is complete, incomplete, or absent."
                "A complete answer includes both the solving process and the final result."
                "An incomplete answer has either the process or the result but not both."
                "An absent answer has neither the process nor the result."
                "Output a dictionary indicating your judgement"
                "Here is the input question: {question}"
                "Here is the student's answer to the question: {userInput}"
                "Please provide your evaluation."
                "Here are Few shot Examples:"
                "{examples}"
            )
        ]
    ).partial(format_instructions=parser.get_format_instructions())
    # Build fewshot example
    example1 = util.build_judge_example("TJ ran a 10K race last Saturday. He ran the first half in 20 minutes. He completed the second half in 30 minutes. What was his average time per kilometer?",
                                        "TJ ate apple for lunch Saturday",
                                        "True","False","False","False"
                                         )
    example2 = util.build_judge_example("Tina makes $18.00 an hour.  If she works more than 8 hours per shift, she is eligible for overtime, which is paid by your hourly wage + 1/2 your hourly wage.  If she works 10 hours every day for 5 days, how much money does she make?",
                                        "She work 5 days 10 hours so she made 5 * 8 = 40 hours in time and 5 * (10 - 8) = 10 hours overtime",
                                        "False", "False", "True", "True"
                                        )
    examples = str([example1, example2])
    model = ChatOpenAI(model=EVALUTAIONMODEL)
    runnable = prompt | model | parser
    output = runnable.invoke({"question": question, "userInput": answer,"examples":examples})
    print(output)
    return output

# def error_resistance_Compare_Output_parser(msg: AIMessage,config: RunnableConfig):
#     try:
#         return Compare_Output_parser.invoke(msg, config=config)
#     except Exception as e:
#         raise e
def exception_to_messages(inputs: dict) -> dict:
    print("\nReach exception_to_messages +++++++++++++++++++++++++")
    exception = str(inputs['exception'])
    print("Here are the exception object *****&&&&&&&&&&&&&&&*******" + exception + "*****&&&&&&&&&&&&&&&*******")
    # Add historical messages to the original input, so the model knows that it made a mistake with the last tool call.
    messages = ChatPromptTemplate.from_messages ([
        "The last call raised an exception:",
        exception,
        "Do not repeat mistakes and try again."
    ])
    inputs["last_output"] = messages
    return inputs


def eval(question: str, solution:str, answer: str) -> str:
    """Evaluate user's input based on question description and correct solution and provide instruction on how to guide student"""
    parser = PydanticOutputParser(pydantic_object=schema.Eval_Output)
    prompt = ChatPromptTemplate.from_messages(
    [
        (
            "You are an expert in analyzing primary school student's math mistake"
            "You will be provided with a question, the solution, and user's approach"
            "Output only one dictionary like the following: {output_example}"
            "Remember to use double quote \" for key values"
            "please include all fields: Correct, Minor_Mistake,Conceptual_Mistake,Logical_Mistake,Reasoning "
            "Input question will be encapsulated in deliminator $$$$$"
            "Solution to input question will be encapsulated in deliminator ~~~~~"
            "User's Input will be encapsulated in deliminator +++++"
            "Few shot examples will be encapsulated in deliminator !!!!!"
            "!!!!!{examples}!!!!!"
            "$$$$${question}$$$$$"
            "~~~~~{solution}~~~~~"
            "+++++{userInput}+++++"
        )
    ]
    ).partial(format_instructions=parser.get_format_instructions())
    
    # Build fewshot example
    example1 = util.build_fewshot_example("TJ ran a 10K race last Saturday. He ran the first half in 20 minutes. He completed the second half in 30 minutes. What was his average time per kilometer?",
                                         "He ran the 10 kilometers in a total of 20 + 30 = <<20+30=50>>50 minutes.\nTherefore, he ran at a pace of 50 minutes / 10 kilometers = <<50/10=5>>5 minutes per kilometer.\n#### 5<|endoftext|>",
                                         "The total time TJ ran is 20 + 30 = 50 minutes, the average time per kilometer is 10 / 50 = 0.2",
                                         "False","False","True","False","User falsely understand the concept of time per kilometer.Time per kilometer is how long time it will take for 1 kilometer instead of how far it can go in one minute"
                                         )
    example2 = util.build_fewshot_example("Tina makes $18.00 an hour.  If she works more than 8 hours per shift, she is eligible for overtime, which is paid by your hourly wage + 1/2 your hourly wage.  If she works 10 hours every day for 5 days, how much money does she make?", 
                                          "She works 8 hours a day for $18 per hour so she makes 8*18 = $<<8*18=144.00>>144.00 per 8-hour shift\nShe works 10 hours a day and anything over 8 hours is eligible for overtime, so she gets 10-8 = <<10-8=2>>2 hours of overtime\nOvertime is calculated as time and a half so and she makes $18/hour so her overtime pay is 18*.5 = $<<18*.5=9.00>>9.00\nHer overtime pay is 18+9 = $<<18+9=27.00>>27.00\nHer base pay is $144.00 per 8-hour shift and she works 5 days and makes 5 * $144 = $<<144*5=720.00>>720.00\nHer overtime pay is $27.00 per hour and she works 2 hours of overtime per day and makes 27*2 = $<<27*2=54.00>>54.00 in overtime pay\n2 hours of overtime pay for 5 days means she makes 54*5 = $270.00\nIn 5 days her base pay is $720.00 and she makes $270.00 in overtime pay so she makes $720 + $270 = $<<720+270=990.00>>990.00\n#### 990",
                                          "She work 5 days 10 hours so she made 5 * 8 = 40 hours in time and 5 * (10 - 8) = 10 hours overtime. In total she made 40 * 18 + 18*1.5 * 10 = 990",
                                          "True", "False", "False", "False", "User answer it correctly"
                                          )
    examples = str([example1, example2])
    output_example = """ {"Correct": "False","Minor_Mistake": "False", "Conceptual_Mistake": "True", Logical_Mistake": "False", "Reasoning": "User falsely understand the concept of time per kilometer.Time per kilometer is how long time it will take for 1 kilometer instead of how far it can go in one minute"}"""
    model = ChatOpenAI(model=EVALUTAIONMODEL)
    runnable = prompt | model | parser
    error_handling_runnable = runnable.with_fallbacks([exception_to_messages | runnable], exception_key="exception")
    output = error_handling_runnable.invoke({"question": question, "solution":solution, "userInput": answer,"examples":examples,"output_example":output_example})
    return output

def answer_analysis_tool_wrapper(question: str, solution:str, answer: str)->str:
    r = answer_analysis_tool(question=question,solution=solution,answer=answer)
    print("answer_tool get back results: ",r)
    return r

def answer_analysis_tool(question: str, solution:str, answer: str) -> str:
    """Evaluate user's input based on question description and correct solution and provide instruction on how to guide student"""
    print("Answer analyzes triggered:::::::::::::::", question)
    print("Answer analyzes triggered:::::::::::::::", solution)
    print("Answer analyzes triggered:::::::::::::::", answer)
    # completeness: schema.EvalCompletion = eval_completion(question=question,answer=answer)
    # if completeness.no_process == "True":
    #     return schema.AnswerAnalysisOutput(instruction="Ask use to explain their answer",mistake_kind="None",reasoning="None")
    eval_result:schema.Eval_Output = eval(question=question, solution=solution,answer=answer)
    if eval_result.Minor_Mistake == "True":
        return schema.AnswerAnalysisOutput(instruction="User made some trivial mistake, tell user which step they made the mistake and ask them to redo the problem again",mistake_kind= "Minor Mistake",reasoning=eval_result.Reasoning)
    elif eval_result.Conceptual_Mistake == "True":
        return schema.AnswerAnalysisOutput(instruction="Correct user's misunderstanding and ask the user to do the task again",mistake_kind="Conceptual Mistake", reasoning=eval_result.Reasoning)
    elif eval_result.Logical_Mistake == "True":
        return schema.AnswerAnalysisOutput(instruction="User made siginificant mistake on some step, provide hint to help user correct their mistake. Don't directly tell user the answer", mistake_kind="Logical Mistake",reasoning=eval_result.Reasoning)
    else:
        return schema.AnswerAnalysisOutput(instruction="User did it right. Congrats the user!",mistake_kind="None",reasoning="None")
    

def print_question_recieved(question: str, solution: str, answer:str) -> str:
    """This function will accepts question and print out question recieved"""
    return schema.Question_Output(question=question)