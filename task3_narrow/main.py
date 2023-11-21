from sympy import symbols
N, t1, t2, t3, t4, t5 = symbols('N, t1, t2, t3, t4, t5')

N = 7

t1 = 1
t2 = 1
t3 = 1
t4 = 2
t5 = 2

import numpy as np

def remove_max_element(values: list[int]) -> list[int]:
    index_max = np.argmax(values)
    values_without_max = values[:index_max] + values[index_max+1:]

    return values_without_max, index_max

t_values = [t1, t2, t3, t4, t5]
t_values_without_max, index_max = remove_max_element(t_values)
print(t_values_without_max)

T = symbols('T')

T = N * max(t1, t2, t3, t4, t5) + sum(map(lambda t: t*t, t_values_without_max)) / t_values[index_max]
print(T)

Lambda = N / T
print(Lambda)

rho_values = list(map(lambda rho: rho * Lambda, t_values))
print(f'rho_values: {rho_values}')


lambda_background = (N - 1) / T
print(f'lambda background (фоновая): {lambda_background}')
rho_background_values = lambda_background * np.array(t_values)
print(f'rho background (фоновые) values: {rho_background_values}')

L_values = np.array(rho_values) / (1 - rho_background_values)
print(f'L values: {L_values}')

T_values = L_values / Lambda
print(f'T values: {T_values}')

W_values = T_values - np.array(t_values)
print(f'W values: {W_values}')
