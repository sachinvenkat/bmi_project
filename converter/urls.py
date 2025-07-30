from django.urls import path
from .views import TemperatureConverterView 

urlpatterns = [
	path('', TemperatureConverterView.as_view(), name='temperature-converter' )
]