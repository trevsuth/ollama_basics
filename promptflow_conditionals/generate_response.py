from promptflow import tool


# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def create_output(ollama_output: str, content_output:str, static_output: str):
    if content_output != None:
        return content_output
    elif static_output != None:
        return static_output
    elif ollama_output != None:
        return ollama_output
    else:
        return 'No valid output found'