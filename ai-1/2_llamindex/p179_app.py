from llama_index import Document
from llama_index import GPTVectorStoreIndex

texts = ['text1','text2', 'text3']
documents = [Document(text) for text in texts]
print('-' * 50)
print("Documents: ", documents)
print("-" * 50)

index = GPTVectorStorIndex.from_documents(documents)
print("index: ", index)
print("-" * 50)