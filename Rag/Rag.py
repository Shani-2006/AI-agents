from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core import Settings
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding

import os
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


Settings.llm = OpenAI(model="gpt-4.1-mini")
Settings.embed_model = OpenAIEmbedding(model_name="text-embedding-3-small")

documents = SimpleDirectoryReader(r"D:\data").load_data()

index = VectorStoreIndex.from_documents(documents)

query_engine=index.as_query_engine(similarity_top_k=2)

response=query_engine.query(
    "What will the weather be like during Purim this year and what is the state of the war?"
)

print(response)
