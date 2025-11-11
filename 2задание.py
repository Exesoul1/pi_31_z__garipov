class LeftParagraph:
    def __init__(self, width):
        self.width = width
        self.line = ""

    def add_word(self, word):
        if not self.line:  # если строка пустая
            self.line = word
        else:
            # проверяем, влезет ли слово с пробелом
            if len(self.line) + 1 + len(word) <= self.width:
                self.line += " " + word
            else:
                print(self.line)
                self.line = word

    def end(self):
        if self.line:
            print(self.line)
            self.line = ""


class RightParagraph:
    def __init__(self, width):
        self.width = width
        self.line = ""

    def add_word(self, word):
        if not self.line:
            self.line = word
        else:
            if len(self.line) + 1 + len(word) <= self.width:
                self.line += " " + word
            else:
                print(self.line.rjust(self.width))
                self.line = word

    def end(self):
        if self.line:
            print(self.line.rjust(self.width))
            self.line = ""


lp = LeftParagraph(8)
lp.add_word('abc')
lp.add_word('defg')
lp.add_word('hi')
lp.add_word('jklmnopq')
lp.add_word('r')
lp.add_word('stuv')
lp.end()
print()

rp = RightParagraph(8)
rp.add_word('abc')
rp.add_word('defg')
rp.add_word('hi')
rp.add_word('jklmnopq')
rp.add_word('r')
rp.add_word('stuv')
rp.end()