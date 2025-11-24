#!/usr/bin/env python3
"""
Autonomous Market Research System using CrewAI and LangChain

This system uses AI agents to conduct comprehensive market research and produce
investment reports. It features two specialized agents:
1. Senior Research Analyst - Conducts deep research
2. Chief Content Officer - Synthesizes findings into actionable reports
"""

import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from crewai_tools import SerperDevTool, ScrapeWebsiteTool

# Load environment variables from .env file
load_dotenv()

# Initialize tools
search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()


def create_research_analyst() -> Agent:
    """
    Create the Senior Research Analyst agent.
    
    This agent is responsible for conducting comprehensive market research,
    finding cutting-edge developments, and analyzing market sentiment.
    """
    return Agent(
        role="Senior Market Research Analyst",
        goal="Uncover cutting-edge developments and detailed market sentiment regarding the user's topic.",
        backstory=(
            "You are an expert analyst at a top-tier venture capital firm. "
            "You have a knack for finding hidden gems and identifying red flags in financial data. "
            "You never rely on surface-level news; you always dig for the original source. "
            "Your research is factual, data-driven, and always cites sources."
        ),
        verbose=True,
        allow_delegation=False,
        tools=[search_tool, scrape_tool],
        llm=ChatOpenAI(
            model=os.getenv("OPENAI_MODEL", "gpt-4"),
            temperature=0.7,
            api_key=os.getenv("OPENAI_API_KEY")
        )
    )


def create_content_officer() -> Agent:
    """
    Create the Chief Content Officer agent.
    
    This agent transforms raw research data into clear, compelling,
    and actionable investment reports.
    """
    return Agent(
        role="Chief Content Officer",
        goal="Synthesize complex data into a compelling executive summary for investors.",
        backstory=(
            "You are a renowned financial writer known for simplifying complex tech "
            "and financial concepts. You take raw research data and transform it into "
            "clear, concise, and actionable insights. Your writing style is professional, "
            "objective, and easy to read."
        ),
        verbose=True,
        allow_delegation=False,
        llm=ChatOpenAI(
            model=os.getenv("OPENAI_MODEL", "gpt-4"),
            temperature=0.7,
            api_key=os.getenv("OPENAI_API_KEY")
        )
    )


def create_research_task(agent: Agent, topic: str) -> Task:
    """
    Create the research task for the Senior Research Analyst.
    
    Args:
        agent: The agent to assign the task to
        topic: The research topic/company to investigate
    
    Returns:
        Task object configured for comprehensive research
    """
    return Task(
        description=(
            f"Conduct comprehensive research on: {topic}\n\n"
            "Your task:\n"
            "1. Search for the latest news, articles, and reports about this topic\n"
            "2. Identify and read the top 3-5 most relevant and authoritative sources\n"
            "3. Extract key information including:\n"
            "   - Recent developments and innovations\n"
            "   - Market trends and sentiment\n"
            "   - Financial performance (if applicable)\n"
            "   - Potential risks and red flags\n"
            "   - Competitive landscape\n"
            "4. Compile your findings with proper source citations\n"
            "5. Focus on factual, data-driven insights\n\n"
            "Remember: Always cite your sources and dig deeper than surface-level news."
        ),
        expected_output=(
            "A detailed research report containing:\n"
            "- Summary of key findings with source citations\n"
            "- Market trends and sentiment analysis\n"
            "- Risk factors and red flags identified\n"
            "- Data-driven insights and observations\n"
            "- List of all sources consulted"
        ),
        agent=agent
    )


def create_writing_task(agent: Agent, topic: str) -> Task:
    """
    Create the report writing task for the Chief Content Officer.
    
    Args:
        agent: The agent to assign the task to
        topic: The research topic for context
    
    Returns:
        Task object configured for report generation
    """
    return Task(
        description=(
            f"Transform the research findings about '{topic}' into a professional "
            "investment report in Markdown format.\n\n"
            "Your task:\n"
            "1. Review all research data provided by the Senior Research Analyst\n"
            "2. Create a structured report with the following sections:\n"
            "   - **Executive Summary**: A concise overview (3-4 paragraphs)\n"
            "   - **Key Findings**: Bullet points of the most important insights\n"
            "   - **Market Analysis**: Detailed analysis of trends and opportunities\n"
            "   - **Risk Assessment**: Potential concerns and red flags\n"
            "   - **Conclusion**: Final recommendation or summary\n"
            "3. Write in a clear, professional, and objective tone\n"
            "4. Make complex concepts accessible to investors\n"
            "5. Include relevant data and citations from the research\n\n"
            "The report should be actionable and decision-ready for investors."
        ),
        expected_output=(
            "A professional Markdown-formatted investment report with:\n"
            "- Executive Summary\n"
            "- Key Findings section\n"
            "- Detailed Market Analysis\n"
            "- Risk Assessment\n"
            "- Clear Conclusion with actionable insights\n"
            "- Proper formatting and structure"
        ),
        agent=agent
    )


def run_market_research(topic: str) -> str:
    """
    Execute the market research system with the specified topic.
    
    Args:
        topic: The company or topic to research
    
    Returns:
        The final investment report as a string
    """
    print(f"\n{'='*60}")
    print(f"Starting Market Research for: {topic}")
    print(f"{'='*60}\n")
    
    # Create agents
    research_analyst = create_research_analyst()
    content_officer = create_content_officer()
    
    # Create tasks
    research_task = create_research_task(research_analyst, topic)
    writing_task = create_writing_task(content_officer, topic)
    
    # Create crew
    crew = Crew(
        agents=[research_analyst, content_officer],
        tasks=[research_task, writing_task],
        process=Process.sequential,
        verbose=True
    )
    
    # Execute the research
    result = crew.kickoff()
    
    return result


def save_report(report: str, filename: str = "market_research_report.md") -> None:
    """
    Save the research report to a file.
    
    Args:
        report: The report content to save
        filename: The output filename (default: market_research_report.md)
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(str(report))
    print(f"\n{'='*60}")
    print(f"Report saved to: {filename}")
    print(f"{'='*60}\n")


def main():
    """
    Main execution function.
    
    Validates environment variables, runs the research, and saves the report.
    """
    # Validate required environment variables
    required_vars = ["OPENAI_API_KEY", "SERPER_API_KEY"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        print("ERROR: Missing required environment variables:")
        for var in missing_vars:
            print(f"  - {var}")
        print("\nPlease set these variables in your .env file or environment.")
        print("See .env.example for the template.")
        return
    
    # Define the research topic
    # Change this to your desired topic
    topic = "Applications of Generative AI in Big Data Analytics"
    
    # Alternative topics you can research:
    # topic = "Tesla's Electric Vehicle Market Strategy"
    # topic = "Quantum Computing Investment Opportunities"
    # topic = "Cryptocurrency Market Trends 2024"
    
    try:
        # Run the market research
        report = run_market_research(topic)
        
        # Save the report
        save_report(report)
        
        # Print summary
        print("Market research completed successfully!")
        print(f"Topic: {topic}")
        print(f"Report saved to: market_research_report.md")
        
    except Exception as e:
        print(f"\nERROR: An error occurred during execution:")
        print(f"{type(e).__name__}: {str(e)}")
        print("\nPlease check your API keys and internet connection.")


if __name__ == "__main__":
    main()
