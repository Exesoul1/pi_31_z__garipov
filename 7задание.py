class Table:
    def __init__(self, rows, cols):
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    # чтение значения
    def get_value(self, row, col):
        if 0 <= row < self.n_rows() and 0 <= col < self.n_cols():
            return self.data[row][col]
        return None

    # запись значения
    def set_value(self, row, col, value):
        self.data[row][col] = value

    # число строк
    def n_rows(self):
        return len(self.data)

    # число колонок
    def n_cols(self):
        return len(self.data[0]) if self.data else 0

    # удалить строку
    def delete_row(self, row):
        if 0 <= row < self.n_rows():
            self.data.pop(row)

    # удалить колонку
    def delete_col(self, col):
        if 0 <= col < self.n_cols():
            for r in self.data:
                r.pop(col)

    # добавить строку с индексом row
    def add_row(self, row):
        if 0 <= row <= self.n_rows():
            new_row = [0] * self.n_cols()
            self.data.insert(row, new_row)

    # добавить колонку с индексом col
    def add_col(self, col):
        if 0 <= col <= self.n_cols():
            for r in self.data:
                r.insert(col, 0)


tab = Table(1, 1)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

tab.set_value(0, 0, 1000)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

for i in range(-1, tab.n_rows() + 1):
    for j in range(-1, tab.n_cols() + 1):
        print(tab.get_value(i, j), end=' ')
    print()
print()

tab.add_row(0)
tab.add_row(2)
tab.add_col(0)
tab.add_col(2)

tab.set_value(0, 0, 2000)
tab.set_value(0, 2, 3000)
tab.set_value(2, 0, 4000)
tab.set_value(2, 2, 5000)

for i in range(-1, tab.n_rows() + 1):
    for j in range(-1, tab.n_cols() + 1):
        print(tab.get_value(i, j), end=' ')
    print()
print()