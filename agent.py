from google.adk.agents import Agent

root_agent = Agent(
    name="my_Assistant",
    model="gemini-3.1-flash-lite",
    description="A helpful assistant.",
    instruction="You are a helpful assistant. Answer questions clearly.",
)