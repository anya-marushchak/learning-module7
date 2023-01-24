#create class
class BusinessCard:
    def  __init__ (self, name, surname, e_mail):
        self.name = name
        self.surname = surname
        self.e_mail = e_mail
    
    def __str__ (self):
        return self.name 

    def __repr__ (self):
        return self.name

    def __str__ (self):
        return self.surname

    def __repr__ (self):
        return self.surname

# creating list
businessCard_1 = BusinessCard(name = "Raymond J.", surname = "White", e_mail = "RaymondJWhite@armyspy.com")
businessCard_2 = BusinessCard(name = "David L.", surname = "Riemer", e_mail = "DavidLRiemer@dayrep.com")
businessCard_3 = BusinessCard(name = "George V.", surname = "Glisson", e_mail = "GeorgeVGlisson@rhyta.com")
businessCards = [businessCard_1, businessCard_2, businessCard_3]


by_name = sorted(businessCards, key=lambda x: x.name)
by_surname = sorted(businessCards, key=lambda x: x.surname)
by_e_mail = sorted(businessCards, key=lambda x: x.e_mail)


for card in by_name:
    print (card) 
    
for card in by_surname:
    print (card) 











 