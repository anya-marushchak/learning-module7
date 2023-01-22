#create class
class BusinessCard:
    def  __init__ (self, name, surname, e_mail):
        self.name = name
        self.surname = surname
        self.e_mail = e_mail


# creating list

x_1 = BusinessCard(name = "Raymond J.", surname = "White", e_mail = "RaymondJWhite@armyspy.com")
x_2 = BusinessCard(name = "David L.", surname = "Riemer", e_mail = "DavidLRiemer@dayrep.com")
x_3 = BusinessCard(name = "George V.", surname = "Glisson", e_mail = "GeorgeVGlisson@rhyta.com")
x = [x_1,x_2,x_3]

def __str__(self):
    return f'{self.name} {self.surname} {self.e_mail}'
print(x)

by_name = sorted(x, key= lambda x: x.name)
print(by_name)

by_surname = sorted(x, key=lambda x: x.surname)
by_e_mail = sorted(x, key=lambda x: x.e_mail)















 