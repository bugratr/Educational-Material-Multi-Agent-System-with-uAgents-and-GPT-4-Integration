import asyncio
from agents.worksheet_agent import worksheet_agent
from agents.test_agent import test_agent
from agents.performance_agent import performance_agent
from agents.rubric_agent import rubric_agent
from agents.coordinator_agent import coordinator_agent

async def main():
    await asyncio.gather(
        worksheet_agent.run(),
        test_agent.run(),
        performance_agent.run(),
        rubric_agent.run(),
        coordinator_agent.run(),
    )

if __name__ == "__main__":
    asyncio.run(main())
