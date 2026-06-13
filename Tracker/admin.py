from django.contrib import admin
from Tracker.models import*
# Register your models here.

admin.site.site_header = "expense_tracker"
admin.site.site_title = "expense_tracker"
admin.site.site_url = "expense_tracker"
admin.site.register(Current_balance)

@admin.action(description="Mark selected rows as Credited" ) # add action to perform 
def make_credited(modeladmin, request, queryset):
     for q in queryset:
        obj = TrackingHistory.objects.get(id = q.id)
        if obj.amount < 0:
            obj.amount = obj.amount * -1
            obj.save()
        queryset.update(expense_type= "CREDIT")
    
@admin.action(description="Mark selected rows as Debited" )
def make_debited(modeladmin, request, queryset): 
    for q in queryset:
        obj = TrackingHistory.objects.get(id = q.id)
        if obj.amount > 0:
            obj.amount = obj.amount * -1
            obj.save()
    queryset.update(expense_type= "DEBIT")

class TrackingHistoryAdmin(admin.ModelAdmin): 
    list_display = [ # for tabular data
        "amount",
        "expense_type",
        "description",
        "created_at",
        "display_age",
    ]
    
    def display_age(self, obj): # to add extra field 
        if obj.amount > 0:
            return "positive"
        return "Negative"
    
    search_fields = [ # for search by particular type 
        'amount', 
        'expense_type',
        'created_at',
    ]
    ordering = ['-amount'] 
    list_filter = ['expense_type','created_at'] #for additional filtering options by name 
    actions = [make_credited,make_debited] #add action here 

admin.site.register(TrackingHistory, TrackingHistoryAdmin) 