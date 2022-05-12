def main():
    play()

# Запуск игры
def play():    
    field_size = get_field_size()
    field = fill_field(field_size)
    show_field(field_size, field)
    gamer = 'O'
    step_remain = field_size**2		
    while True:
        if gamer == 'X':
            gamer = 'O'
        else:
            gamer = 'X'
        step_remain = move(gamer, step_remain, field_size, field)
        show_field(field_size, field)
        if check_win(gamer, field_size, field):
            print('Игра окончена')
            print('Победил игрок', gamer)	
            break	
        elif check_draw(step_remain):
            print('Ходы закончились. Ничья!')
            break

	
# Функция запроса размера игрового поля
def get_field_size():
    print('Добро пожаловать в игру "Крестики-нолики"!')
    while True:
        x = input('Выберите размер поля по вертикали и горизонтали в диапазоне от 3 до 5: ')
        if x != '' and x.isdigit():
            if int(x) in range(3, 6):
                return int(x)
        else:
            print('Диапазон не удовлетворяет условию. Должен быть от 3 до 5.')

			
# Заполнение игрового поля		
def fill_field(field_size):
    return [['-'] * field_size for _ in range(field_size)]			
			

# Процедура вызова поля на экран
def show_field(field_size, field):
    for i in range(field_size + 1):
        print(i, end=' ')
    print()
    for row in range(field_size):
        print(row + 1, *field[row])			
	
	


# Функция проверки выиграл игрок или нет
def check_win(player, field_size, field):
    trans_field = [[field[col][row] for col in range(field_size)] for row in range(field_size)]
    #check_draw()
    return any([
		check_vertical_gorizontal(field, player),
        check_vertical_gorizontal(trans_field, player),		
        check_diagonal(player, field_size, field),
    ])

	
# Проверка по диагоналям
def check_diagonal(pl, field_size, field):
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
def move(player, max_steps, field_size, field):
    while True:
        while True:
            lst = input(
                f'Ходит {player}. Введите координаты x, y через пробел в диапазоне от 1 до {field_size}: ').split()
            if len(lst) != 2:
                print('Введены неверные координаты, попробуйте еще раз.')
            else:
                if check_coordinates_type(lst[0]) and check_coordinates_type(lst[1]):
                    break
                else:
                    print('Координаты должны состоять только из целых чисел, попробуйте еще раз.')
        x, y = list(map(lambda i: int(i) - 1, lst))
        if check_coordinates_range(x, field_size) and check_coordinates_range(y, field_size):
            if field[y][x] == '-':
                field[y][x] = player
                max_steps -= 1
                return max_steps
            else:
                print('Поле уже занято. Введите другие координаты.')
        else:
            print('Ваши координаты выходят за пределы игрового поля. Попробуйте еще раз.')

def check_coordinates_type(coord):
    return coord.isdigit()
    

def check_coordinates_range(coord, field_size):
    return coord in range(field_size)
	
if __name__ == '__main__':
    main()			
