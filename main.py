from backtesting import *


"""
共三个回测函数可选
1. 回测某一天: backtesting_one_day(ticker, date, debug, log)
2. 回测某一年: backtesting_year(ticker, year, debug, log)
3. 回测某一时间范围: backtesting_range(ticker, start, end, debug, log)

每个回测函数都共有两个参数debug、log，默认为false。
若使用这两个功能理论更耗时一点但区别不大，和模型运算时间相比可忽略不计，但为效率考虑尽量选False
    debug: 是否trace整个流程，输出每个步骤的结果
    log: 是否将最终的state结果写入json文件

******* 注意：返回结果都是HOLD/SELL/BUY字符串，如需0/-1/1需自行修改 *******

"""

# 回测2025-08-18 Bitcoin——非debug模式+不记录日志 （测试运行时间：376.5025s 429.9547s 359.5137s 316.6s 374.8s 390.2s）
# start_time = time.time()
# decision = backtesting_one_day("Bitcoin", "2025-08-18")
# end_time = time.time()
# print(decision)
# print(f"函数执行时间: {end_time - start_time:.1f} 秒")

# 回测2025-08-18 Bitcoin——debug模式+记录日志 （测试运行时间：371.8s 349.5s 397.5s）
# start_time = time.time()
# decision = backtesting_one_day("Bitcoin", "2025-08-18", debug=True, log=True)
# end_time = time.time()
# print(decision)
# print(f"函数执行时间: {end_time - start_time:.1f} 秒")

# 回测一个时间范围
results = backtesting_range("Bitcoin", "2025-08-16", "2025-08-18")
print(results)

# 回测某一年
# decisions = backtesting_year("Bitcoin", 2023)
