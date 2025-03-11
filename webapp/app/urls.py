from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('predict/', views.predict, name='predict'),
    path('history/', views.prediction_history, name='history'),
    path('api/chart-data/', views.get_chart_data, name='chart-data'),
]