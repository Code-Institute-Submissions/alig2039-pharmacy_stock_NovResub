from http import client
from django.contrib import admin
from .models import *

admin.site.register(Stock)
admin.site.register(Sales)
admin.site.register(Customer)
admin.site.register(Supplier)