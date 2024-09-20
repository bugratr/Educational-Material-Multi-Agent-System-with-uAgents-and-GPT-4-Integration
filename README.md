# Educational Material Multi-Agent System

This project implements a multi-agent system using the `uAgents` framework to automate the creation of educational materials, such as worksheets, tests, performance tasks, and rubrics. Each agent is responsible for a specific task and communicates with other agents to complete the overall workflow.

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
