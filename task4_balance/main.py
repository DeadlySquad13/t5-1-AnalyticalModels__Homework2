from sympy import symbols
import numpy as np

N, t1, t2, t3, t4, t5 = symbols('N, t1, t2, t3, t4, t5')

N = 7
m = 5

t1 = 1
t2 = 1
t3 = 1
t4 = 2
t5 = 2

rho = N * m / (N + m - 1)
print(f'rho: {rho}')

t_values = np.array([t1, t2, t3, t4, t5])
rho_values = t_values * rho / sum(t_values)
print(f'rho values: {rho_values}')

unstationary_rho_values = list(filter(lambda rho: rho >= 1, rho_values))
if len(unstationary_rho_values):
    WARNING_COLOR = '\033[93m'
    END_COLOR = '\033[0m'
    print(WARNING_COLOR + \
            f'Warning: some rho_values {unstationary_rho_values} are larger then 1, it seems that system is unstationary!' +\
            ' Please choose other time values.' +\
            END_COLOR)

T_cycle = N * t1 / rho_values[0] # Why formula uses only first?
print(f'T cycle: {T_cycle}')

Lambda = N / T_cycle
print(f'Lambda: {Lambda}')

lambda_background = (N - 1) / T_cycle
print(f'lambda background (фоновая): {lambda_background}')
rho_background_values = lambda_background * np.array(t_values)
print(f'rho background (фоновые) values: {rho_background_values}')

L_values = np.array(rho_values) / (1 - rho_background_values)
print(f'L values: {L_values}')

T_values = L_values / Lambda
print(f'T values: {T_values}')

W_values = T_values - np.array(t_values)
print(f'W values: {W_values}')
