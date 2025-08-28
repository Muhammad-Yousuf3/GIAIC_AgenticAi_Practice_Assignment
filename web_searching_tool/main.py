import chainlit as cl
from agents import Runner, set_tracing_disabled
from web_search_agent import WebSearchAgent

set_tracing_disabled(True)

@cl.on_chat_start
async def start():
    await cl.Message(content="Hi 👋! Ask me anything to search.").send()

@cl.on_message
async def handle_message(message: cl.Message):
    # Run your agent with the user's input
    results = Runner.run_sync(starting_agent=WebSearchAgent, input=message.content)
    
    # Send the agent's response back to the UI
    await cl.Message(content=results.final_output).send()