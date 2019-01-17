# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class tblemp(models.Model):
	emp_name=models.CharField(max_length=264,unique=True)
	
	def __str__(self):
		return self.emp_name

class webpage(models.Model):
	top=models.ForeignKey(tblemp)
	name=models.CharField(max_length=264,unique=True)
	url=models.URLField(unique=True)

	def __str__(self):
		return self.name

class access(models.Model):
	name=models.ForeignKey(webpage)
	date=models.DateField()

	def __str__(self):
		return str(self.date)

