from Tools import toolset
from dotenv import load_dotenv
import json
from Pipeline import studiagent
load_dotenv()
def evaluate_example():
    question = "We have a triangle with height 10 and width 8, what is the area of it?"
    solution = "10 * 8 / 2 = 40"
    userInput = "the height is 10 and width is 8, so we multiply them together to get the area of triangle. the area in this case is 10 *8 = 80"
    print("execute")
    # print(toolset.eval.name)
    # print(toolset.eval.description)
    # print(toolset.eval.args)
    # evaluate_result = tools.eval.invoke({question,solution, userInput)
    # print(toolset.eval.run({"question":question, "solution":solution, "answer":userInput}))

def judge_example():
    question = "We have a triangle with height 10 and width 8, what is the area of it?"
    userInput = "10 * 8 / 2 = 40"
    # print("execute")
    # print(toolset.eval_completion.name)
    # print(toolset.eval_completion.description)
    # print(toolset.eval_completion.args)
    # print(toolset.eval_completion.run({"question":question, "answer":userInput}))


if __name__ == '__main__':
    print("run")
    studiagent.main_agent()
    # Prompt Question
    # recieve answer judge whether complete. If the result is correct incorrect, static print
    # judge, into chat, reasoning
    # Agent, if user provide a new input result re enter the evaluation find reason loop 
    
    