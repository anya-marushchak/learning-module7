#creating class
class BaseContact:
    def  __init__ (self, name, surname, phone_number, e_mail, type, quantity):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.type = type
        self.quantity = quantity


    # creating @property decorator for BaseContact
    @property
    def name_size(self):
        length = self.name +self.surname
        return len(length)

    # creating method to compare type and quantity attributes
    def __eq__(self, other):
        return (
            self.type == other.type and
            self.quantity == other.quantity 
        )

#creating subclass
class BusinessContact(BaseContact):
    def __init__(self, company_name, position, company_number, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.position = position
        self.company_name = company_name
        self.company_number = company_number

    # creating @property decorator for BusinessContact
    @property
    def name_size(self):
        length = self.name +self.surname
        return len(length)
    


# creating list to class BaseContact
list_1 = BaseContact(name = "Raymond J.", surname = "White",phone_number = "+48589589525",e_mail = "RaymondJWhite@armyspy.com" ,type = "base contact", quantity = 1 )


# creating list to class BusinessContact
list_2 = BusinessContact(name ="Raymond J.",surname="White",phone_number="+48589589525",e_mail = "RaymondJWhite@armyspy.com",type = "business contact" ,company_name = "Laura Ashley Mother & Child",position = "Administrative lead",company_number = "+48789252123" , quantity = 1)

print(list_1 == list_2)

# defining function to choose the neccessary card
def contact():
    while True:
        action = input ("Choose card: Basecontact or Businesscontact: ")
        if action == "Basecontact":
            
                print(f'I am connecting to {list_1.name} {list_1.surname} with the length of {list_1.name_size} words in name and surname, number {list_1.phone_number} .')
 
        if action == "Businesscontact":
            
                print(f'I am connecting to {list_2.name} {list_2.surname} with the length of {list_2.name_size} words in name and surname, number {list_2.company_number}.')


contact()



    

