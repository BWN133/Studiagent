from config import *


def build_fewshot_example(question:str, solution:str, userInput: str, correct,minor_mistake, cm, lm, reason):
    # cur_result = "For the content below, all content inside **** **** are what system provided you. The AI output are what is after"
    cur_result =  "Question: " + question + "\n Solution: " + solution + "\n User Input: " + userInput + "\n \n AI Output: "
    cur_result += """{"Correct": \""""  + correct + """\","Minor_Mistake": \"""" + minor_mistake + """\", "Conceptual_Mistake": \"""" +  cm + """\", Logical_Mistake": \"""" + lm + """\", "Reasoning": \"""" + reason +"\"}"
    return cur_result

def build_judge_example(question:str, userInput: str, absent, no_process, no_result, complete):
    result =  "Question: " + question + "\n User Input: " + userInput + "\n \n "
    d = {"absent": absent, "no_process":  no_process, "no_result": no_result, "complete": complete}
    return result + str(d)

