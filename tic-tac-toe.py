board = [["-" for _ in range(3)] for _ in range(3)]

def f_board():
    print('  0 1 2')
    for i in range(len(board)):
        print(i, *board[i])

def check_input():
    while True:
        coordinate = input("Введите две координаты:").split()

        if len(coordinate) != 2:
            print("Требуются ДВЕ координаты")
            continue
        if not(coordinate[0].isdigit() and coordinate[1].isdigit()):
            print("Требуется номер")
            continue
        x, y = map(int, coordinate)
        if x not in range(3) or y not in range(3):
            print("Нарушение ограничительных условий от 0 до 2 включительно")
            continue
        if board[x][y] != "-":
            print("Ячейка занята, повторите попытку")
            continue
        break
    return x, y

def game_end():
    win_combo = (((0, 0), (0, 1), (0, 2)),
                 ((1, 0), (1, 1), (1, 2)),
                 ((2, 0), (2, 1), (2, 2)),
                 ((0, 0), (1, 1), (2, 2)),
                 ((0, 2), (1, 1), (2, 0)))
    for position in win_combo:
        if board[position[0][0]][position[0][1]] == board[position[1][0]][position[1][1]] == board[position[2][0]][position[2][1]] != "-":
            return board[position[0][0]][position[0][1]]
    return None

def game_start():
    correct_player = 'x'
    count = 0
    while True:
        if count == 9:
            print("Ничья!")
            break
        f_board()
        x, y = check_input()
        board[x][y] = correct_player
        if correct_player == 'x':
            correct_player = 'o'
        else:
            correct_player = 'x'
        count += 1
        win = game_end()
        if win:
            print(f"Игрок {win} выиграл!")
            break
    f_board()

game_start()