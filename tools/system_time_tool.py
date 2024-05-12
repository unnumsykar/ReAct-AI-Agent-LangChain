import datetime
from langchain.agents import tool 
@tool
def check_system_time(format:str = "%Y-%m-%d %H:%M:%S"):
    """returns the current system time in specified format"""
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime(format)
    
    return formatted_time
    