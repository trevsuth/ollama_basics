# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from promptflow import tool
import json
import requests

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need


@tool
def generate(prompt: str, context: str):
    r = requests.post('http://localhost:11434/api/generate',
                    json={
                        'model': 'llama2',
                        'prompt': prompt,
                        'context': context,
                    },
                    stream=True)
    r.raise_for_status()

    complete_response = ''  # Initialize an empty string to store the response

    for line in r.iter_lines():
        body = json.loads(line)
        response_part = body.get('response', '')

        complete_response += response_part  # Append each part of the response

        if 'error' in body:
            raise Exception(body['error'])

        if body.get('done', False):
            return complete_response  # Return the complete response at the end

    return complete_response  # Also return the complete response if loop exits without 'done'
