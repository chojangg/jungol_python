sum_ = 0
cnt = 0

while True:
    num = int(input())
    sum_ += num
    cnt += 1
    if num >= 100:
        break
print(sum_)
print(f'{(sum_/cnt):.1f}')