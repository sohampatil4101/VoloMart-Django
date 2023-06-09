from django.contrib import admin
from todoapp.models import Contact
from todoapp.models import Owner
from todoapp.models import Finalowner
from todoapp.models import Item
from todoapp.models import Order_placed
from todoapp.models import Customer
from todoapp.models import Expired
from todoapp.models import Save
from todoapp.models import Final_order_placed

# Register your models here.

admin.site.register(Contact)
admin.site.register(Owner)
admin.site.register(Finalowner)
admin.site.register(Item)
admin.site.register(Order_placed)
admin.site.register(Customer)
admin.site.register(Expired)
admin.site.register(Save)
admin.site.register(Final_order_placed)
