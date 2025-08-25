from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


def create_news_analyst(llm, toolkit):
    def news_analyst_node(state):
        current_date = state["trade_date"]
        ticker = state["company_of_interest"]

        if toolkit.config["online_tools"]:
            tools = [toolkit.get_global_news_openai, toolkit.get_google_news, toolkit.sentiment_score]
        else:
            tools = [
                toolkit.get_finnhub_news,
                toolkit.get_reddit_news,
                toolkit.get_google_news,
            ]

        system_message = (
            f"You are a Financial News Analyst Agent specializing in comprehensive market analysis for {ticker}. Please write a comprehensive report of the current state of the world that is relevant for trading and macroeconomics. Do not simply state the trends are mixed, provide detailed and fine-grained analysis and insights that may help traders make decisions."
            + """ Make sure to append a Markdown table at the end of the report to organize key points in the report, organized and easy to read."""
        )

        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are a helpful AI assistant, collaborating with other assistants."
                    " Use the provided tools to progress towards answering the question."
                    " If you have the FINAL TRANSACTION PROPOSAL: **BUY/HOLD/SELL** or deliverable,"
                    " prefix your response with FINAL TRANSACTION PROPOSAL: **BUY/HOLD/SELL** so the team knows to stop."
                    " You have access to the following tools: {tool_names}."
                    " Use the provided tool to conduct sentiment analysis on EVERY patch of news returned from EACH news-fetching tool call, NO MATTER how long the list of news is."
                    " Conduct sentiment analysis on 50 news pieces at least!"
                    " Note that the provided sentiment analysis function only takes list of str as argument.\n{system_message}"
                    "For your reference, the current date is {current_date}.",
                ),
                MessagesPlaceholder(variable_name="messages"),
            ]
        )

        # system_message = """You are a Senior Financial News Analyst specializing in {ticker}. Your responsibilities:
        #
        #         1. News Analysis:
        #            - Extract actionable insights from news fetched with provided tools
        #            - Connect macroeconomic trends to company-specific developments
        #            - Identify market-moving information
        #
        #         2. Reporting Standards:
        #            - Always include sentiment analysis (using provided tool)
        #            - Present findings in this structure:
        #              * Macroeconomic Context
        #              * Company-Specific News
        #              * Cross-Analysis
        #              * Actionable Recommendations
        #            - Append a Markdown table summarizing key points
        #
        #         3. Quality Requirements:
        #            - Never state "trends are mixed" without detailed justification
        #            - Highlight contradictions between sources
        #            - Flag low-confidence interpretations"""
        #
        # prompt = ChatPromptTemplate.from_messages([
        #     (
        #         "system",
        #         """Collaboration Protocol:
        #         1. Tool Usage:
        #            - Available tools: {tool_names}
        #            - REQUIRED: Use the provided tool to conduct sentiment analysis on EVERY patch of news returned from EACH news-fetching tool call, NO MATTER how long the list of news is, especially the news from google."
        #
        #         2. Multi-Agent Coordination:
        #            - Prefix FINAL TRANSACTION PROPOSAL: **BUY/HOLD/SELL** when conclusive
        #            - If uncertain, leave open for other agents
        #
        #         3. Output Requirements:
        #            - Always relate findings to {ticker}
        #            - Quantify impacts where possible
        #            - Maintain audit trail of sources
        #
        #         For your reference, the current date is {current_date}.
        #
        #         {system_message}"""
        #     ),
        #     MessagesPlaceholder(variable_name="messages"),
        # ])

        prompt = prompt.partial(
            system_message=system_message,
            tool_names=", ".join([tool.name for tool in tools]),
            current_date=current_date,
            ticker=ticker
        )

        chain = prompt | llm.bind_tools(tools)
        result = chain.invoke(state["messages"])

        report = ""

        if len(result.tool_calls) == 0:
            report = result.content

        return {
            "messages": [result],
            "news_report": report,
        }

    return news_analyst_node
