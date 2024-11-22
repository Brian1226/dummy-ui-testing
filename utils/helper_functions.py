import json
from faker import Faker


def read_test_data(file_path, key):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data[key]


def generate_random_registration_info():
    fake = Faker()
    return {
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'email': fake.email(),
        'password': fake.password()
    }

def generate_random_shipping_info():
    fake = Faker()
    return {
        'address': fake.address(),
        'city': fake.city(),
        'state': fake.state(),
        'zip_code': fake.zipcode(),
        'phone_number': fake.phone_number()
    }