# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from app2.models import User
# Create your views here.

def index(request):
	return render(request,'app2/index.html')
def users(request):
	user_list=User.objects.order_by('first_name')
	dict={'users':user_list}
	return render(request,'app2/users.html',context=dict)	