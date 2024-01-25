"""
Partially generated by Colaboratory.
"""

# Commented out IPython magic to ensure Python compatibility.
# %%capture
# !pip install openai
# !pip install langchain

from google.colab import userdata
OPENAI_API_KEY = userdata.get('OPENAI_API_KEY')

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = OpenAI(
    openai_api_key=OPENAI_API_KEY,
    model_name='gpt-3.5-turbo-instruct',
)

promptMaker = PromptTemplate(
    template='What are 5 of the most famous {what}?',
    input_variables=['what'],
)

chain = LLMChain(
    llm=llm,
    prompt=promptMaker, # <-- LLMChain chains the LLM with the prompt for us!
)

what = 'conlangs'
response = chain.run(what)
print(response)
