import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","pro2.settings")
import django
django.setup()
from app2.models import User
from faker import Faker
fake=Faker()


def pop(n=5):
	for entry in range(n):
		fake_name=fake.name().split()
		fake_fname=fake_name[0]
		fake_lname=fake_name[1]
		fake_email=fake.email()

		#create
		user=User.objects.get_or_create(first_name=fake_fname,last_name=fake_lname,email=fake_email)[0]

if __name__ == '__main__':
	print("populating")
	pop(20)
	print("complete")