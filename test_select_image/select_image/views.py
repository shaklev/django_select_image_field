from django.shortcuts import render
from .forms import CountriesForm
# Create your views here.
def get_countries(request):
    context = {}
    context['form'] = CountriesForm()
    return render(request,'base.html',context)
