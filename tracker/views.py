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

def impressum(request):
    return render(request, 'tracker/impressum.html')

def pp(request):
    return render(request, 'tracker/pp.html')

def tc(request):
    return render(request, 'tracker/tc.html')

def contact(request):
    return render(request, 'tracker/contact.html')