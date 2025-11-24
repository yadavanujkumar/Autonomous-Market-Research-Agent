# Autonomous Market Research Agent 🤖📊

An intelligent multi-agent system that leverages AI to conduct comprehensive market research and produce professional investment reports. Built with CrewAI and LangChain, this system orchestrates specialized AI agents that collaborate to deliver data-driven insights.

## 🎯 Features

- **Multi-Agent Collaboration**: Two specialized AI agents work together:
  - **Senior Research Analyst**: Conducts deep research, finds cutting-edge developments, and analyzes market sentiment
  - **Chief Content Officer**: Transforms raw research into clear, actionable investment reports

- **Powerful Tools Integration**:
  - Google Search via SerperDev API
  - Web scraping capabilities
  - OpenAI GPT-4 powered analysis

- **Professional Output**: Generates structured Markdown reports with:
  - Executive Summary
  - Key Findings
  - Market Analysis
  - Risk Assessment
  - Actionable Conclusions

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Serper API key (free tier available)

### Installation

1. **Clone the repository**:
```bash
git clone https://github.com/yadavanujkumar/Autonomous-Market-Research-Agent.git
cd Autonomous-Market-Research-Agent
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**:
```bash
cp .env.example .env
```

Edit the `.env` file and add your API keys:
```env
OPENAI_API_KEY=your_openai_api_key_here
SERPER_API_KEY=your_serper_api_key_here
OPENAI_MODEL=gpt-4  # Optional: defaults to gpt-4
```

### Getting API Keys

#### OpenAI API Key
1. Go to [OpenAI Platform](https://platform.openai.com/api-keys)
2. Sign up or log in
3. Create a new API key
4. Copy the key to your `.env` file

#### Serper API Key (Free Tier Available)
1. Go to [Serper.dev](https://serper.dev/)
2. Sign up for a free account (includes 2,500 searches)
3. Copy your API key from the dashboard
4. Add it to your `.env` file

### Running the System

```bash
python main.py
```

The system will:
1. Research the specified topic using Google Search
2. Analyze the top 3-5 relevant sources
3. Compile findings with citations
4. Generate a professional investment report
5. Save the report as `market_research_report.md`

## 🎨 Customization

### Change Research Topic

Edit the `main.py` file and modify the `topic` variable in the `main()` function:

```python
# Default topic
topic = "Applications of Generative AI in Big Data Analytics"

# Alternative examples:
# topic = "Tesla's Electric Vehicle Market Strategy"
# topic = "Quantum Computing Investment Opportunities"
# topic = "Cryptocurrency Market Trends 2024"
```

### Adjust LLM Model

In your `.env` file, you can choose different OpenAI models:

```env
OPENAI_MODEL=gpt-4              # Most capable (recommended)
OPENAI_MODEL=gpt-3.5-turbo      # Faster and cheaper
OPENAI_MODEL=gpt-4-turbo-preview # Latest preview version
```

## 📋 System Architecture

```
┌─────────────────────────────────────┐
│      Main Orchestration Layer      │
│         (CrewAI Crew)              │
└─────────────────┬───────────────────┘
                  │
        ┌─────────┴─────────┐
        │                   │
        ▼                   ▼
┌───────────────┐   ┌──────────────────┐
│   Research    │   │     Content      │
│   Analyst     │──▶│     Officer      │
│   Agent       │   │     Agent        │
└───────┬───────┘   └──────────────────┘
        │
   ┌────┴────┐
   │         │
   ▼         ▼
┌──────┐ ┌────────┐
│Search│ │Scrape  │
│Tool  │ │Tool    │
└──────┘ └────────┘
```

## 🛠️ Technical Stack

- **Framework**: CrewAI for agent orchestration
- **LLM**: OpenAI GPT-4 / GPT-3.5-turbo
- **Tools**: 
  - LangChain Community Tools
  - SerperDevTool (Google Search)
  - ScrapeWebsiteTool (Web scraping)
- **Environment**: python-dotenv for configuration management

## 📝 Output Example

The system generates a comprehensive Markdown report like this:

```markdown
# Market Research Report: [Topic]

## Executive Summary
[Concise overview of findings...]

## Key Findings
- Finding 1
- Finding 2
- Finding 3

## Market Analysis
[Detailed analysis of trends and opportunities...]

## Risk Assessment
[Potential concerns and red flags...]

## Conclusion
[Final insights and recommendations...]
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [CrewAI](https://github.com/joaomdmoura/crewai)
- Powered by [LangChain](https://github.com/langchain-ai/langchain)
- Search capabilities by [Serper.dev](https://serper.dev/)
- AI by [OpenAI](https://openai.com/)

## 📧 Support

For issues, questions, or suggestions, please open an issue on GitHub.

---

**Happy Researching! 🚀**