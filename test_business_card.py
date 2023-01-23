
#defining function to create fake cards

from faker import Faker

faker = Faker()


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
list_1 = BaseContact(name = "Raymond J.", surname = "White",phone_number = "+48589589525",e_mail = "RaymondJWhite@armyspy.com" )


# creating list to class BusinessContact
list_2 = BusinessContact(name ="Raymond J.",surname="White",phone_number="+48589589525",e_mail = "RaymondJWhite@armyspy.com",company_name = "Laura Ashley Mother & Child",position = "Administrative lead",company_number = "+48789252123")


# defining function to choose the neccessary card
def contact():
    while True:
        action = input ("Choose card: ")
        if action == "Basecontact":
            
                print(f'I am connecting to {list_1.name} {list_1.surname} number {list_1.phone_number} .')

        if action == "Businesscontact":
            
                print(f'I am connecting to {list_2.name} {list_2.surname} number {list_2.company_number} .')



def create_contacts():
   
    type = faker.type
    quantity = faker.quantity()
    list_3 = [faker.type, faker.quality] 
    list_1.append(list_3)
    list_2.append(list_3)
    print(list_1)
    print(list_2)

def label_length():
    length = list_1.name + list_2.surname 
    print (len(length))

label_length()

create_contacts()

contact()