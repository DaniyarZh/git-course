def main():
    x, y = 100, 100
    width, height = 200, 200
    draw_house(x, y, width, height)


def draw_house(x, y, width, height):
    '''
    Нарисовать домик ширины width и высоты height от опорной точки(x, y),
    которая находится в середине нижней точки фундамента.
    : param x: координата x середины домика
    : param y: координата y низа фундамента
    : param width: полная ширина домика (фундамент или вылет крыши включены)
    : param height: полная высота домика
    : return: None
    '''
    foundation_height = 0.05 * height  # высота фундамента 5% от всей
    walls_width = 0.9 * width
    walls_height = 0.5 * height
    roof_height = height - foundation_height - walls_height

    draw_house_foundation(x, y, width, foundation_height)
    draw_house_walls(x, y - foundation_height, walls_width, walls_height)
    draw_house_roof(x, y - foundation_height - walls_height, width, roof_height)
    print(x, y, width, height)
    pass


def draw_house_foundation(x, y, width, height):
    '''
    Нарисовать основание ширины  домика width и высоты height от опорной точки(x, y),
    которая находится в середине нижней точки фундамента.
    : param x: координата x середины фундамента
    : param y: координата y низа фундамента
    : param width: полная ширина фундамента
    : param foundation_height: полная высота фундамента
    : return: None
    '''
    pass
    print('Типа рисую фундамент', x, y, width, height)


def draw_house_walls(x, y, width, height):
    pass
    print('Типа рисую стены', x, y, width, height)


def draw_house_roof(x, y, width, height):
    pass
    print('Типа рисую крышу', x, y, width, height)


main()
