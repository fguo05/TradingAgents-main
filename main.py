from backtesting import *


# 回测2025-08-18 Bitcoin——正常模式+不记录日志 376.5025s 429.9547s 359.5137s 316.6s 374.8s 390.2s
start_time = time.time()
decision = backtesting_one_day("Bitcoin", "2025-08-18", debug=False, log=False)
end_time = time.time()
print(decision)
print(f"函数执行时间: {end_time - start_time:.1f} 秒")

# 回测2025-08-18 Bitcoin——debug模式+记录日志 371.8s 349.5s 397.5s
# start_time = time.time()
# decision = backtesting_one_day("Bitcoin", "2025-08-18", debug=True, log=True)
# end_time = time.time()
# print(decision)
# print(f"函数执行时间: {end_time - start_time:.1f} 秒")

# 回测一个时间范围
# results = backtesting_range("Bitcoin", "2025-08-16", "2025-08-18", False, False)
# print(results)

# 回测2023年Bitcoin
# decisions = backtesting_year("Bitcoin", 2023)
