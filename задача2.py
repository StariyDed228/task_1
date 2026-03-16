def rectangle_area(a, b = None):
    #если b не задан, то считаем квадрат
    if b is None:
        b = a
    if a <= 0 or b <= 0:
        return 0
    return a * b
print(rectangle_area(5))
print(rectangle_area(5, 6))
