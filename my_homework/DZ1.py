N = int(input('enter_time:\n'))
x = N // 3600
y = (N % 3600) // 60
z = (N % 3600) % 60
print(f'{x} : {y} : {z}')
