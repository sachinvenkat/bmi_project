from django.urls import path
from .views import QuoteView

urlpatterns = [
	#Route for a ranfdom quote
	path('random/',QuoteView.as_view(), name='random-quote'),
	#Route for a specific quote by its id
	path('<int:quote_id>',QuoteView.as_view(), name='specific-quote'),
]