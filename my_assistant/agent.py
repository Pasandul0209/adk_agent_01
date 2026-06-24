from google.adk.agents import Agent 
 
root_agent = Agent( 
    name="My_Assistant", 
    model="gemini-3.1-flash-lite-preview", 
    description="A helpful assistant.", 
    instruction="You are a helpful assistant. Answer questions clearly.", 
) 
