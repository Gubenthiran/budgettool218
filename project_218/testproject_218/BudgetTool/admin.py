from django.contrib import admin
from .models import Expense  # Import your model here

@admin.register(Expense)  # Use the @admin.register() decorator to register the model
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'amount', 'date')  # Customize the fields displayed in the list view
    list_filter = ('date',)  # Add filters to the right sidebar
    search_fields = ('title', 'desc')  # Add a search bar
