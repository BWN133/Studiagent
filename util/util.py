from config import *


def build_fewshot_example(question:str, solution:str, userInput: str, correct,minor_mistake, cm, lm, reason):
    result =  "Question: " + question + "\n Solution: " + solution + "\n User Input: " + userInput + "\n \n "
    d = {"Correct": correct, "Minor_Mistake": minor_mistake, "Conceptual_Mistake": cm, "Logical_Mistake":lm,"Reasoning": reason}
    return result + str(d)

def build_judge_example(question:str, userInput: str, if_answer, incomplete, complete, input_type):
    result =  "Question: " + question + "\n User Input: " + userInput + "\n \n "
    d = {"if_answer": if_answer, "incomplete": incomplete, "complete": complete, "input_type": input_type}
    return result + str(d)