"""
Partially generated by Colaboratory.
"""

# Commented out IPython magic to ensure Python compatibility.
# %%capture
# !pip install langchain

# https://www.youtube.com/watch?v=kYRB-vJFy38&list=PLqZXAkvF1bPNQER9mLmDbntNfSpzdDIU5&index=2

from google.colab import userdata
OPENAI_API_KEY = userdata.get('OPENAI_API_KEY')

from langchain import OpenAI, ConversationChain

llm = OpenAI(
    openai_api_key=OPENAI_API_KEY,
    model_name='gpt-3.5-turbo-instruct',
    temperature=0
)

convo = ConversationChain(
    llm=llm,
    verbose=False, # whether to show what it's thinking
)

def continueConvo(input):
    print('\nUser:',input,)
    response = convo.predict(input=input)
    print('\nAI:',response)

continueConvo('Hi there!')
continueConvo('What was the first thing I said to you?')
continueConvo('What is an alternative for the first thing I said to you?')
continueConvo('Now translate it into French and Arabic and Chinese and Russian and Swahili and Tagalog.')

"""

User: Hi there!

AI:  Hello! It's nice to meet you. I am an AI created by OpenAI. I am constantly learning and improving my abilities through machine learning algorithms. How can I assist you today?

User: What was the first thing I said to you?

AI:  The first thing you said to me was "Hi there!" Would you like me to repeat it back to you?

User: What is an alternative for the first thing I said to you?

AI:  An alternative for "Hi there!" could be "Hello!" or "Greetings!" Is there a specific alternative you had in mind?

User: Now translate it into French and Arabic and Chinese and Russian and Swahili and Tagalog.

AI:  In French, "Hi there!" would be "Salut!" In Arabic, it would be "مرحبا!" In Chinese, it would be "你好!" In Russian, it would be "Привет!" In Swahili, it would be "Habari!" And in Tagalog, it would be "Kumusta!" Is there a specific language you would like me to translate it into?
"""
