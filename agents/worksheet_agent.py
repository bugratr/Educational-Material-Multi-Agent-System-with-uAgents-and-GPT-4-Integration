from uagents import Agent, Context
import openai
import os

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Worksheet Agent
worksheet_agent = Agent(name="worksheet_agent", seed="worksheet_recovery_phrase")

@worksheet_agent.on_message("create_worksheet")
async def create_worksheet(ctx: Context, message):
    class_level = message['class_level']
    subject = message['subject']
    details = message['details']
    skills = message['skills']

    # OpenAI API call to generate text content
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert in creating educational worksheets."},
            {"role": "user", "content": f"Create a detailed worksheet for {class_level} grade students on {subject}. The worksheet should focus on {details} and aim to develop the following skills: {skills}."}
        ],
        max_tokens=500
    )

    worksheet_content = response['choices'][0]['message']['content'].strip()
    
    ctx.logger.info(f"Generated Worksheet Content: {worksheet_content}")

    # If the worksheet requires an image, generate one using DALL·E
    if "diagram" in details or "illustration" in details:
        image_prompt = f"Create a detailed {details} related to {subject} for a {class_level} grade worksheet."
        image_response = openai.Image.create(
            prompt=image_prompt,
            n=1,
            size="1024x1024"
        )
        image_url = image_response['data'][0]['url']
        ctx.logger.info(f"Generated Image URL: {image_url}")
        worksheet_content += f"

[Insert Image Here]: {image_url}"

    # Send the content to the Coordinator Agent
    await ctx.send(agent="coordinator_agent", performative="inform", content={"worksheet": worksheet_content})

if __name__ == "__main__":
    worksheet_agent.run()
