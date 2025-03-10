from django import forms

class PredictionForm(forms.Form):
    GENDER_CHOICES = [('male', 'male'), ('female', 'female')]
    
    Gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    Age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    Height = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    Weight = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    Duration = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    Heart_Rate = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    Body_Temp = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))