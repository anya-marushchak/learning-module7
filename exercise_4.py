#create class
class BusinessCard:
    def  __init__ (self, name, surname, company_name, position, e_mail):
        self.name = name
        self.surname = surname
        self.company_name = company_name
        self.position = position
        self.e_mail = e_mail


# creating list
list = []

# appending instances to list
list.append(BusinessCard("Raymond J.","White","Laura Ashley Mother & Child","Administrative lead","RaymondJWhite@armyspy.com"))
list.append(BusinessCard("David L.","Riemer","White Tower Hamburgers","Occupational analyst","DavidLRiemer@dayrep.com"))
list.append(BusinessCard("George V.","Glisson","Our Own Hardware","Cutting, punching, and press machine operator","GeorgeVGlisson@rhyta.com"))

# Accessing object value using a for loop


def contact():
    for j in list:
        print(f'I am connecting to {j.name}, {j.surname}, {j.company_name},{j.position}, {j.e_mail}')
 
contact()

 