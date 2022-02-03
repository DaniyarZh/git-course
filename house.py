
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
    print(x, y, width, height)
    pass

x, y = 100, 100
width, height = 200, 200
t = 1
draw_house(x, y, width, height)
