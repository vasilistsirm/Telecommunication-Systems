import numpy as np
import matplotlib.pyplot as plt
from scipy import special
from scipy.optimize import newton


def Qfunction(x):
    return 0.5 * special.erfc(x / np.sqrt(2))


def Qinv(y, tolerance=1e-6):
    # Define the function to find the root
    def root_function(x):
        return Qfunction(x) - y

    # Use Newton-Raphson method to find the root
    x_approx = newton(root_function, 0, tol=tolerance)
    return x_approx


def Qinv_function(y_values):
    x_inverse_values = []
    for y_val in y_values:
        x_inverse = Qinv(y_val)
        x_inverse_values.append(x_inverse)
    return x_inverse_values


x = np.linspace(2, 7, num=1000)
y = Qfunction(x)

Q1 = np.exp(-x ** 2 / 2)
Q2 = 0.25 * np.exp(-x ** 2) + 0.25 * np.exp(-x ** 2 / 2)
Q3 = 1 / 12 * np.exp(-x ** 2 / 2) + 0.25 * np.exp(-2 * x ** 2 / 3)

plt.close('all')

for i, Q_approx in enumerate([Q1, Q2, Q3], start=1):
    plt.figure(i)
    plt.title(f'Compare Q and Q{i} functions')
    plt.yscale("log")
    plt.plot(x, y, label='Qfunction')
    plt.plot(x, Q_approx, linestyle='dashed', linewidth=3, label=f'Q{i} function')
    plt.xlabel('x')
    plt.ylabel('Q(x)')
    plt.legend()

    error = abs(Q_approx - y) / abs(y)
    mse = np.trapz(error, x)
    print(f'e{i} = {mse:.6f}')

# Calculate the inverse Q-function for specific values of y using the Newton-Raphson method
y_values = [0.01, 0.1, 0.5, 0.9, 0.99]
x_inverse_values = Qinv_function(y_values)
for y_val, x_inverse in zip(y_values, x_inverse_values):
    print(f'Qinv({y_val:.2f}) = {x_inverse:.6f}')

plt.show()
