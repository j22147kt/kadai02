import random

total = 0
for i in range(10):
    x = random.randint(1,6)
    total += x
    print(str(i+1)+"回目："+str(x))
    
    average = total / 10
print("平均値：" + str(average))

# 出力結果
"""
1回目：5
2回目：2
3回目：6
4回目：2
5回目：1
6回目：3
7回目：2
8回目：5
9回目：3
10回目：4
平均値：3.3
"""
