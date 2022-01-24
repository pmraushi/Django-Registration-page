from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NameForm, LoginForm
from django.contrib.auth.models import User, auth


# Create your views here.

# It renders homepage after user logged in.
def home(request):
    return render(request, "base.html")


# It renders homepage?welcoming page.
def index(request):
    return render(request, "index.html")


# It renders signup page for a new user.
def signup(request):
    form = NameForm

    # It takes the required input from the user.
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # It check whether the first input password matches with the second (confirm password field).
        if password == password2:
            # It checks whether the email taken by another user and terminate.
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email exist!')
                print('email exists!')
            else:
                # If all the required input information are valid it push/saves to database.
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email,
                                                password=password, username=username)
                user.save()
                messages.info(request, 'Account created successfully!')
                print('User created!')
                return redirect('login')
        else:
            messages.info(request, 'password not matching!')
            print('password not matching!')
            return render(request, "signup.html", {'form': form})
    else:
        return render(request, "signup.html", {'form': form})


# It renders login page for an existing user.
def login(request):
    form = LoginForm

    # It checks and compare the input credentials are the same from the database to the corresponding user.
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # If all credentials are correct and same from the database it take the user to the homepage/user dashboard.
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid credentials!')
            return redirect('login')
    else:
        return render(request, "login.html", {'form': form})


# It takes the user out from home dashboard.
def logout(request):
    auth.logout(request)
    print('User logged out!')
    return redirect('signup')
