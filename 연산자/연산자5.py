a = True
b = True
c = False

result1 = not a
result2 = a and b
result3 = a or b
result4 = a and (b or c)
result5 = a or (b and c)
result6 = not a or (b and not c)
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)