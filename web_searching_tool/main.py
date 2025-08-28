from agents import Runner,set_tracing_disabled
from web_search_agent import WebSearchAgent

set_tracing_disabled(True)

prompt=input("Enter your query : ")
results=Runner.run_sync(starting_agent=WebSearchAgent, input=prompt)

print(results.final_output)