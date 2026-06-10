from django.db import models

# Create your models here.
class Current_balance(models.Model):
    current_balance = models.FloatField(default = 0) 
class TrackingHistory(models.Model):
    current_balance = models.ForeignKey(Current_balance, on_delete=models.CASCADE)
    amount = models.FloatField()
    expense_type = models.CharField(choices = (('CREDIT', 'CREDIT'),('DEBIT','DEBIT')),max_length=200)
    description =models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now= True)
    updated_at = models.DateTimeField(auto_now_add= True)  