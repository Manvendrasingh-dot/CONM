def f(x):
    return x**2 - x - 1


def df(x):
    return 2*x - 1


x = 2.0
iteration = 1

print("Newton-Raphson Method")
print("Equation: f(x) = x^2 - x - 1")
print()

print("-" * 65)
header = f"{'Iter':<8}{'x':<12}{'f(x)':<15}{'fprime(x)':<15}{'x_new':<12}"
print(header)
print("-" * 65)

while True:

    fx = f(x)
    dfx = df(x)

    x_new = x - (fx / dfx)

    print(f"{iteration:<8}{x:<12.6f}{fx:<15.6f}"
          f"{dfx:<15.6f}{x_new:<12.6f}")

    if abs(x_new - x) < 0.001:
        break

    x = x_new
    iteration += 1

print("-" * 65)
print(f"Approximate Root = {x_new:.3f}")
print(f"Total Iterations = {iteration}")