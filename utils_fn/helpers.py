from llama_index.core import VectorStoreIndex

class colors:
    green = "\033[92m"
    reset = "\033[0m"


def print_qa(query: str, response_no_rag: str, response_rag) -> None:    
    print(f"{colors.green}Question:\n{colors.reset}{query}", end="\n\n")
    print(f"{colors.green}LLM:\n{colors.reset}{response_no_rag}", end="\n\n")
    print(f"{colors.green}RAG:\n{colors.reset}{response_rag}")


def print_rag(index: VectorStoreIndex, query: str):
    vector_retriever = index.as_retriever(similarity_top_k=5)
    query_engine = index.as_query_engine(similarity_top_k=5)

    retrieved = "\n\n".join([str(x) for x in vector_retriever.retrieve(query)])
    answer = query_engine.query(query).response

    result_text = (
        f"{colors.green}Question:\n{colors.reset}{query}\n\n"
        f"{colors.green}Retrieved:\n{colors.reset}{retrieved}\n\n"
        f"{colors.green}Answer:\n{colors.reset}{answer}"
    )

    print(result_text)
    
