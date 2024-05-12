import psutil

from langchain.agents import tool

@tool
def check_system_performance(interval: int = 1):
    """Returns system performance metrics"""
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    
    return  cpu_usage
