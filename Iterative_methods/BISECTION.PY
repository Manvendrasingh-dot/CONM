def f(x):
    return x**2 - x - 1


a = 1.0
b = 2.0
iteration = 1

print("Bisection Method")
print("Equation: f(x) = x^2 - x - 1")
print()

print("-" * 90)
print(f"{'Iter':<6}{'a':<10}{'b':<10}{'m':<10}{'f(a)':<12}{'f(b)':<12}{'f(m)':<12}{'f(a)*f(m)':<15}")
print("-" * 90)

while abs(b - a) > 0.001:

    m = (a + b) / 2

    fa = f(a)
    fb = f(b)
    fm = f(m)

    product = fa * fm

    print(f"{iteration:<6}{a:<10.3f}{b:<10.3f}{m:<10.3f}"
          f"{fa:<12.4f}{fb:<12.4f}{fm:<12.4f}{product:<15.4f}")

    if product < 0:
        b = m
    else:
        a = m

    iteration += 1

print("-" * 90)
print(f"Approximate Root = {m:.3f}")
print(f"Total Iterations = {iteration - 1}")