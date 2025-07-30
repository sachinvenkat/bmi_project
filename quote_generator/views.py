from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import random 

# --- Our "database" of quotes ---
QUOTES = [
	{
		"id":1,
		"quote": "The only way to do great work is to love what you do.",
		"author":"Steve Jobs"
	},
	{
		"id":2,
		"quote":"The journey of thousand miles begins with a single step.",
		"author": "Lao Tzu"
	},
	{
		"id":3,
		"quote": "That which does not kill us makes us stronger.",
		"author": "Friedrich Nietzsche"
	},
	{
		"id":4,
		"quote":"Strive not to be a success, but rather to be of value",
		"author":"Albert Einstein"
	},
	{
		"id":5,
		"quote":"You miss 100% of the shots you don't take.",
		"author":"Wayne Gretzky"
	},
]

class QuoteView(APIView):
	"""
	API View to return a random quote or a specific quote by itd ID.
	"""
	def get(self, request, quote_id=None):
		"""
		Handle GET requests to return a random quote.
		If quote_id is provided, returns the speific quote.
		Otherwise, returns a random quote.
		"""
		if quote_id:
			quote = next(( q for q in QUOTES if q['id'] == quote_id), None)
			if quote:
				return Response(quote, status=status.HTTP_200_OK)
			else:
				return Response(
					{"error": "Quote not found."}, 
					status=status.HTTP_404_NOT_FOUND
				)
		else:
			#Select a random quote from our list if no ID is specified
			quote = random.choice(QUOTES)
			return Response(quote, status=status.HTTP_200_OK) 			

		