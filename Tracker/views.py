from django.shortcuts import render, redirect 
from .models import TrackingHistory, Current_balance # models connections  
from django.contrib import messages # for pop massages 
from django.contrib.auth.models import User  # for user database connections 
from django.contrib.auth  import authenticate, login , logout # for authentications 
from django.contrib.auth.decorators import login_required # for login requirement no one can directly access website 



# Create your views here.
@login_required(login_url='login')
def index(request):
    print(request.user)
    print(request.user.is_authenticated)
    if request.method == 'POST':
        description = request.POST.get('description')
        amount = request.POST.get('amount')  
        
        if float(amount) == 0:
            messages.success(request,"cannot add 0") 
            return redirect('/') 
        
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
    current_balance, _ = Current_balance.objects.get_or_create(id = 1) 
    # balance = current_balance.current_balance 
    income = 0 
    expense = 0 
    for tracking_history in TrackingHistory.objects.all():
        if tracking_history.expense_type == "CREDIT":
            income += tracking_history.amount
        else:
            expense += tracking_history.amount          
    context = {'income': income , 'expense' : expense,  'Transactions' : TrackingHistory.objects.all(), 'current_balance' : current_balance  }
    return render(request,"index.html", context) 

def delete_transaction(request,id):
    tracking_history = TrackingHistory.objects.filter(id = id)
    
    if tracking_history.exists():
        current_balance, _ = Current_balance.objects.get_or_create(id = 1)
        tracking_history = tracking_history[0]
    
        current_balance.current_balance = current_balance.current_balance - tracking_history.amount
        current_balance.save()
    tracking_history.delete()
    return redirect('/') 



def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already used")
            return redirect('/signupp/')

        User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name = first_name,
            last_name= last_name
            
        )

        messages.success(request, "Account created successfully")
        return redirect('/login/')

    return render(request, "signup.html")
   


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('/')

        if not User.objects.filter(username=username).exists():
            messages.error(request, "Username does not exist")
        else:
            messages.error(request, "Wrong password")

        return redirect('/login/')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/login/')