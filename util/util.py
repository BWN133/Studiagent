from config import *


def build_fewshot_example(question:str, solution:str, userInput: str, correct, rm ,minor_mistake, cm, lm, reason):
    result =  "Question: " + question + "\n Solution: " + solution + "\n User Input: " + userInput + "\n \n "
    d = {"Correct": correct,"Reading_Mistake": rm,"Minor_Mistake": minor_mistake, "Conceptual_Mistake": cm, "Logical_Mistake":lm,"Reasoning": reason}
    return result + str(d)