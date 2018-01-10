from django.shortcuts import render

# Create your views here.
def index(request):
	template = 'dashboard.html'
	context = {}
	return render(request, template, context)
