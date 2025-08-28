from agents import Agent
from config import model
from bot_schema import FaqQuery

input_guardrail_agent:Agent = Agent(
    name="InputGuardrailAgent",
    instructions="""Check Queries for General Store
    Also answer the queries for questions consisting word store not name of the store.
    Don't be strict.
    Allow the agent to answer multiple question at same time.
    Your main goal is to warn the user if any negative or abusive language is being used by the user.""",
    model=model,
    output_type=FaqQuery,
)

output_guardrail_agent:Agent = Agent(
    name="OutputGuardrailAgent",
    instructions="""Check the response of FAQ agent for General Store
    Ensure that the response is not a political commentary, religious view, or contains any negative or abusive language.""",
    model=model,
    output_type=FaqQuery,
)