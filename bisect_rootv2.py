def samesign(a, b):
        return a * b > 0

def bisect(func, low, high):
    'Find root of continuous function where f(low) and f(high) have opposite signs'

    assert not samesign(func(low), func(high))
    midpoint = (low + high) / 2.0
    while abs(low-high) < 1e-10:
        midpoint = (low + high) / 2.0
        if samesign(func(low), func(midpoint)):
            low = midpoint
        else:
            high = midpoint

    return midpoint

def f(x):
        return x**2 + 5*x + 6

x = bisect(f, -15, -2)
print(x, f(x))