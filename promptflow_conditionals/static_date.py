from promptflow import tool
from datetime import datetime

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def get_current_date():
    # Get the current date
    today = datetime.today()

    # Format the date as a string (e.g., '2023-11-18')
    return str(today.strftime("%Y-%m-%d"))