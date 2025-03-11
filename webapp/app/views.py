from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import JsonResponse 
from .forms import PredictionForm
import requests
from app.db import db
import os 

def home(request):
    context = {}
    if request.user.is_authenticated:
        context['username'] = request.user.username
    return render(request, 'home.html', context)

@login_required
def dashboard(request):
    if not request.user.is_authenticated:
        return redirect("accounts/login")

    return render(request, "dashboard.html")

def get_chart_data(request):
    user_id = str(request.user.id)
    print("Fetching data for user_id:", user_id)

    predictions = list(db.predictions.find({'user_id': int(user_id)}))
    print("Fetched Predictions:", predictions)  # Debugging

    if not predictions:
        print("No data found for user_id:", user_id)

    # Extract Data
    ages = [entry.get('Age', 0) for entry in predictions]
    calories = [entry.get('Calories', 0) for entry in predictions]
    durations = [entry.get('Duration', 0) for entry in predictions]
    genders = [entry.get('Gender', 'Unknown') for entry in predictions]

    # Gender Distribution
    male_count = sum(1 for g in genders if g.lower() == 'male')
    female_count = sum(1 for g in genders if g.lower() == 'female')

    return JsonResponse({
        "ages": ages,
        "calories": calories,
        "durations": durations,
        "gender_distribution": {
            "labels": ["Male", "Female"],
            "values": [male_count, female_count]
        }
    })


@login_required
def predict(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            response = requests.post(os.getenv('api-url'), json=data)
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