import random

from data.data import Person
from faker import Faker   # it gives randon values

faker_en = Faker('En')

def generated_person():
    return Person(
        first_name=faker_en.first_name(),    #method faker gives me random first name
        last_name=faker_en.last_name(),     #method faker gives me random last name
        email=faker_en.email(),
        current_address=faker_en.address(),
        mobile=faker_en.msisdn(),
        subject='English'
    )

def generated_file():
    path = rf'D:\Python_Marshall_ARTVLAD(Auto)\test{random.randint(10,100)}.txt'
    file = open(path, 'w')
    file.write(f'Helloword{random.randint(23, 100)}')
    file.close()
    return path
