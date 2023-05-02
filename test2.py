import time
inicio = time.time()

# Código a medir
# The code defines a lambda function `R` that takes no arguments and returns a map object that applies
# the `int` function to each element of the input obtained from the `input()` function after splitting
# it by whitespace.
R = lambda: map(int, input().split())

t, = R()

# The code is running a loop `t` times, where `t` is the first input obtained from the user. In each
# iteration of the loop, the code reads three integers `l`, `r`, and `x` from the user using the `R`
# lambda function. Then, it reads two more integers `a` and `b` using the `R` function and sorts them
# in ascending order.
for _ in range(t):
    l, r, x = R()
    a, b = sorted(R())
    if a == b:
        print(0)
    elif b - a >= x:
        print(1)
    elif x <= max(a - l, r - b):
        print(2)
    elif r - a >= x and x <= b - l:
        print(3)
    else:
        print(-1)
time.sleep(1)
# -------------

fin = time.time()
print(fin-inicio) # 1.0005340576171875