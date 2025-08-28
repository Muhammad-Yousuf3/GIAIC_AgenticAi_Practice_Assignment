from config import tavily_client
from agents import function_tool

@function_tool
def Web_Search(query):
    """Perform a web search using Tavily and return the results."""
    search_results = tavily_client.search(query=query, num_results=3)
    return f"Searching: {search_results}"