def main():
    play()

	
# Функция запроса размера игрового поля
def get_field_size():
    while True:
        x = input('Выберите размер поля по вертикали и горизонтали в диапазоне от 3 до 5: ')
        if x != '' and x.isdigit():
            if int(x) in range(3, 6):
                return int(x)
        else:
            print('Диапазон не удовлетворяет условию. Должен быть от 3 до 5.')

			
# Заполнение игрового поля		
def fill_field():
    return [['-'] * field_size for _ in range(field_size)]			
			

# Процедура вызова поля на экран
def show_field():
    for i in range(field_size + 1):
        print(i, end=' ')
    print()
    for row in range(field_size):
        print(row + 1, *field[row])			
	
	
# Запуск игры
def play():
    print('Добро пожаловать в игру "Крестики-нолики"!')
    gamer = 'O'
    step_remain = field_size**2		
    while True:
        if gamer == 'X':
            gamer = 'O'
        else:
            gamer = 'X'
        step_remain = move(gamer, step_remain)
        show_field()
        if check_draw(step_remain):
            print('Ходы закончились. Ничья!')
            break
        elif check_win(gamer):
            print('Игра окончена')
            print('Победил игрок', gamer)	
            break	


# Функция проверки выиграл игрок или нет
def check_win(player):
    trans_field = [[field[col][row] for col in range(field_size)] for row in range(field_size)]
    #check_draw()
    return any([
		check_vertical_gorizontal(field, player),
        check_vertical_gorizontal(trans_field, player),		
        check_diagonal(player),
    ])

	
# Проверка по диагоналям
def check_diagonal(pl):
    u_d, d_u = [], []
    for x in range(field_size):
        u_d.append(field[x][x] == pl)
        d_u.append(field[field_size - 1 - x][x] == pl)
    return any([all(u_d), all(d_u)])

	
# Проверка по вертикалям и горизонталям	
def check_vertical_gorizontal(checking_field, pl):
    return any(map(lambda row: all([el == pl for el in row]), checking_field))

	
# Проверка на ничью
def check_draw(steps):
    return not steps

	
# Процедура хода и возврата количества оставшихся ходов
def move(player, max_steps):
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
                max_steps -= 1
                return max_steps
            else:
                print('Поле уже занято. Введите другие координаты.')
        else:
            print('Ваши координаты выходят за пределы игрового поля. Попробуйте еще раз.')

			
if __name__ == '__main__':
    field_size = get_field_size()
    field = fill_field()
    show_field()
    main()
	
			