from django import forms

class CalculatorForm(forms.Form):
    departure = forms.CharField(max_length=3)
    arrival = forms.CharField(max_length=3)
