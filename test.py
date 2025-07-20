"""
- 4个Analysts的prompt如果有FINAL TRANSACTION PROPOSAL就stop：1.合理吗 2.怎么实现的 3.顺序有影响吗
- 两个debateResearcher&Risk，为什么manager用deep thinking，debater用quick thinking？
- workflow中，current_clear是什么？为什么current_node->tool&clear clear->next node
- debate过程如果一方劣势很大会不会强词夺理？
- 每个agent传递给下一个的信息是什么？manager能拿到之前的信息吗
"""
import os

print(os.getenv('OPENAI_API_KEY'))
print(os.environ.get("OPENAI_API_KEY"))