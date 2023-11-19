# Ollama Basics
Basic of working with a locally hosted Ollama environment, focusing on using the prompt flow framwork for managing a locally hosted llama2 model

## Instructions

### Setup Ollama
- Download from https://ollama.ai/download
- Pull and serve llama2
```
ollama pull llama2
ollama serve llama2
```
- If you elect to use a different model, you will need to change `client.py` and `ollama_pf/ollama.py` to reflect the new model choice

### Run the following to install dependencies
```
# Create and activate virtual environment 
python -m venv venv
source ./venv/bin/activate

# Install required libraries
pip install -r requirements.txt
```

## Locally hosted ASCII chat client
The file `./client.py` contains code provided in the Ollama repo for creating a basic ascii-only chat client.  To start the client simply call 
```
python ./client.py
```

## Prompt Flow
To create the prompt flow `client.py` was modified to create `./ollama_pf/ollama.py`, which calls the locally hosted ollama model as part of the prompt flow.

CURRENTLY THE FLOW WILL NOT SUPPORT A CONVERSATION

The flow has several parts:
1. The input is first run through a content filter.  If any words in the prompt appear in the list of restricted words, then the output is alterd and does not ever to to the LLM
1. After the content filter the flow evaluates the prompt for several conditions that are better handeled through inputs that do not go through the LLM.  These return simple python function returns, either static files or the system date.  The file/node `static_output.py` performs basic error handeling and passes the appropriate text on through the chain
1. If the prompt passes the content filter AND does not satisy any of the conditions for the static returns, the prompt is them passed to the LLM
1. The file/node `generate_response.py` again does some basic error handling and passes the appropriate text to the output. 

Test the flow by calling
```
pf flow test --flow ollama_pf --interactive
```

 ## TODO
 - Prompt flow - Add jinja prompts to handle conversation history
 - Prompt flow - Create examples of different prompts (math, code cleaning, etc)
 - General - Create env variables to handle different models
 - General - Create setup.sh to download Ollama (assume linux?), pull and server model, and download python libraries
 - Prompt flow AND client - add temperature controls