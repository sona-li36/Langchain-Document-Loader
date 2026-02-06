from langchain_community.document_loaders import TextLoader

# Load the cricket.txt file
loader = TextLoader("cricket.txt")
documents = loader.load()

print(documents)