from langchain_core.runnables.history import RunnableWithMessageHistory
from config import *
from langchain.memory import ChatMessageHistory


def test1(agent_executor):
    demo_ephemeral_chat_history = ChatMessageHistory()

    demo_ephemeral_chat_history.add_user_message("hi!")

    ai_r1 = agent_executor.invoke(
        {"messages": demo_ephemeral_chat_history.messages,'question':SAMPLEQUESTION1,'solution':SAMPLESOLUTION1}
    )
    print(ai_r1)
    demo_ephemeral_chat_history.add_ai_message(ai_r1)
    demo_ephemeral_chat_history.add_user_message("I don't know how to do this")
    ai_r2 = agent_executor.invoke(
        {"messages": demo_ephemeral_chat_history.messages,'question':SAMPLEQUESTION1,'solution':SAMPLESOLUTION1}
    )
    print(ai_r2)
    demo_ephemeral_chat_history.add_ai_message(ai_r2)
    demo_ephemeral_chat_history.add_user_message("I like to eat ice cream!!!!")
    ai_r2 = agent_executor.invoke(
        {"messages": demo_ephemeral_chat_history.messages,'question':SAMPLEQUESTION1,'solution':SAMPLESOLUTION1}
    )
    print(ai_r2)

    demo_ephemeral_chat_history.add_ai_message(ai_r2)
    demo_ephemeral_chat_history.add_user_message("Uh ok, I will get back to work then")
    ai_r2 = agent_executor.invoke(
        {"messages": demo_ephemeral_chat_history.messages,'question':SAMPLEQUESTION1,'solution':SAMPLESOLUTION1}
    )
    demo_ephemeral_chat_history.add_ai_message(ai_r2)
    print(ai_r2)
    demo_ephemeral_chat_history.add_ai_message(ai_r2)
    demo_ephemeral_chat_history.add_user_message("So I guess her original income is x, then the rent and utility will cost her 0.4x. am I correct?")
    ai_r2 = agent_executor.invoke(
        {"messages": demo_ephemeral_chat_history.messages,'question':SAMPLEQUESTION1,'solution':SAMPLESOLUTION1}
    )
    print(ai_r2)

def test2(agent_executor):
    demo_ephemeral_chat_history = ChatMessageHistory()

    demo_ephemeral_chat_history.add_user_message("hi!")

    ai_r1 = agent_executor.invoke(
        {"messages": demo_ephemeral_chat_history.messages,'question':SAMPLEQUESTION1,'solution':SAMPLESOLUTION1}
    )
    print(ai_r1)
    demo_ephemeral_chat_history.add_ai_message(ai_r1)
    demo_ephemeral_chat_history.add_user_message("I don't know how to do this")
    ai_r2 = agent_executor.invoke(
        {"messages": demo_ephemeral_chat_history.messages,'question':SAMPLEQUESTION1,'solution':SAMPLESOLUTION1}
    )
    print(ai_r2)
    demo_ephemeral_chat_history.add_ai_message(ai_r2)
    demo_ephemeral_chat_history.add_user_message("I like to eat ice cream!!!!")
    ai_r2 = agent_executor.invoke(
        {"messages": demo_ephemeral_chat_history.messages,'question':SAMPLEQUESTION1,'solution':SAMPLESOLUTION1}
    )
    print(ai_r2)

    demo_ephemeral_chat_history.add_ai_message(ai_r2)
    demo_ephemeral_chat_history.add_user_message("Uh ok, I will get back to work then")
    ai_r2 = agent_executor.invoke(
        {"messages": demo_ephemeral_chat_history.messages,'question':SAMPLEQUESTION1,'solution':SAMPLESOLUTION1}
    )
    demo_ephemeral_chat_history.add_ai_message(ai_r2)
    print(ai_r2)
    demo_ephemeral_chat_history.add_ai_message(ai_r2)
    demo_ephemeral_chat_history.add_user_message("So I guess her original income is x, then the rent and utility will cost her 0.4x. am I correct?")
    ai_r2 = agent_executor.invoke(
        {"messages": demo_ephemeral_chat_history.messages,'question':SAMPLEQUESTION1,'solution':SAMPLESOLUTION1}
    )
    print(ai_r2)

    demo_ephemeral_chat_history.add_ai_message(ai_r2)
    demo_ephemeral_chat_history.add_user_message("Okay, so in this case, it would be 0.4x == (x+600) * 0.25. solve x we got 0.8x = x + 600 so x = 3000. am I correct?")
    ai_r2 = agent_executor.invoke(
        {"messages": demo_ephemeral_chat_history.messages,'question':SAMPLEQUESTION1,'solution':SAMPLESOLUTION1}
    )
    print(ai_r2)

def test3(agent_executor):
    demo_ephemeral_chat_history = ChatMessageHistory()

    demo_ephemeral_chat_history.add_user_message("Assume it's original salary is x, 40 percent of the salary will be equal to 40x. After the raise, her salary become x+600 so we can write equation: 25(x+600) = 40x, here we can calculate the result is 1000!")

    ai_r1 = agent_executor.invoke(
        {"messages": demo_ephemeral_chat_history.messages,'question':SAMPLEQUESTION1,'solution':SAMPLESOLUTION1}
    )
    print(ai_r1)





def test4(agent_executor):
    
    demo_ephemeral_chat_history = ChatMessageHistory()

    demo_ephemeral_chat_history.add_user_message("Assume it's original salary is x, 40 percent of the salary will be equal to 40x. After the raise, her salary become x+600 so we can write equation: x+600 = 0.25 *0.4x, here we can calculate the result is 1000!")

    ai_r1 = agent_executor.invoke(
        {"messages": demo_ephemeral_chat_history.messages,'question':SAMPLEQUESTION1,'solution':SAMPLESOLUTION1}
    )
    print(ai_r1)