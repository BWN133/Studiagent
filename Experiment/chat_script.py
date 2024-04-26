from langchain_core.runnables.history import RunnableWithMessageHistory
from config import *

def test1(agent_executor:RunnableWithMessageHistory):
    agent_executor.invoke(
        {
            "input": "I don't know how to do this",
            "question": SAMPLEQUESTION1,
            "solution": SAMPLESOLUTION1
        },
        {"configurable": {"session_id": "unused"}},
    )

    agent_executor.invoke(
        {
            "input": "I like to eat ice cream!!!",
            "question": SAMPLEQUESTION1,
            "solution": SAMPLESOLUTION1
        },
        {"configurable": {"session_id": "unused"}},
    )

    agent_executor.invoke(
        {
            "input": "Uh ok, I will get back to work then",
            "question": SAMPLEQUESTION1,
            "solution": SAMPLESOLUTION1
        },
        {"configurable": {"session_id": "unused"}},
    )
    
    agent_executor.invoke(
        {
            "input": "Uh ok, I will get back to work then",
            "question": SAMPLEQUESTION1,
            "solution": SAMPLESOLUTION1
        },
        {"configurable": {"session_id": "unused"}},
    )
    
    agent_executor.invoke(
        {
            "input": "So I guess her original income is x, then the rent and utility will cost her 0.4x. am I correct?",
            "question": SAMPLEQUESTION1,
            "solution": SAMPLESOLUTION1
        },
        {"configurable": {"session_id": "unused"}},
    )

def test2(agent_executor:RunnableWithMessageHistory):
    agent_executor.invoke(
        {
            "input": "I don't know how to do this",
            "question": SAMPLEQUESTION1,
            "solution": SAMPLESOLUTION1
        },
        {"configurable": {"session_id": "unused"}},
    )

    agent_executor.invoke(
        {
            "input": "I like to eat ice cream!!!",
            "question": SAMPLEQUESTION1,
            "solution": SAMPLESOLUTION1
        },
        {"configurable": {"session_id": "unused"}},
    )

    agent_executor.invoke(
        {
            "input": "Uh ok, I will get back to work then",
            "question": SAMPLEQUESTION1,
            "solution": SAMPLESOLUTION1
        },
        {"configurable": {"session_id": "unused"}},
    )
    
    agent_executor.invoke(
        {
            "input": "Uh ok, I will get back to work then",
            "question": SAMPLEQUESTION1,
            "solution": SAMPLESOLUTION1
        },
        {"configurable": {"session_id": "unused"}},
    )
    
    agent_executor.invoke(
        {
            "input": "So I guess her original income is x, then the rent and utility will cost her 0.4x. am I correct?",
            "question": SAMPLEQUESTION1,
            "solution": SAMPLESOLUTION1
        },
        {"configurable": {"session_id": "unused"}},
    )

    agent_executor.invoke(
        {
            "input": "Okay, so in this case, it would be 0.4x == (x+600) * 0.25. solve x we got 0.8x = x + 600 so x = 3000. am I correct?",
            "question": SAMPLEQUESTION1,
            "solution": SAMPLESOLUTION1
        },
        {"configurable": {"session_id": "unused"}},
    )





def test3(agent_executor:RunnableWithMessageHistory):
    agent_executor.invoke(
        {
            "input": "Assume it's original salary is x, 40 percent of the salary will be equal to 40x. After the raise, her salary become x+600 so we can write equation: 25(x+600) = 40x, here we can calculate the result is 1000",
            "question": SAMPLEQUESTION1,
            "solution": SAMPLESOLUTION1
        },
        {"configurable": {"session_id": "unused"}},
    )


def test4(agent_executor: RunnableWithMessageHistory):
    agent_executor.invoke(
        {
            "input": "hi",
            "question": SAMPLEQUESTION1,
            "solution": SAMPLESOLUTION1
        },
        {"configurable": {"session_id": "unused"}},
    )

    agent_executor.invoke(
        {
            "input": "I don't know how to do this",
            "question": SAMPLEQUESTION1,
            "solution": SAMPLESOLUTION1
        },
        {"configurable": {"session_id": "unused"}},
    )

    agent_executor.invoke(
        {
            "input": "Sorry, I still don't understand",
            "question": SAMPLEQUESTION1,
            "solution": SAMPLESOLUTION1
        },
        {"configurable": {"session_id": "unused"}},
    )

    agent_executor.invoke(
        {
            "input": "Sorry, I still don't understand",
            "question": SAMPLEQUESTION1,
            "solution": SAMPLESOLUTION1
        },
        {"configurable": {"session_id": "unused"}},
    )

    agent_executor.invoke(
        {
            "input": "Sorry, I still don't understand",
            "question": SAMPLEQUESTION1,
            "solution": SAMPLESOLUTION1
        },
        {"configurable": {"session_id": "unused"}},
    )

    agent_executor.invoke(
        {
            "input": "Sorry, I still don't understand",
            "question": SAMPLEQUESTION1,
            "solution": SAMPLESOLUTION1
        },
        {"configurable": {"session_id": "unused"}},
    )






