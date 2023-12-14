from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accounts.models import User


class CreatUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = UserCreationForm._meta.fields + ('roll',)


class ChangeUserForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('roll', )

