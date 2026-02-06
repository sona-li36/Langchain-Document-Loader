from langchain_community.document_loaders import TextLoader

# Load the cricket.txt file
loader = TextLoader("cricket.txt")
doc= loader.load()

print(doc)
print(type(doc))

print(len(doc))

print(doc[0])