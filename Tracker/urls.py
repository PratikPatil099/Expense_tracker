from django.urls import path 
from . import views

urlpatterns = [
    path('logout_view/', views.logout_view, name = "logout_view" ),
    path('login/', views.login_page, name = "login" ),
    path('signupp/', views.signup, name = "signup" ),
    path('', views.index, name = "index" ),
    path('delete-transaction/<id>/',views.delete_transaction, name = "delete_transaction")
]
