from django.shortcuts import render

# Create your views here.
def index(request):
	"""Render the app dashboard for the root URL."""
	return render(request, 'appTest_app/dashboard.html')
