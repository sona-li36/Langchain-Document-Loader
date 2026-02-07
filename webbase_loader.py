from langchain_community.document_loaders import WebBaseLoader

url = "https://flipkart.com/apple-macbook-air-m4-16-gb-256-gb-ssd-macos-sequoia-mw0w3hn-a/p/itmf733f99c22ee6?pid=COMH9ZWQP4EP2XAT&lid=LSTCOMH9ZWQP4EP2XAT2OHHOE&marketplace=FLIPKART&q=mac+book+air+4&store=6bo%2Fb5g&srno=s_1_1&otracker=search&otracker1=search&fm=organic&iid=aa9ed37a-b98f-4c75-8786-66865eac2b0a.COMH9ZWQP4EP2XAT.SEARCH&ppt=hp&ppn=homepage&ssid=wt8u4ptugg0000001770461611541&qH=079f269e152f5aaf"

loader = WebBaseLoader(url)
docs = loader.load()
print(docs[0].page_content)