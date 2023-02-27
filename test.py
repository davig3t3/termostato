R = lambda: map(int, input().split())

t, = R()

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