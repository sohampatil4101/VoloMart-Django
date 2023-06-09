from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    desc = models.TextField()
    # date = models.DateField()

    def __str__(self):
        return self.name


state_choice = (
	("Maharashtra", "Maharashtra"),
)
city_choice = (
	("Mumbai", "Mumbai"),
)
area_choice = (
	("Borivali(east)", "Borivali(east)"),
	("Borivali(West)", "Borivali(west)"),
	("Kandivali(east)", "Kandivali(east)"),
	("Kandivali(west)", "Kandivali(west)"),
	("Dahisar(east)", "Dahisar(east)"),
	("Dahisar(West)", "Dahisar(west)"),
	("Miraroad(east)", "Miraroad(east)"),
	("Miraroad(West)", "Miraroad(west)"),
	("Bhaindar(east)", "Bhaindar(east)"),
	("Bhaindar(West)", "Bhaindar(west)"),
	("Naigoan(east)", "Naigoan(east)"),
	("Naigoan(West)", "Naigoan(west)"),
	("Vasairoad(east)", "Vasairoad(east)"),
	("Vasairoad(West)", "Vasairoad(west)"),
	("Nalasopara(east)", "Nalasopara(east)"),
	("Nalasopara(West)", "Nalasopara(west)"),
	("Virar(east)", "Virar(east)"),
	("Virar(West)", "Virar(west)"),
)


class Customer(models.Model):
    username = models.TextField(max_length = 20)
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField()
    password = models.TextField()
    state = models.TextField(choices = state_choice, default = 'Maharashtra')
    city = models.TextField(choices = city_choice, default = 'Mumbai')
    area = models.TextField(choices = area_choice, default = 'Kandivali(East)')
    pincode = models.TextField()
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.username

class Owner(models.Model):
    username = models.TextField(max_length = 20)
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    password = models.TextField()
    state = models.TextField(choices = state_choice, default = 'Maharashtra')
    city = models.TextField(choices = city_choice, default = 'Mumbai')
    area = models.TextField(choices = area_choice, default = 'Kandivali(East)')
    pincode = models.TextField()
    images1 = models.FileField(upload_to='images/', default = 0)
    images2 = models.FileField(upload_to='images/', default = 0)
    images3 = models.FileField(upload_to='images/', default = 0)

    def __str__(self):
        return self.username


    # date = models.DateField()

class Finalowner(models.Model):
    username = models.TextField(max_length = 20)
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    password = models.TextField()
    state = models.TextField()
    city = models.TextField()
    area = models.TextField()
    pincode = models.TextField()
    images = models.ImageField(upload_to='images')
    images = models.ImageField(upload_to='images')
    images = models.ImageField(upload_to='images')

    def __str__(self):
        return self.username

ITEMS_CHOICES = (
	("Vegetables", "Vegetables"),
	("Fruits", "Fruits"),
	("Electronics", "Electronics"),
	("Clothes", "Clothes"),
)


class Item(models.Model):
    seller = models.TextField()
    category = models.TextField(
		choices = ITEMS_CHOICES )
    itemname = models.TextField()
    discription = models.TextField()
    key_features1 = models.TextField()
    key_features2 = models.TextField()
    key_features3 = models.TextField()
    key_features4 = models.TextField()
    old_itemprice = models.IntegerField()
    new_itemprice = models.IntegerField()
    percentage = models.IntegerField()
    lastdate = models.DateField()
    state = models.TextField()
    city = models.TextField()
    area = models.TextField()
    address = models.TextField()
    images = models.ImageField(upload_to='images')

    def __str__(self):
        return self.itemname + " " + self.category



class Expired(models.Model):
    seller = models.TextField()
    category = models.TextField(
		choices = ITEMS_CHOICES )
    itemname = models.TextField()
    discription = models.TextField()
    key_features1 = models.TextField()
    key_features2 = models.TextField()
    key_features3 = models.TextField()
    key_features4 = models.TextField()
    old_itemprice = models.IntegerField()
    new_itemprice = models.IntegerField()
    percentage = models.IntegerField()
    lastdate = models.DateField()
    state = models.TextField()
    city = models.TextField()
    area = models.TextField()
    address = models.TextField()
    images = models.ImageField(upload_to='images')

    def __str__(self):
        return self.itemname + " " + self.category


payment_choice = (
	("Online", "Online"),
	("cash on delievery", "cash on delievery"),
)

class Order_placed(models.Model):
    username = models.TextField()
    sellername = models.TextField()
    itemname = models.TextField()
    paymentmode = models.TextField(
		choices = payment_choice,
		default = '2'
    )
    piece = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.username + " " + self.itemname



class Final_order_placed(models.Model):
    username = models.TextField()
    sellername = models.TextField()
    itemname = models.TextField()
    paymentmode = models.TextField(
		choices = payment_choice,
		default = '2'
    )
    piece = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.username + " " + self.itemname





class Save(models.Model):
    username = models.TextField()
    seller = models.TextField()
    category = models.TextField()
    itemname = models.TextField()
    old_itemprice = models.IntegerField(default = 0)
    new_itemprice = models.IntegerField(default = 0)
    lastdate = models.TextField(null = True)
