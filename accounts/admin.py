from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin
from accounts.models import User, Customer, Restaurant
from .forms import CreatUserForm, ChangeUserForm


# Register your models here.

@admin.register(User)
class MyAdminUser(UserAdmin):
    add_formset = CreatUserForm

    formset = ChangeUserForm
    add_fieldsets = (
        (None, {'fields': ('username', 'roll', 'password1', 'password2')},),
    )
    fieldsets = (
        ('Information', {'fields': ('username', 'roll', 'first_name', 'last_name')},),
    )
    list_display = ['username', 'email', 'roll']
    filter_horizontal = []


admin.site.register(Customer)
admin.site.register(Restaurant)