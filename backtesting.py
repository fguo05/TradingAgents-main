import time
from datetime import datetime, timedelta
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG


def backtesting_year(ticker:str, year:int, debug:bool=False, log:bool=False):
    """
    回测某一年
    """
    if year > datetime.now().year:
        return False

    # Create a custom config
    config = DEFAULT_CONFIG.copy()
    # config["llm_provider"] = "google"  # Use a different model
    # config["backend_url"] = "https://generativelanguage.googleapis.com/v1"  # Use a different backend
    # config["deep_think_llm"] = "gemini-2.0-flash"  # Use a different model
    # config["quick_think_llm"] = "gemini-2.0-flash"  # Use a different model
    # config["max_debate_rounds"] = 1  # Increase debate rounds
    # config["online_tools"] = True  # Increase debate rounds

    ta = TradingAgentsGraph(debug=debug, config=config, log=log)

    results = []

    start_date = datetime(year, 1, 1)
    end_date = datetime.now().date() if year == datetime.now().year else datetime(year, 12, 31)

    current_date = start_date
    while current_date <= end_date:
        _, decision = ta.propagate(ticker, current_date.strftime("%Y-%m-%d"))
        results.append(decision)
        # Memorize mistakes and reflect
        # ta.reflect_and_remember(1000) # parameter is the position returns
        current_date += timedelta(days=1)

    return results

def backtesting_one_day(ticker:str, date:str, debug:bool=False, log:bool=False):
    """
    回测某一天
    ticker: ticker名称
    date: YYYY-MM-DD格式日期
    debug: 设置是否debug模式
    log: 是否记录日志
    """
    config = DEFAULT_CONFIG.copy()

    ta = TradingAgentsGraph(debug=debug, config=config, log=log)

    _, decision = ta.propagate(ticker, date)

    return decision

def backtesting_range(ticker:str, start_date:str, end_date:str, debug:bool=False, log:bool=False):
    """
    回测某一时间范围
    ticker: ticker名称
    start_date: YYYY-MM-DD格式日期
    end_date: YYYY-MM-DD格式日期
    debug: 设置是否debug模式
    log: 是否记录日志
    """
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    if start_date > end_date or end_date > datetime.now():
        return False

    config = DEFAULT_CONFIG.copy()

    ta = TradingAgentsGraph(debug=debug, config=config, log=log)

    results = []

    current_date = start_date
    while current_date <= end_date:
        # start_time = time.time()

        _, decision = ta.propagate(ticker, current_date.strftime("%Y-%m-%d"))
        results.append(decision)
        # Memorize mistakes and reflect
        ta.reflect_and_remember(1000) # parameter is the position returns
        current_date += timedelta(days=1)

        # end_time = time.time()
        # print(f"执行时间: {end_time - start_time:.1f} 秒")

    return results