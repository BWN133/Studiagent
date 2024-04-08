from Tools import tools
from dotenv import load_dotenv
import json
load_dotenv()
def evaluate_example():
    question = "We have a triangle with height 10 and width 8, what is the area of it?"
    solution = "10 * 8 / 2 = 40"
    userInput = "the height is 10 and width is 8, so we multiply them together to get the area of triangle. the area in this case is 10 *8 = 80"
    evaluate_result = tools.eval(question,solution, userInput)


def main():
    # Prompt Question
    
    # recieve answer judge whether complete. If the result is correct incorrect, static print
    # judge, into chat, reasoning
    # Agent, if user provide a new input result re enter the evaluation find reason loop 
    
    
    pass 