from agents import Runner,set_tracing_disabled,InputGuardrailTripwireTriggered,OutputGuardrailTripwireTriggered
from config import model
from faq_agents import Faq_agent

set_tracing_disabled(True)
prompt=input("Enter your query: ")

try:
    result = Runner.run_sync(starting_agent=Faq_agent, input=prompt)
    print(result.final_output)
except InputGuardrailTripwireTriggered as e:
    print("Error: Invalid Query.")
except OutputGuardrailTripwireTriggered as e:
    print("Error: Inappropriate Response Generated.")