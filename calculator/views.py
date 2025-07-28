from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class BMICalculatorView(APIView):
	def post(self, request):
		#Get data from the POST request
		height = request.data.get('height')
		weight = request.data.get('weight')
		unit = request.data.get('unit', 'metric').lower() #set default to metric

		#validation
		if not height or not weight:
			return Response(
				{"error": "Plear provide both height and weight."},
				status = status.HTTP_404_BAD_REQUEST
				)

		try:
			height = float(height)
			weight = float(weight)
		except ValueError:
			return Response(
                {"error": "Height and weight must be numeric values."},
                status=status.HTTP_400_BAD_REQUEST
            )
		if height <= 0 or weight <= 0:
			return Response(
                {"error": "Height and weight must be positive values."},
                status=status.HTTP_400_BAD_REQUEST
            )

		#---Calculation---
		bmi = 0
		if unit == 'metric':
			#height in meters, weight in kg	
			bmi =  weight / (height ** 2)
		elif unit == 'imperial':
			#height in inches, weight in lbs
			bmi = 703 * (weight / (height **2))
		else:
			return Response(
				{"error":"Invalid unit, Please use 'metric' or 'imperial'"},
				status=status.HTTP_404_BAD_REQUEST
			)
		#---Classification---
		bmi =  round(bmi, 2)
		if bmi < 18.5:
			category = "Underweight"
		elif 18.5 <= bmi < 24.9:
			category = "Normal Weight"
		elif 25 <= bmi < 29.9:
			category = "Overweight"
		else:
			category = "Obesity"

		#---Response---	
		response_data = {
		'bmi': bmi,
		'category': category
		}
		return Response(response_data, status=status.HTTP_200_OK)

