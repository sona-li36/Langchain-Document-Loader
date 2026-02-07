from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template ='Write a summary fro the folloeing poem - \n {poem}',
    input_variable=['poem']
)

parser = StrOutParser()
# Load the cricket.txt file
loader = TextLoader("cricket.txt")
doc= loader.load()

print(doc)
print(type(doc))

print(len(doc).page_content)

print(doc[0].metadata)

chain = prompt | model |parser
print(chain.invoke({'poem':docs[0].page_content}))