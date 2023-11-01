import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain


os.environ['OPENAI_API_KEY']='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'

llm = OpenAI(temperature=0.6)

prompt_template_name= PromptTemplate(
    input_variables=['cuisine'],
    template="I want to open a restaurant for {cuisine} food, suggest me a fancy name for this."
)
name_chain= LLMChain(llm=llm, prompt=prompt_template_name, output_key='restaurant_name')

prompt_template_items= PromptTemplate(
    input_variables=['restaurant_name'],
    template="Suggest me some menu items for {restaurant_name},reurn it as coma seprate list."
)
items_chain= LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

def Data(food):
    chain=SequentialChain(chains=[name_chain, items_chain],input_variables=['cuisine'], output_variables=['restaurant_name','menu_items'])
    reponse=chain(food)
    return reponse

# response=Data("Indian")
# print(response['restaurant_name'].strip())

# print(response['menu_items'].strip().split(','))
