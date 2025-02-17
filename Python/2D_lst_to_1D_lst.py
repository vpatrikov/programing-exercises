# Въвеждаме двумерния масив A
A = [
    [4, -1, 3],
    [2, -3, 5],
    [-2, 6, -4]
]

n = len(A)  # Размер на масива (предполага се квадратна матрица)

# 1. Намираме минималните елементи от всеки ред
min_elements = [min(row) for row in A]

# 2. Изчисляваме сумата на елементите по главния диагонал
main_diagonal_sum = sum(A[i][i] for i in range(n))

# 3. Преброяваме отрицателните елементи по вторичния диагонал
secondary_diagonal_neg_count = sum(1 for i in range(n) if A[i][n - i - 1] < 0)

# 4. Създаваме масива B
B = min_elements + [main_diagonal_sum, secondary_diagonal_neg_count]

# 5. Сортираме масива B с Bubble Sort
for i in range(len(B)):
    for j in range(0, len(B) - i - 1):
        if B[j] > B[j + 1]:
            # Разменяме елементите
            B[j], B[j + 1] = B[j + 1], B[j]

# Извеждаме резултата
print("Минимални елементи от редовете на A:", min_elements)
print("Сума на елементите по главния диагонал:", main_diagonal_sum)
print("Брой отрицателни елементи по вторичния диагонал:", secondary_diagonal_neg_count)
print("Сортиран масив B:", B)
