# Quick Start Guide

## 🚀 Getting Started in 3 Minutes

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Configure API Keys
```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your keys:
# - OPENAI_API_KEY: Get from https://platform.openai.com/api-keys
# - SERPER_API_KEY: Get from https://serper.dev/ (free tier: 2,500 searches)
```

### Step 3: Run the System
```bash
python main.py
```

## 🎯 Customize Your Research

Edit `main.py` and change the `topic` variable (around line 223):

```python
# Default
topic = "Applications of Generative AI in Big Data Analytics"

# Or try:
topic = "Electric Vehicle Market Trends 2024"
topic = "Quantum Computing Investment Opportunities"
topic = "Your Company Name Here"
```

## 📊 What Happens

1. **Research Agent** searches and analyzes 3-5 top sources
2. **Content Agent** synthesizes findings into a report
3. **Output** saved as `market_research_report.md`

## 💡 Model Options

In your `.env` file:
- `gpt-4` - Most capable (recommended)
- `gpt-3.5-turbo` - Faster and cheaper
- `gpt-4-turbo-preview` - Latest features

## 🐛 Troubleshooting

**"Missing required environment variables"**
→ Check your `.env` file has both API keys

**"Rate limit exceeded"**
→ Wait a moment and try again, or upgrade your API plan

**"Serper API error"**
→ Check your Serper API key is valid and has credits remaining

## 📖 Full Documentation

See [README.md](README.md) for complete documentation.
