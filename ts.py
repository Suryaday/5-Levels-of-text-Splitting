from langchain_text_splitters import CharacterTextSplitter
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import SimpleDirectoryReader

text = "A Quick brown fox jumps over the lazy dog. This sentence contains all the letters of the alphabet"
chunks = []
chunk_size = 30

for i in range(4, len(text), chunk_size):
    chunk = text[i-4: i+chunk_size]
    chunks.append(chunk)

print(chunks)

#######Langchain############

text_splitter = CharacterTextSplitter(chunk_size=35, chunk_overlap=4, separator="")
split = text_splitter.create_documents([text])

for i in range(len(split)):
    print(split[i].page_content)

print(split)

######LLAMA Index##########

splitter = SentenceSplitter(
    chunk_size=200,
    chunk_overlap=15,
)

documents = SimpleDirectoryReader(
    input_files=["Mit.txt"]
).load_data()

nodes = splitter.get_nodes_from_documents(documents)

print(nodes[0])