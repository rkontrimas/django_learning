import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()
from appTwo.models import Person
from faker import Faker

fakegen = Faker()

def populate_person(n=5):
    for entry in range(n):
        fake_first_name=fakegen.name_male()
        fake_last_name=fakegen.last_name()
        fake_email=fakegen.free_email()

        add_person = Person.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]


if __name__ == '__main__':
    print('populating script!')
    populate_person(20)
