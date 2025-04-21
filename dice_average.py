import random
kaisuu = [10, 100, 1000, 10000, 1000000] # 平均値用のリスト

def roll_average(trial):
    average = 0 # 平均値の初期化
    total = 0 # サイコロの出目の合計値を記録する変数
    for n in range(trial): # trial分だけループ処理
        total += random.randint(1,6) #1~6のランダムな数を加算
    average = total / trial #合計数を試行回数で割る
    return average # 関数の戻り値は平均値

# リスト[kaisuu]までの平均値を求める処理
for i in kaisuu:
    print(str(i)+"回試行の平均値："+str(roll_average(i)))

# 実際の実行結果
""" 
10回試行の平均値：4.0
100回試行の平均値：3.48
1000回試行の平均値：3.525
10000回試行の平均値：3.4857
1000000回試行の平均値：3.499314
"""
