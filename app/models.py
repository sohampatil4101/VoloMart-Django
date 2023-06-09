from django.db import models

class Payment(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    transaction_id = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True, null=True)