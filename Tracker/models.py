from django.db import models

# Create your models here.
class Current_balance(models.Model):
    current_balance = models.FloatField(default = 0) 
    
class TrackingHistory(models.Model):
    current_balance = models.ForeignKey(Current_balance, on_delete=models.CASCADE)
    amount = models.FloatField(editable = False)
    expense_type = models.CharField(choices = (('CREDIT', 'CREDIT'),('DEBIT','DEBIT')),max_length=200)
    description =models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now= True)
    updated_at = models.DateTimeField(auto_now_add= True)  
    
    def __str__(self) -> str:
        return f"the amount is {self.amount} for {self.description} "
    
class RequestLogs(models.Model):
    request_info = models.TextField()
    request_type = models.CharField(max_length=100)
    method = models.CharField(max_length=50 ,default = "postget")
    ip_address = models.CharField( max_length=100 , default = 100)
    created_at = models.DateTimeField(auto_now_add= True) 
 
    
    
