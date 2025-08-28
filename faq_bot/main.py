import chainlit as cl
from agents import Runner, set_tracing_disabled, InputGuardrailTripwireTriggered, OutputGuardrailTripwireTriggered
from config import model
from faq_agents import Faq_agent

# Disable tracing
set_tracing_disabled(True)

@cl.on_chat_start
async def start():
    await cl.Message(content="Hi 👋! Ask me any FAQ query.").send()

@cl.on_message
async def handle_message(message: cl.Message):
    try:
        # Run the FAQ agent with user input
        result = Runner.run_sync(starting_agent=Faq_agent, input=message.content)
        await cl.Message(content=result.final_output).send()

    except InputGuardrailTripwireTriggered:
        await cl.Message(content="❌ Error: Invalid Query.").send()

    except OutputGuardrailTripwireTriggered:
        await cl.Message(content="⚠️ Error: Inappropriate Response Generated.").send()
