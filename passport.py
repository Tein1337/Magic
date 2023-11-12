class Passport:
    def __init__(self, first_name, last_name, country, date_of_birth, numb_of_passport):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.country = country
        self.numb_of_passport = numb_of_passport

    def printInfo(self):
        print(f'''\nFullname: {self.first_name} {self.last_name}
Date of birth: {self.date_of_birth}
County: {self.country}
Passport number: {self.numb_of_passport}''')

    def __repr__(self):
        return f'name {self.first_name} {self.last_name}, Passport: {self.numb_of_passport}'

class ForeignPassport(Passport):

    def __init__(self, first_name, last_name, country, date_of_birth, numb_of_passport, visa):
        super().__init__(first_name, last_name, country, date_of_birth, numb_of_passport)
        self.visa = visa

    def printInfo(self):
        super().printInfo()
        print(f'Visa: {self.visa}')


MFC = []
p = Passport('Ivan', 'Ivanov', 'Russia', '16.02.2000', '8221 457896')
p.printInfo()
MFC.append(p)
fp = ForeignPassport('Matthew', 'Young', 'USA', '6.11.2005', '1233 812499', 'Russia')
fp.printInfo()
MFC.append(fp)
print(MFC)
for item in MFC:
    item.printInfo()
