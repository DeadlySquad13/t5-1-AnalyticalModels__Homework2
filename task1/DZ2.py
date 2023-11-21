def print_table(table, n):
    print("Таблица Базена:")
    for i in range(n+1):
            print(basen_table[i])

print("Задача 1")

n = 9 # Кол-во заявок
m = 5 # Кол-во фаз
tj = [1, 1, 1, 2, 3] # Время обработки заявок в ОА
X = [1.0] # Коэффициенты Базена
basen_table = []

for t in tj[1:]:
    X.append( t/tj[0] * X[0])
print("Коэффициенты Базена: ", X)

basen_table.append([1.0] * m) # Первая строка таблицы - единицы
for i in range(n):
    basen_table.append([1.0]+[0.0]*(m-1)) # Первый столбец - единицы

for i in range(1, m):
    for j in range(1, n+1):
        basen_table[j][i] = basen_table[j][i-1] + X[i] * basen_table[j-1][i]

print_table(basen_table, n)

# Расчет коэффициентов использования
ro = [0.0] * 5 # Коэффициенты использования СМО
ro[0] = basen_table[n-2][m-1] / basen_table[n-1][m-1]
for i in range(1, m):
    ro[i] = ro[0] * X[i]
print("Коэффициенты использования:", ro)

# Кол-во заявок в каждой СМО
L = [0.0] * m
for j in range(m):
    sum_coef = 0
    for i in range(n):
        sum_coef += pow(X[j], i+1) * basen_table[n-i][m-1]
    L[j] = sum_coef / basen_table[n][m-1]

print("Кол-во заявок в каждой СМО", L)

# Кол-во заявок в очереди каждой СМО
Q = [0.0] * m
for i in range(m):
    Q[i] = L[i] - ro [i]

print("Кол-во заявок в очереди к каждой СМО", Q)

# Время цикла
Tc = n * tj[0] / ro[0]
print("Среднее время цикла", Tc)

# Интенсивность потока заявок в СеМО
l = n / Tc

# Время пребывания заявок в каждой СМО
Tj = [0.0] * m
for i in range(m):
    Tj[i] = Tc * L[i] / n
print("Время пребывания заявок в каждой СМО: ", Tj)

# Среднее время ожидания заявок в очереди каждой СМО
Wj = [0.0]*m
for i in range(m):
    Wj[i] = Tj[i] - tj[i]
print("Среднее время ожидания заявок в очереди каждой СМО: ", Wj)