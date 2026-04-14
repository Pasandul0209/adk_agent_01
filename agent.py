from google.adk.agents import Agent

root_agent = Agent(
    name="my_assistant",
    model="gemini-2.0-flash",
    description="A helpful assistant that can answer questions.",
    instruction="You are a helpful assistant. Answer user questions clearly and concisely.",
)
