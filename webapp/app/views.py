from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import PredictionForm
import requests
from app.db import db

def home(request):
    context = {}
    if request.user.is_authenticated:
        context['username'] = request.user.username
    return render(request, 'home.html', context)

def dashboard(request):
    return HttpResponse("Hello, this is the dashboard")

@login_required
def predict(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            response = requests.post('http://fastapi:5000/predict/', json=data)
            if response.status_code == 200:
                prediction = response.json()['Calories']
                # Save the input data and prediction to MongoDB
                data['Calories'] = prediction
                data['user_id'] = request.user.id
                db.predictions.insert_one(data)
                return render(request, 'predict.html', {'form': form, 'prediction': prediction})
            else:
                return render(request, 'predict.html', {'form': form, 'error': 'An error occurred. Please try again.'})
    else:
        form = PredictionForm()
    
    return render(request, 'predict.html', {'form': form})

@login_required
def prediction_history(request):
    user_id = request.user.id
    predictions = db.predictions.find({'user_id': user_id})
    return render(request, 'history.html', {'predictions': predictions})