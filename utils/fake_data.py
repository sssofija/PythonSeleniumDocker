from faker import Faker

fake = Faker()


def generate_user_data():
    full_name = fake.name()
    email = fake.email()
    current_address = fake.address().replace("\n", ", ")
    permanent_address = fake.address().replace("\n", ", ")

    return {
        "full_name": full_name,
        "email": email,
        "current_address": current_address,
        "permanent_address": permanent_address
    }

def generate_webtable_user_data():
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "age": fake.random_int(min=18, max=65),
        "salary": fake.random_int(min=30000, max=150000),
        "department": fake.job()
    }
