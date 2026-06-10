from django.shortcuts import render, redirect 
from .models import TrackingHistory, Current_balance


# Create your views here.
def index(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        amount = request.POST.get('amount')  
        
        current_balance, _ = Current_balance.objects.get_or_create(id = 1)
        
        expense_type = "CREDIT"
        if float(amount) < 0:
            expense_type = "DEBIT"
        up = TrackingHistory.objects.create(
            description =description,
            current_balance = current_balance,
            expense_type= expense_type, 
            amount = amount,
        )
        current_balance.current_balance += float(up.amount)
        current_balance.save()
        return redirect('/')
    return render(request,"index.html") 
