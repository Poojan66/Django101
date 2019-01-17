# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	first_name=models.CharField(max_length=246)
	last_name=models.CharField(max_length=246)
	email=models.EmailField(max_length=246,unique=True)
	def __str__(self):
		return str(self.first_name)
	
