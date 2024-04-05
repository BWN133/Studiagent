from Tools import tools
from dotenv import load_dotenv
load_dotenv()

question = "We have a triangle with height 10 and width 8, what is the area of it?"
solution = "10 * 8 / 2 = 40"
userInput = "the height is 10 and width is 8, so we multiply them together to get the area of triangle."
print(tools.eval(question,solution, userInput))