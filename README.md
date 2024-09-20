# Educational Material Multi-Agent System

This project implements a sophisticated multi-agent system using the uAgents framework to automate the creation of educational materials, including worksheets, tests, performance tasks, and rubrics. The system is designed with multiple specialized agents, each responsible for a distinct task, and utilizes advanced AI technologies to enhance the content generation process.

*Key Features:*

Multi-Agent Interaction: Each agent is dedicated to a specific task, such as creating worksheets or generating rubrics. The agents communicate and collaborate with one another via the Coordinator Agent to ensure a seamless and coherent workflow.
GPT-4 Integration: The agents leverage OpenAI's GPT-4 to generate high-quality, detailed educational content, including textual descriptions, questions, and structured tasks.
DALL·E Integration: For tasks requiring visual content, such as diagrams or illustrations, the system integrates with OpenAI’s DALL·E to automatically generate relevant images, enhancing the educational materials created.

*Why uAgents?*

The uAgents framework is at the core of this project, providing a scalable and flexible architecture for developing AI-driven applications. By utilizing uAgents, this project demonstrates the power of multi-agent systems in managing complex workflows, where each agent can focus on its specific role while ensuring the overall system works in harmony.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/bugratr/Educational-Material-Multi-Agent-System-with-uAgents-and-GPT-4-Integration.git

   ```
2. Navigate to the project directory:
   ```bash
   cd educational-material-multi-agent-system
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the main application:
   ```bash
   python app.py
   ```

2. The system will start all agents and coordinate the creation of educational materials based on the user input.

## Agents

### Worksheet Agent
- Generates worksheet content based on user inputs.

### Test Agent
- Generates test content based on user inputs.

### Performance Task Agent
- Creates comprehensive performance tasks based on user inputs.

### Rubric Agent
- Creates rubrics for evaluating the generated tasks.

### Coordinator Agent
- Manages communication between agents and coordinates the workflow.

## Contributions

Contributions are welcome! Please submit a pull request or open an issue if you have suggestions for improvements.

## License

This project is licensed under the MIT License.