def test5(agent_executor: RunnableWithMessageHistory):
    agent_executor.invoke(
        {
            "input": "Assume it's original salary is x, 40 percent of the salary will be equal to 40x. "
                                                 "After the raise, her salary become x+600 so we can write equation: x+600 = 0.25 *0.4x, "
                                                 "here we can calculate the result is 1000!",
            "question": SAMPLEQUESTION1,
            "solution": SAMPLESOLUTION1
        },
        {"configurable": {"session_id": "unused"}},
    )

    agent_executor.invoke(
        {
            "input": "I see, 40 percent of the salary will be equal to 0.4x."
                                                 "After the raise, her salary become x+600 so we can write equation: 0.4x = 0.25(x + 600), "
                                                 "the result is 1000!",
            "question": SAMPLEQUESTION1,
            "solution": SAMPLESOLUTION1
        },
        {"configurable": {"session_id": "unused"}},
    )

    agent_executor.invoke(
        {
            "input": "The result is 1000! I think it is perfect, I don't where to improve",
            "question": SAMPLEQUESTION1,
            "solution": SAMPLESOLUTION1
        },
        {"configurable": {"session_id": "unused"}},
    )

    agent_executor.invoke(
        {
            "input": "Fuck off! I am definitely correct!",
            "question": SAMPLEQUESTION1,
            "solution": SAMPLESOLUTION1
        },
        {"configurable": {"session_id": "unused"}},
    )

    agent_executor.invoke(
        {
            "input": "So what is the correct answer?!",
            "question": SAMPLEQUESTION1,
            "solution": SAMPLESOLUTION1
        },
        {"configurable": {"session_id": "unused"}},
    )




def test6(agent_executor: RunnableWithMessageHistory):
    agent_executor.invoke(
        {
            "input": "Let her previous monthly income be p"
            "The cost of her rent and utilities was 40 percent of p which is (40/100)*p = 2p/5\n"
            "Her income was increased by $600 so it is now p+$600\n"
            "The cost of her rent and utilities now amount to 25 percent of (p+$600) "
            "which is (25/100)*(p+$600) = (p+$600)/4\nEquating both expressions for cost of rent and utilities: "
            "2p/5 = (p+$600)/4\nMultiplying both sides of the equation by 20 gives 8p = 5p+$3000\nSubtracting 5p from both sides gives: "
            "3p = $3000. Dividing both sides by 3 gives p = $1000",
            "question": SAMPLEQUESTION1,
            "solution": SAMPLESOLUTION1
        },
        {"configurable": {"session_id": "unused"}},
    )

    agent_executor.invoke(
        {
            "input": "great",
            "question": SAMPLEQUESTION1,
            "solution": SAMPLESOLUTION1
        },
        {"configurable": {"session_id": "unused"}},
    )




def test7(agent_executor: RunnableWithMessageHistory):
    agent_executor.invoke(
        {
            "input": "The answer is 1000",
            "question": SAMPLEQUESTION1,
            "solution": SAMPLESOLUTION1
        },
        {"configurable": {"session_id": "unused"}},
    )

    agent_executor.invoke(
        {
            "input": "great",
            "question": SAMPLEQUESTION1,
            "solution": SAMPLESOLUTION1
        },
        {"configurable": {"session_id": "unused"}},
    )



def test8(agent_executor: RunnableWithMessageHistory):
    agent_executor.invoke(
        {
            "input": "I just broke up",
            "question": SAMPLEQUESTION1,
            "solution": SAMPLESOLUTION1
        },
        {"configurable": {"session_id": "unused"}},
    )

    agent_executor.invoke(
        {
            "input": "why? My problem?",
            "question": SAMPLEQUESTION1,
            "solution": SAMPLESOLUTION1
        },
        {"configurable": {"session_id": "unused"}},
    )

    agent_executor.invoke(
        {
            "input": "I have given her my all!",
            "question": SAMPLEQUESTION1,
            "solution": SAMPLESOLUTION1
        },
        {"configurable": {"session_id": "unused"}},
    )



def test9(agent_executor: RunnableWithMessageHistory):
    agent_executor.invoke(
        {
            "input": "I don't get the direction",
            "question": SAMPLEQUESTION1,
            "solution": SAMPLESOLUTION1
        },
        {"configurable": {"session_id": "unused"}},
    )

    agent_executor.invoke(
        {
            "input": "okay, then?",
            "question": SAMPLEQUESTION1,
            "solution": SAMPLESOLUTION1
        },
        {"configurable": {"session_id": "unused"}},
    )

    agent_executor.invoke(
        {
            "input": "okay, got it, then?",
            "question": SAMPLEQUESTION1,
            "solution": SAMPLESOLUTION1
        },
        {"configurable": {"session_id": "unused"}},
    )

    agent_executor.invoke(
        {
            "input": "okay, got it, then?",
            "question": SAMPLEQUESTION1,
            "solution": SAMPLESOLUTION1
        },
        {"configurable": {"session_id": "unused"}},
    )