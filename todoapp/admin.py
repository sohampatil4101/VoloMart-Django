from django.contrib import admin
from todoapp.models import Contact
from todoapp.models import Owner
from todoapp.models import Finalowner
from todoapp.models import Item

# Register your models here.

admin.site.register(Contact)
admin.site.register(Owner)
admin.site.register(Finalowner)
admin.site.register(Item)
