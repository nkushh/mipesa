from django.contrib import messages
from django.shortcuts import render

# Create your views here.
def create_account(request):
    if request.method == 'POST':
        username = request.POST['username']
        email =  request.POST['email']
        password =  request.POST['password']
        if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
            User.objects.create_user(username, email, password)
            user = authenticate(username = username, password = password)
            login(request, user)
            return HttpResponseRedirect('/')
        else:
        	messages.error(request, "Error! Looks like a username with that email or password already exists.")
        	context = {}
        	return render(request, 'auth_app/register.html', context)
    else:
    	template = 'auth_app/register.html'
    	context = {}
    	return render(request, template, context)
