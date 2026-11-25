N = int(input("Введите размер матрицы: "))

L = []
i = 0

while N > i:
    row = []
    j = 0

    while N > j:
        x = int(input("Введите элемент: "))
        row.append(x)
        j = j + 1

    L.append(row)
    i = i + 1

flag = 1
i = 0

while N > i:
    j = 0

    while N > j:
        if L[i][j] != L[j][i]:
            flag = 0

        j = j + 1

    i = i + 1

if flag == 1:
    print("Список L симметричный")
else:
    print("Список L не симметричный")
