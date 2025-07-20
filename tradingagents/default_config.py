import os

DEFAULT_CONFIG = {
    "project_dir": os.path.abspath(os.path.join(os.path.dirname(__file__), ".")),
    "results_dir": os.getenv("TRADINGAGENTS_RESULTS_DIR", "./results"),
    "data_dir": "/Users/yluo/Documents/Code/ScAI/FR1-data",
    "data_cache_dir": os.path.join(
        os.path.abspath(os.path.join(os.path.dirname(__file__), ".")),
        "dataflows/data_cache",
    ),
    # LLM settings
    "llm_provider": "openai",
    "deep_think_llm": "o4-mini",
    "quick_think_llm": "gpt-4o-mini",
    "backend_url": "https://api.openai.com/v1",
    # Debate and discussion settings
    "max_debate_rounds": 1,
    "max_risk_discuss_rounds": 1,
    "max_recur_limit": 100,
    # Tool settings
    "online_tools": True,
}

OPENAI_API_KEY = "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"