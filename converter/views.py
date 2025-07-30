from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class TemperatureConverterView(APIView):

	def get(self, request):
		value_str = request.query_params.get('value')
		from_unit = request.query_params.get('from', '').lower()

		if not value_str or not from_unit:
			return Response(
				{"error": "Please provide 'value' and 'from' query parameters. E.g., ?value=32&from=celsius"},
				status=status.HTTP_400_BAD_REQUEST
				)
		try:
			value = float(value_str)
		except (ValueError, TypeError):
			return Response(
				{"error": "Temperature 'value' must be a number."},
				status=status.HTTP_400_BAD_REQUEST
				)
		celsius, fahrenheit, kelvin = None, None, None

		if from_unit == 'celsius':
			celsius = value
			fahrenheit = (value * 9/5) + 32
			kelvin = value + 273.15

		elif from_unit == 'fahrenheit':
			fahrenheit = value
			celsius = (value - 32) * 5/9
			kelvin = celsius + 273.15

		elif from_unit == 'kelvin':
			kelvin = value
			celsius = value - 273.15
			fahrenheit = (celsius * 9/5) + 32

		else:
			return Response(
				{"error": "Invalid unit. 'from' must be 'celsius', 'fahrenheit', or 'kelvin'."},
				status=status.HTTP_400_BAD_REQUEST
            )
		
		response_data ={
			'celsius': round(celsius, 2),
			'fahrenheit': round(fahrenheit, 2),
			'kelvin': round(kelvin, 2)
		}	
		return Response(response_data, status=status.HTTP_200_OK)