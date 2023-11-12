class Equipment:

    def __init__(self, name, make, year):
        self.name = name
        self.make = make
        self.year = year

    def action(self):
        return 'Не определено'

    def __str__(self):
        return f'{self.name}, {self.make}, {self.year}'

    def __le__(self, other):
        if not isinstance(other, Equipment):
            raise TypeError
        return self.year <= other.year


class Printer(Equipment):

    def __init__(self, series, name, make, year):
        super().__init__(name, make, year)
        self.series = series

    def action(self):
        return 'Печатает'

    def __str__(self):
        return f'{self.series} {self.name}, {self.make}, {self.year}'


class Scaner(Equipment):

    def __init__(self, series, name, make, year):
        super().__init__(name, make, year)
        self.series = series

    def action(self):
        return 'Сканирует'


class Xerox(Equipment):

    def __init__(self, name, make, year):
        super().__init__(name, make, year)

    def action(self):
        return 'Копирует и печатает на листочек'

def allitems(sklad):
    for item in sklad:
        print(item)

def get_items(sklad, ename):
    for item in sklad:
        if isinstance(item, ename):
            print(item)


sklad = []
e = Equipment('Noname', 'X', 2000)
sklad.append(e)
s = Printer('asd', 'asd', 'asdasd', 1214)
sklad.append(s)
x = Xerox('asd', 'asd', 123123)
sklad.append(x)
e = Equipment('N12', '1223', 2012300)
sklad.append(e)
s = Printer('aasgggd', 'asgsdgsd', 'asdasd', 112312214)
sklad.append(s)
x = Xerox('afdgsd', 'aasfasgsd', 112321323123)
sklad.append(x)
# allitems(sklad)
get_items(sklad, Equipment)
