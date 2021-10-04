

def countdown(num):
    while num > 0:
        yield num
        num-=1
val = countdown(10)
print(next(val))

print(next(val))
print(next(val))
print(next(val))
print(next(val))
print(next(val))