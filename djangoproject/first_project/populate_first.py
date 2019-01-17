import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')
import django
django.setup()

#fake script
import random
from first_app.models import access,tblemp,webpage
from faker import Faker
fake=Faker()
tops=['search','social','entertainment']

def add_top():
	t=tblemp.objects.get_or_create(emp_name=random.choice(tops))[0]
	t.save()
	return t

def populate(n=5):
	for entry in range(n):
		#get topic for entry
		top=add_top()
		#craete fake data
		fake_url=fake.url()
		fake_date=fake.date()
		fake_name=fake.company()

		#create new web page entry
		webpg=webpage.objects.get_or_create(top=top,url=fake_url,name=fake_name)[0]

		#fake access
		acc=access.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == '__main__':

	print('populating script')
	populate(20)
	print('compelte')
				