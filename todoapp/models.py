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


class Owner(models.Model):
    username = models.TextField()
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    images = models.ImageField(upload_to='images')

    def __str__(self):
        return self.username


    # date = models.DateField()

class Finalowner(models.Model):
    username = models.TextField()
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    images = models.ImageField(upload_to='images')

    def __str__(self):
        return self.username

ITEMS_CHOICES = (
	("1", "Vegetables"),
	("2", "Fruits"),
	("3", "Electronics"),
	("4", "Clothes"),
)
class Item(models.Model):
    seller = models.TextField()
    category = models.TextField(
		choices = ITEMS_CHOICES,
		default = '1' )
    itemname = models.TextField()
    itemprice = models.IntegerField()
    lastdate = models.DateField()
    images = models.ImageField(upload_to='images')

    def __str__(self):
        return self.itemname



# # specifying choices

# SEMESTER_CHOICES = (
# 	("1", "1"),
# 	("2", "2"),
# 	("3", "3"),
# 	("4", "4"),
# 	("5", "5"),
# 	("6", "6"),
# 	("7", "7"),
# 	("8", "8"),
# )

# # declaring a Student Model

# class Student(models.Model):
# 	semester = models.CharField(
# 		max_length = 20,
# 		choices = SEMESTER_CHOICES,
# 		default = '1'
# 		)
