from langchain_core.runnables.history import RunnableWithMessageHistory
from config import *

def speech_Condition_1(agent_executor:RunnableWithMessageHistory):
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

def speech_Condition_2(agent_executor:RunnableWithMessageHistory):
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