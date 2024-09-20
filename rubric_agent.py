from uagents import Agent, Context
import openai
import os

# Set your OpenAI API key for GPT-4
openai.api_key = os.getenv("OPENAI_API_KEY")

# Rubric Agent
rubric_agent = Agent(name="rubric_agent", seed="rubric_recovery_phrase")

@rubric_agent.on_message("create_rubric")
async def create_rubric(ctx: Context, message):
    class_level = message['class_level']
    subject = message['subject']
    details = message['details']
    skills = message['skills']

    # OpenAI API call using GPT-4 to generate rubric content
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert in creating evaluation rubrics."},
            {"role": "user", "content": f"Create a rubric for evaluating {class_level} grade students on {subject} with the task involving {details}. The rubric should assess the following skills: {skills}."}
        ],
        max_tokens=500
    )

    rubric_content = response['choices'][0]['message']['content'].strip()

    ctx.logger.info(f"Generated Rubric Content: {rubric_content}")

    # Send the rubric to the Coordinator Agent
    await ctx.send(agent="coordinator_agent", performative="inform", content={"rubric": rubric_content})

if __name__ == "__main__":
    rubric_agent.run()
