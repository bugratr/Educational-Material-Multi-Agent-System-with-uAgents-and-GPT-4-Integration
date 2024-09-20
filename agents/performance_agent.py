from uagents import Agent, Context
import openai
import os

# Set your OpenAI API key for GPT-4
openai.api_key = os.getenv("OPENAI_API_KEY")

# Performance Task Agent
performance_agent = Agent(name="performance_agent", seed="performance_recovery_phrase")

@performance_agent.on_message("create_performance_task")
async def create_performance_task(ctx: Context, message):
    class_level = message['class_level']
    subject = message['subject']
    details = message['details']
    skills = message['skills']

    # OpenAI API call using GPT-4 to generate content
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert in creating comprehensive performance tasks."},
            {"role": "user", "content": f"Create performance tasks for {class_level} grade students on {subject}. The tasks should involve {details} and aim to enhance the following skills: {skills}."}
        ],
        max_tokens=500
    )

    performance_content = response['choices'][0]['message']['content'].strip()

    ctx.logger.info(f"Generated Performance Task Content: {performance_content}")

    # Send the content to the Coordinator Agent
    await ctx.send(agent="coordinator_agent", performative="inform", content={"performance_task": performance_content})

if __name__ == "__main__":
    performance_agent.run()
