from promptflow import tool


# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def generate_static_output(prompt:str, websites: str, dates:str):
    if prompt != None:
        return prompt
    elif websites != None:
        return websites
    elif dates != None:
        return dates
    else:
        return 'No static output found'
