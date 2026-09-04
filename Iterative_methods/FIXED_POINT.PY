import math


def g(x):
    return math.sqrt(x + 1)


x = 1.0
iteration = 1

print("Fixed Point Iteration Method")
print("Equation: x^2 - x - 1 = 0")
print("Iteration formula: x = sqrt(x + 1)")
print()

print("-" * 40)
print(f"{'Iter':<10}{'x':<15}{'x_new':<15}")
print("-" * 40)

while True:

    x_new = g(x)

    print(f"{iteration:<10}{x:<15.6f}{x_new:<15.6f}")

    if abs(x_new - x) < 0.001:
        break

    x = x_new
    iteration += 1

print("-" * 40)
print(f"Approximate Root = {x_new:.3f}")
print(f"Total Iterations = {iteration}")