from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('compile Book.pdf')

docs = loader.load()

print(len(docs))