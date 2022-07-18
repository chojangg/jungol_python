import time

now = time.localtime()
a = 0
a = now.tm_year - 1900  # ----------------------- ①
a += now.tm_mon - 1  # ----------------------- ②
a += now.tm_mday
print(a, a, a)