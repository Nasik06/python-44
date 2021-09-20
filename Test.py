import math
N = int(input('enter_time:\n'))
x = N / 3600
y = math.trunc(x)
z = (x - y) * 60
c = (z - math.trunc(z))*60
print(y), print(math.trunc(z)), print(math.ceil(c))
print(y, math.trunc(z), math.ceil(c))


x = N // 3600
y = (N % 3600)
z =

print(x)
