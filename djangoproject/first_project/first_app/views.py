# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from first_app.models import webpage,tblemp,access

# Create your views here.

def index(request):
	ls=access.objects.order_by('date')
	mydict={'records':ls}

	return render(request,'first_app/index.html',context=mydict)
