N = int(input("Введите размер матрицы: "))

L = []
i = 0

while i < N:
    L.append([])
    j = 0

    while j < N:
        L[i].append(int(input("Введите элемент: ")))
        j += 1

    i += 1

flag = True
i = 0

while i < N:
    j = i + 1

    while j < N:
        if L[i][j] != L[j][i]:
            flag = False
            break

        j += 1

    if flag == False:
        break

    i += 1

if flag:
    print("Список L симметричный")
else:
    print("Список L не симметричный")
