def print_table(table, n):
    print("Таблица Базена:")
    for i in range(n+1):
            print(basen_table[i])

print("Задача 1")

n = 5 # Кол-во заявок
m = 5 # Кол-во фаз
tj = [1, 1, 1, 2, 4] # Время обработки заявок в ОА
X = [1.0] # Коэффициенты Базена
basen_table = []

for t in tj[1:4]:
    X.append( t/tj[0] * X[0])
X.append(0.5 * tj[4]/tj[0] * X[0]) # Расчет последнего столбца
print("Коэффициенты Базена: ", X)

basen_table.append([1.0] * m) # Первая строка таблицы - единицы
for i in range(n):
    basen_table.append([1.0]+[0.0]*(m-1)) # Первый столбец - единицы

for i in range(1, m-1):
    for j in range(1, n+1):
        basen_table[j][i] = basen_table[j][i-1] + X[i] * basen_table[j-1][i]

# В пятой фазе два ОА, поэтому считаем по другой формуле
for i in range(1, n+1):
    basen_table[i][m-1] = basen_table[i][m-2] + X[4]*(basen_table[i-1][m-2] + basen_table[i-1][m-1])

print_table(basen_table, n)

# Расчет коэффициентов использования
ro = [0.0] * 5 # Коэффициенты использования СМО
ro[0] = basen_table[n-1][m-1] / basen_table[n][m-1]
for i in range(1, m):
    ro[i] = ro[0] * X[i]
print("Коэффициенты использования:", ro)

# Кол-во заявок в каждой СМО
L = [0.0] * m
for j in range(m-1):
    sum_coef = 0
    for i in range(n):
        sum_coef += pow(X[j], i+1) * basen_table[n-i-1][m-1]
    L[j] = sum_coef / basen_table[n][m-1]

# Отдельно считаем 5ую фазу
sum_coef = 0
for i in range(n):
    sum_coef += pow(X[j], i+1) * (basen_table[n-i-1][m-1] + basen_table[n-i-1][m-2])
L[4] = sum_coef / basen_table[n][m-1]

print("Кол-во заявок в каждой СМО:", L)

# Кол-во заявок в очереди каждой СМО
Q = [0.0] * m
for i in range(m-1):
    Q[i] = L[i] - ro[i]
Q[4] = L[4] - 2*ro[4] # 5ая фаза

print("Кол-во заявок в очереди к каждой СМО", Q)

# Время цикла
Tc = n * tj[0] / ro[0]
print("Среднее время цикла", Tc)

# Интенсивность потока заявок в СеМО
l = n / Tc
print("Интенсивность потока заявок в СеМО: ", l)

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