# coding : utf-8
sum_1 = sum[x * x for x in range(1, 101)]
sum_2 = (sum[x for x in range(1, 101)]) ** 2

print(sum_2 - sum_1)
