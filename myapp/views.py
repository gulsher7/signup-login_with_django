from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib import messages

def index(request):
	return render(request, 'myapp/index.html')

def signup(request):
	if request.method == 'POST':
		if request.POST['password1']== request.POST['password2']:
			try: 
				user = User.objects.get(username=request.POST['username'])
				return render(request, 'myapp/signup.html', {'usernameerror':'username is already exist please try a different name'})
			except User.DoesNotExist:
				user = User.objects.create_user(username=request.POST['username'], email = request.POST['email'], password =request.POST['password1'])
				auth.login(request, user)
				return render(request, 'myapp/login.html', {'success':'your account has been successfully created'})
		else:
			return render(request, 'myapp/signup.html', {'passworderror': 'password does not matched'})
	else:
		return render(request, 'myapp/signup.html')

def login(request):
	if request.method == 'POST':
		user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			auth.login(request, user)
			return render(request, 'myapp/index.html', {'loginsuccess': 'login success'})
		else:
			return render(request, 'myapp/login.html', {'error':'username or password is incorrect'})
	else:
		return render(request, 'myapp/login.html')


def userdata(request):
    data = User.objects.all()
    return render(request, 'myapp/userdata.html', {'data': data})

def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		return redirect('index')

