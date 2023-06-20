from django.shortcuts import render
from .models import Provider, Category, Offering
from django.db.models import Subquery, OuterRef, FloatField

# Create your views here.



def provider_list(request):
    categories = Category.objects.all()
    offerings = Offering.objects.all().order_by('-interest_rate')

    context = {
        'categories': categories,
        'offerings': offerings
    }

    return render(request, 'tracker/provider_list.html', context)
