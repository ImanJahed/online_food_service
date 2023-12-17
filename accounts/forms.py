from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accounts.models import User, Customer, Restaurant


class CreatUserForm(UserCreationForm):
    address = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User
        fields = UserCreationForm._meta.fields + ('first_name', 'last_name', 'address', 'roll',)


class ChangeUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('roll',)


class RegisterForm(UserCreationForm):
    address = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'address')



class RestaurantRegisterForm(forms.ModelForm):
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Password Confirmation')

    class Meta:
        model = Restaurant
        exclude = ['user', 'shipping_cost']

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            return forms.ValidationError('Username already exists')
        return username
    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Password Does not match')
        return password2
