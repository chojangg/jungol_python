a = input()
b = input()
a = int(a)
b = int(b)

result1 = a > b
result2 = a < b
result3 = a >= b
result4 = a <= b
print(f'{a} > {b} --- {result1}')
print(f'{a} < {b} --- {result2}')
print(f'{a} >= {b} --- {result3}')
print(f'{a} <= {b} --- {result4}')