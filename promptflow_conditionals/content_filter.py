# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from promptflow import tool

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need


@tool
def is_content_appropriate(input_text, bad_words_path='./english_badwords.txt'):
    # Load the list of bad words
    bad_words = load_bad_words(bad_words_path)

    # Convert the input text to lower case for case-insensitive comparison
    lower_input_text = input_text.lower()

    # Check if any bad word is in the input text
    for word in bad_words:
        if word in lower_input_text:
            return False
    
    # If no bad words found
    return True

def load_bad_words(bad_words_path):
    try:
        with open(bad_words_path, 'r') as file:
            # Read lines and strip newline characters
            return [line.strip() for line in file]
    except FileNotFoundError:
        print("File not found. Please check the file path.")