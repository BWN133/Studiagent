from Tools import tools
from dotenv import load_dotenv
import json
load_dotenv()
def evaluate_example():
    question = "We have a triangle with height 10 and width 8, what is the area of it?"
    solution = "10 * 8 / 2 = 40"
    userInput = "the height is 10 and width is 8, so we multiply them together to get the area of triangle. the area in this case is 10 *8 = 80"
    print("execute")
    print(tools.eval.name)
    print(tools.eval.description)
    print(tools.eval.args)
    # evaluate_result = tools.eval.invoke({question,solution, userInput)
    print(tools.eval.run({"question":question, "solution":solution, "answer":userInput}))

def judge_example():
    question = "We have a triangle with height 10 and width 8, what is the area of it?"
    userInput = "We have a triangle with height 10 and width 8, what is the area of it?"
    print("execute")
    print(tools.eval_completion.name)
    print(tools.eval_completion.description)
    print(tools.eval_completion.args)
    print(tools.eval_completion.run({"question":question, "answer":userInput}))


if __name__ == '__main__':
    print("run")
    judge_example()
    evaluate_example()
    # Prompt Question
    # recieve answer judge whether complete. If the result is correct incorrect, static print
    # judge, into chat, reasoning
    # Agent, if user provide a new input result re enter the evaluation find reason loop 
    
    