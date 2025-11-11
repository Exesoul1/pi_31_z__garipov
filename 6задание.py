class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x  # левая нижняя точка
        self.y = y
        self.w = w  # ширина
        self.h = h  # высота

    # методы получения атрибутов
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_w(self):
        return self.w

    def get_h(self):
        return self.h

    # метод пересечения с другим прямоугольником
    def intersection(self, other):
        # координаты правого верхнего угла
        x1_max = self.x + self.w
        y1_max = self.y + self.h
        x2_max = other.x + other.w
        y2_max = other.y + other.h

        # координаты пересечения
        inter_x = max(self.x, other.x)
        inter_y = max(self.y, other.y)
        inter_x_max = min(x1_max, x2_max)
        inter_y_max = min(y1_max, y2_max)

        inter_w = inter_x_max - inter_x
        inter_h = inter_y_max - inter_y

        # если пересечение пустое или является точкой/отрезком
        if inter_w <= 0 or inter_h <= 0:
            return None

        return Rectangle(inter_x, inter_y, inter_w, inter_h)


rect1 = Rectangle(0, 0, 10, 10)
rect2 = Rectangle(5, 5, 10, 10)
rect3 = rect1.intersection(rect2)

if rect3 is None:
    print('No intersection')
else:
    print(rect3.get_x(), rect3.get_y(), rect3.get_w(), rect3.get_h())