one_color = input('Введите первый цвет')
two_color = input('Введите второй цвет')
color = ['красный','синий','желтый']
res_color = 'Не верно введены данные'
if one_color in color and two_color in color:
    if one_color == color [0]:
        if two_color == color [1]:
            res_color = 'фиолетовый'
        elif two_color == color [2]:
            res_color = 'оранжевый'
        else:
            res_color = one_color

    if one_color == color[1]:
        if two_color == color[0]:
            res_color = 'фиолетовый'
        elif two_color == color[2]:
             res_color = 'зеленый'
        else:
            res_color = one_color

    if one_color == color[2]:
        if two_color == color[0]:
            res_color = 'оранжевый'
        elif two_color == color[1]:
            res_color = 'зеленый'
        else:
            res_color = one_color

print(res_color)