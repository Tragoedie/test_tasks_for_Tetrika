"""
Задача №1.
Дан массив чисел, состоящий из некоторого количества подряд идущих единиц, за которыми следует какое-то
количество подряд идущих нулей: 111111111111111111111111100000000.
Найти индекс первого нуля (то есть найти такое место, где заканчиваются единицы, и начинаются нули)
def task(array):
    pass

print(task("111111111110000000000000000"))
# >> OUT: 10
"""


def task(array):
    array = list(array)
    start = 0
    end = len(array) - 1
    while start < end:
        middle = (start + end) // 2
        if int(array[middle]) == 1:
            start = middle + 1
        else:
            end = middle - 1
    return start if int(array[start]) == 0 else end


# print(task("111111111110000000000000000"))
# >> OUT: 10
# print(task([1, 1, 1, 1, 1, 0]))


"""
В функцию передаются координаты двух противоположных вершин одного прямоугольника и двух противоположных
вершин второго прямоугольника. Найти, пересекаются ли эти прямоугольники?
"""


def task(x1, y1, x2, y2, x3, y3, x4, y4):
    # Нормализация прямоугольников
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    if x3 > x4:
        x3, x4 = x4, x3
    if y3 > y4:
        y3, y4 = y4, y3
    # Вычисление точек прямоугольника пересечения
    point_x1 = max(x1, x3)
    point_y1 = max(y1, y3)
    point_x2 = min(x2, x4)
    point_y2 = min(y2, y4)
    if point_x2 > point_x1 and point_y2 > point_y1:
        square = (point_x2 - point_x1) * (point_y2 - point_y1)  # Вычисление площади
        return True
    return False


print(task(1, 1, 2, 2, 3, 3, 4, 4))
print(task(5, 0, 0, 8, 2, 5, 8, 14))
print(task(2, 5, 8, 14, 5, 0, 0, 8))
print(task(0, 0, 2, 2, -1, -1, 1, 1))
