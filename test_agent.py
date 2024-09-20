from uagents import Agent, Context
import openai
import os

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Test Agent
test_agent = Agent(name="test_agent", seed="test_recovery_phrase")

@test_agent.on_message("create_test")
async def create_test(ctx: Context, message):
    class_level = message['class_level']
    subject = message['subject']
    details = message['details']
    skills = message['skills']

    # OpenAI API call to generate content
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert in creating educational tests."},
            {"role": "user", "content": f"Create a test for {class_level} grade students on {subject}. The test should include questions that assess the following skills: {skills}."}
        ],
        max_tokens=500
    )

    test_content = response['choices'][0]['message']['content'].strip()

    ctx.logger.info(f"Generated Test Content: {test_content}")

    # Send the content to the Coordinator Agent
    await ctx.send(agent="coordinator_agent", performative="inform", content={"test": test_content})

if __name__ == "__main__":
    test_agent.run()
