#!/usr/bin/env python3
import matplotlib.pyplot as plt


def linear_polynomial(x):
    return 2 * x + 1


# Plot
x_val, y_val = [], []

for i in range(1, 11):
    x_val.append(i)
    y_val.append(linear_polynomial(i))


def quadratic_polynomial(x):
    return (x * x) + x - 2


x_val, y_val = [], []
for i in range(-8, 8):
    x_val.append(i)
    y_val.append(quadratic_polynomial(i))

fig, ax = plt.subplots(figsize=(12, 9))
# ax.autoscale(enable=False)
ax.plot(x_val, y_val)
ax.set_title("Quadratic Polynomial")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid(axis="both")
plt.show()


def cubic_polynomial(x):
    return 5 * (x**3) + (x**2)


x_val, y_val = [], []
for i in range(-8, 8):
    x_val.append(i)
    y_val.append(cubic_polynomial(i))

fig, ax = plt.subplots(figsize=(12, 9))
# ax.autoscale(enable=False)
ax.plot(x_val, y_val)
ax.set_title("Cubic Polynomial")
ax.set_xlabel("x")
ax.set_ylabel("y")
plt.show()
