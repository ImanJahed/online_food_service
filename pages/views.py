from django.shortcuts import render
from django.views.generic import View

from accounts.models import Restaurant
from restaurant.models import Food


# Create your views here.


class Home(View):
    template_name = "pages/home.html"

    def get(self, request):
        return render(request, self.template_name)


class SearchFood(View):
    template_name = 'pages/search.html'

    def get(self, reqeust):
        q = reqeust.GET.get('q')
        foods = Food.objects.filter(food_title__icontains=q)
        context = {
            'foods': foods,
            'q': q
        }

        return render(reqeust, self.template_name, context)
