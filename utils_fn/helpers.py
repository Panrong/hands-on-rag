

class colors:
    green = "\033[92m"
    reset = "\033[0m"


def print_qa(query: str, response_no_rag: str, response_rag) -> None:    
    print(f"{colors.green}Question:\n{colors.reset}{query}", end="\n\n")
    print(f"{colors.green}LLM:\n{colors.reset}{response_no_rag}", end="\n\n")
    print(f"{colors.green}RAG:\n{colors.reset}{response_rag}")
