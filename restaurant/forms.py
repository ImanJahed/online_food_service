from django import forms


from .models import Category, Food


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name', 'description']


class FoodItemForm(forms.ModelForm):
    image = forms.FileField(widget=forms.FileInput(attrs={'class': 'btn btn-info w-100'}))

    class Meta:
        model = Food
        fields = ['food_title', 'description', 'price', 'preparation_time', 'image', 'is_available']



