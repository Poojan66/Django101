# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from first_app.models import webpage,tblemp,access
# Register your models here.

admin.site.register(webpage)
admin.site.register(tblemp)
admin.site.register(access)