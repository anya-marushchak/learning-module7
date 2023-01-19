from faker import Faker

faker = Faker()


def Business_card():
    for i in range(6):
        name = faker.name()
        job = faker.job()
        company = faker.company()
        email = faker.email()

        print(f'{name}, {job}, {company},{email}')

Business_card()

