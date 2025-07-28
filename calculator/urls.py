from django.urls import path
from .views import BMICalculatorView

urlpatterns = [
	path('calculate/', BMICalculatorView.as_view(), name='bmi-calculate'),
]