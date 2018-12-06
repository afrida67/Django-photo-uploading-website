from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.
def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # log the user in
            return redirect('gallery:index') #after sigining in go to this page app

    else:
        form = UserCreationForm()
    return render(request,'accounts/signup.html',{'form':form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #loggef in
            user = form.get_user()
            login(request, user)
            return redirect('gallery:index')  
    else:
        form = AuthenticationForm()
    
    return render(request,'accounts/login.html',{'form':form})

def logout_view(request):
    if request.method == 'POST': #post request to logout then 
        logout(request)
        return redirect('mainpage')