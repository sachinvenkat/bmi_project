from django.urls import path
from .views import RandomQuoteView

urlpatterns = [
	path('random/',RandomQuoteView.as_view(), name='random-quote'),
]