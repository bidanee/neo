from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex, ServiceContext, LLMPredictor, StorageContext, load_index_from_storage
from langchain.chat_models import ChatOpenAI

# 데이터 뽑아와서
documents = SimpleDirectoryReader('data').load_data()

# predictor 설정
llm_predictor = LLMPredictor(llm=ChatOpenAI(
  temperature=0,
  model_name="gpt-3.5-turbo"
))

ServiceContext = ServiceContext.from_defaults(
  llm_predictor=llm_predictor,
)

index = GPTVectorStoreIndex.from_documents(
  documents,
  service_context=ServiceContext
)

# index save
index.storage_context.persist(persist_dir="./storage")

# index load
storage_cotext = StorageContext.from_defaults(persist_dir="./storage")
loaded_index = load_index_from_storage(storage_cotext)

query_engin = index.as_query_engine()

print('-' *50)
print(query_engin.query("미코의 소꿉친구 이름은?"))

print('-' *50)
print(query_engin.query("울프 코퍼레이션의 CEO 이름은?"))