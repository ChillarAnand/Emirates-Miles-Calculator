from django.shortcuts import render
from django.http import HttpResponse

from .forms import CalculatorForm



# Create your views here.
def calculator(request):
    if request.method == "GET":
        return render(request, 
                      'calculator.html', 
                      {'forms' : CalculatorForm }, )
    elif request.method == "POST":
        form = CalculatorForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['departure']
            b = form.cleaned_data['arrival']

        return render(request,
                      'calculator.html',
                      {'forms' : form }, )



