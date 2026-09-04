def f(x):
    return x**2 - x - 1


x0 = 1.0
x1 = 2.0
iteration = 1

print("Secant Method")
print("Equation: f(x) = x^2 - x - 1")
print()

print("-" * 65)
print(f"{'Iter':<8}{'x0':<12}{'x1':<12}{'f(x0)':<12}{'f(x1)':<12}{'x2':<12}")
print("-" * 65)

while True:

    fx0 = f(x0)
    fx1 = f(x1)

    x2 = x1 - (fx1 * (x1 - x0)) / (fx1 - fx0)

    print(f"{iteration:<8}{x0:<12.6f}{x1:<12.6f}"
          f"{fx0:<12.6f}{fx1:<12.6f}{x2:<12.6f}")

    if abs(x2 - x1) < 0.001:
        break

    x0 = x1
    x1 = x2

    iteration += 1

print("-" * 65)
print(f"Approximate Root = {x2:.3f}")
print(f"Total Iterations = {iteration}")