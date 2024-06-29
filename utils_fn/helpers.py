
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_qa(query: str, response_no_rag: str, response_rag) -> None:
    text = f"{bcolors.OKGREEN}Question:{bcolors.ENDC} {query} \n" + \
    f"{bcolors.OKGREEN}LLM:{bcolors.ENDC} {response_no_rag} \n" + \
    f"{bcolors.OKGREEN}RAG:{bcolors.ENDC} {response_rag}"
    print(text)