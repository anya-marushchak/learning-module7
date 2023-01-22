#creating class
class BaseContact:
    def  __init__ (self, name, surname, phone_number, e_mail):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.e_mail = e_mail


#creating subclass
class BusinessContact(BaseContact):
    def __init__(self, company_name, position, company_number, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.position = position
        self.company_name = company_name
        self.company_number = company_number


# creating list to class BaseContact
list_1 = []

# appending instances to list
list_1.append(BaseContact("Raymond J.","White","+48589589525","RaymondJWhite@armyspy.com"))

# creating list to class BusinessContact
list_2 = []

# appending instances to list
list_2.append(BusinessContact("Raymond J.","White","+48589589525","RaymondJWhite@armyspy.com","Laura Ashley Mother & Child","Administrative lead","+48789252123"))

# defining function to choose the neccessary card
def contact():
    while True:
        action = input ("Choose card: ")
        if action == "Basecontact":
            for j in list_1:
                print(f'I am connecting to {j.name} {j.surname} number {j.phone_number} .')

        if action == "Businesscontact":
            for j in list_2:
                print(f'I am connecting to {j.name} {j.surname} number {j.company_number} .')

contact()