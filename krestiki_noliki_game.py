print('Добро пожаловать в игру "Крестики-нолики"!')


# Функция проверки размера поля, которое задает игрок
def def_field_size():
    while True:
        x = input('Выберите размер поля по вертикали и горизонтали в диапазоне от 3 до 5: ')
        if x != '':
            if int(x) in range(3, 6):
                return int(x)
        else:
            print('Диапазон не удовлетворяет условию. Должен быть от 3 до 5.')


field_size = def_field_size()
field = [['-'] * field_size for _ in range(field_size)]
gamer = 'O'
step = 0
max_steps = field_size**2

# Процедура вызова поля
def show_field():
    for i in range(field_size + 1):
        print(i, end=' ')
    print()
    for row in range(field_size):
        print(row + 1, *field[row])


show_field()


# Процедура проверки выиграл игрок или нет
def check_win(player):
    trans_field = [[field[col][row] for col in range(field_size)] for row in range(field_size)]
    #check_draw()
    return any([
        # проверка по строкам
        any(map(lambda row: all([el == player for el in row]), field)),
        # проверка по диагоналям
        check_diagonal(player),
        # проверка по вертикалям
        any(map(lambda row: all([el == player for el in row]), trans_field)),
    ])


def check_diagonal(pl):
    u_d, d_u = [], []
    for x in range(field_size):
        u_d.append(field[x][x] == pl)
        d_u.append(field[field_size - 1 - x][x] == pl)
    return any([all(u_d), all(d_u)])


# Процедура хода
def move(player):
    global step
    while True:
        while True:
            lst = input(
                f'Ходит {player}. Введите координаты x, y через пробел в диапазоне от 1 до {field_size}: ').split()
            if len(lst) != 2:
                print('Введены неверные координаты, попробуйте еще раз.')
            else:
                break
        x, y = list(map(lambda i: int(i) - 1, lst))
        if x in range(field_size) and y in range(field_size):
            if field[y][x] == '-':
                field[y][x] = player
                step += 1
                break
            else:
                print('Поле уже занято. Введите другие координаты.')
        else:
            print('Ваши координаты выходят за пределы игрового поля. Попробуйте еще раз.')


# Игра
while True:
    if gamer == 'X':
        gamer = 'O'
    else:
        gamer = 'X'
    move(gamer)
    show_field()
    if check_win(gamer):
        print('Игра окончена')
        print('Победил игрок', gamer)	
        break
    elif step == max_steps:
        print('Ходы закончились. Ничья!')
        break