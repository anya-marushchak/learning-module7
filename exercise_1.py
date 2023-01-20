
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
for j in list:
    print(j.name, j.surname, j.company_name,j.position, j.e_mail)
 

 #create class
class BusinessCard:
    def  __init__ (self, name, surname, e_mail):
        self.name = name
        self.surname = surname
        self.e_mail = e_mail


# creating list
BusinessCard_1 = BusinessCard(name = "Raymond J.", surname = "White", e_mail = "RaymondJWhite@armyspy.com")
BusinessCard_2 = BusinessCard(name = "David L.", surname = "Riemer", e_mail = "DavidLRiemer@dayrep.com")
BusinessCard_3 = BusinessCard(name = "George V.", surname = "Glisson", e_mail = "GeorgeVGlisson@rhyta.com")
BusinessCards = [BusinessCard_1, BusinessCard_2, BusinessCard_3]


by_name = sorted(BusinessCards, key=lambda BusinessCard: BusinessCard.name)
by_surname = sorted(BusinessCards, key=lambda BusinessCard: BusinessCard.surname)
by_e_mail = sorted(BusinessCards, key=lambda BusinessCard: BusinessCard.e_mail)

lambda BusinessCards: BusinessCards.name
print(by_name)






 