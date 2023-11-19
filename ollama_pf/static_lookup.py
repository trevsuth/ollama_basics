from promptflow import tool


# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def static_input_type(prompt: str):
    prompt_lower = prompt.lower()
    cases = {
            'teach me about prompting': 'example_prompts',
            'what are some websites': 'websites',
            'what is the date': 'date'
    }

    return cases.get(prompt_lower, 'not static')

