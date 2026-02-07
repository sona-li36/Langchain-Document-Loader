from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template ='Answer the folloeing question\n {question}  from the following text - \n {text}',
    input_variable=['question','text']
)

parser = StrOutParser()
loader =DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls= PyPDFLoader
)
#docs = loader.load()
docs = loader.lazy_load()
# print(len(docs))
#print(docs[0].page_content)
#print(docs[0].metadata)

for document in docs:
    print(document.metadata)

chain = prompt |model|parser
chain.invoke({'question': 'What is the peak brightness of the product','text':docs[0].page_content})
