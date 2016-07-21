from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import User
# Create your views here.
def index(request):
    try:
        request.session['logged_in']
        return redirect(reverse('accounts_wall'))
    except KeyError:
        return render(request, 'accounts/index.html')

def signin(request):
    if User.userManager.UserExistsLogin(request.POST, request):
        passFlag = True
        if 'logged_in' not in request.session:
            email = request.POST['email']
            request.session['logged_in'] =  User.objects.get(email=email).id
            return redirect(reverse('accounts_wall'))
    else:
        passFlag = False
        return redirect (reverse('accounts_index'))

def registerpage(request):
    try:
        request.session['logged_in']
        return redirect(reverse('accounts_wall'))
    except KeyError:
        return render(request, 'accounts/register.html')

def register(request):
    try:
        request.session['logged_in']
        return redirect(reverse('accounts_wall'))
    except KeyError:
        if User.userManager.isValidRegistration(request.POST, request):
            passFlag = True
            return redirect(reverse('accounts_index'))
        else:
            passFlag = False
            return redirect(reverse('accounts_registerpage'))

def logout(request):
    request.session.clear()
    return redirect (reverse('accounts_index'))

def wall(request):
    logged_in = request.session['logged_in']
    context = {
        "person": User.objects.get(id=logged_in)
    }
    return render(request, 'accounts/wall.html', context)
