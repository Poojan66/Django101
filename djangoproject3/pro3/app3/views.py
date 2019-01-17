# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from . import forms 
# Create your views here.

def index(request) :
	return render(request,'app3/index.html')
