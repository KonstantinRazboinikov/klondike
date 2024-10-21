# Создание поля
field = []
[field.append(["e"] * 12) for i in range(12)]

player = 1  # Номер текущего игрока
winner = 0  # В эту переменную запишется победитель
while winner == 0:

    # Визуализация поля
    print("Сейчас ходит игрок", player, "\n")

    print("      1  2  3  4  5  6  7  8  9  10")
    for i in range(1, 11):

        if i == 10:
            print("  10 ", end="")
        else:
            print(" ", i, end="  ")

        for j in range(1, 11):
            if field[i][j] == "e":
                print("[ ]", end="")
            else:
                print("[x]", end="")
        print()

    # Ввод координат и их проверка их правильности.

    while True:
        print("\n\nСначала введите номер столбца, потом номер строки (через пробел)\n")
        сord = input("Введите координаты новой фишки: ")
        result = 1
        data = сord.split()

        if len(data) == 2:
            if data[0] in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
                if data[1] in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
                    x, y = int(data[0]), int(data[1])
                    if field[y][x] == "f":
                        result = 2
                    else:
                        result = 0
        if result == 0:
            break
        if result == 1:
            print("\n - - Ошибка ввода. Попробуйте еще раз. - -")
        if result == 2:
            print("\n - - На этих координатах уже есть фишка. Введите другие координаты. - -")

    # Постановка фишки

    field[y][x] = "f"

    # Реализация механики проверки на наличие "змеек" из трех фишек на поле

    for i in range(1, 11):
        for j in range(1, 11):
            if field[i][j] == "f":
                count = 0

                if field[i - 1][j] == "f":
                    count += 1
                if field[i + 1][j] == "f":
                    count += 1
                if field[i][j - 1] == "f":
                    count += 1
                if field[i][j + 1] == "f":
                    count += 1
                if field[i - 1][j - 1] == "f":
                    count += 1
                if field[i + 1][j - 1] == "f":
                    count += 1
                if field[i - 1][j + 1] == "f":
                    count += 1
                if field[i + 1][j + 1] == "f":
                    count += 1

                if count >= 2:
                    print(player, "ИГРОК ПРОИГРАЛ")
                    if player == 2:
                        winner = 1
                    else:
                        winner = 2
                    break
        if winner != 0:
            break
    if winner != 0:
        break

    # Смена игрока

    if player == 1:
        player = 2
    else:
        player = 1

print("ПОБЕДИЛ ИГРОК", winner)