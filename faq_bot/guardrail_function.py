from guardrail_agent import input_guardrail_agent,output_guardrail_agent
from agents import GuardrailFunctionOutput,input_guardrail,RunContextWrapper,Runner,output_guardrail

@input_guardrail
async def guardrail_input_function(ctx: RunContextWrapper, agent, input):

    result = await Runner.run(input_guardrail_agent, input=input, context=ctx)

    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=not result.final_output.is_query_valid
    )

@output_guardrail
async def guardrail_output_function(ctx: RunContextWrapper, agent, output):

    result = await Runner.run(output_guardrail_agent, input=output, context=ctx)

    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=not result.final_output.is_query_valid
    )