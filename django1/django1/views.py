from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
# from django.contrib import messages
from .forms import LogInForm, SignUp
from jobs.models import jobHiring

def home(request):
    # using dictionary we can send our message or data to any html page from views.py file like this:
    # msg = {
    #     'title': 'New Home',
    #     'body': 'Hello this views data to show in html',

    #     # create a list and show on html page using for loop
    #     'body2': ['java', 'django', 'python'],
    #     # dictionary with for loop
    #     'detail': [
    #         { 'Name': "Zaid", 'Phone_Number': '03328516774',  'Dev': 'Python Developer', 'Address': 'Pakistan'},
    #         { 'Name': "Any", 'Phone_Number': '03328516774', 'Dev': 'Java Developer', 'Address': 'UK' }
    #     ],
    # create a list to implement if and ifelse statement
    # 'anylist': [30, 31, 35, 101, 99, 67, 18]
    # }
    HiringData = jobHiring.objects.all()
    data = {    
        'HiringData':HiringData
    }
    return render(request, "index.html", data)  # here we can pass three argument


def about(request):
    return render(request, "about.html")


def freelancer(request):
    return render(request, "freelancer.html")

def job(request):
    # HiringData = jobHiring.objects.all()
    # data = {    
    #     'HiringData':HiringData
    # }
    return render(request, "job.html")

def login(request):
    # print(request.POST, "Hello")
    fm = LogInForm() # call form and save in the variable
    try:
        # username = request.GET['username']
        # password = request.GET['password']
        
        # we can also achieve like this:
        # username = request.GET.get('username')
        # password = request.GET.get('password')
        # print(username + password) # cancatenate
        
        if request.method == "POST":
            # username = request.POST.get('username')
            # password = request.POST.get('password')
            username = request.POST['username']
            password = request.POST['password']
    except:
        pass
    return render(request, "login.html", {'form':fm})

def signup(request):
    signupform = SignUp() # call the sign up form and save in the variable
    try:
        if request.method == "POST":
            username = request.POST['fullname']
            email = request.POST['email']
            password = request.POST['password']
    except:
        pass
    # import pdb; pdb.set_trace() -->  interpreter type tracer stopper, where we can stop our interpreter and check how our code is doing debugging
    return render(request, 'signup.html', {'form': signupform})

def verification(request, verifyID):
    if request.method == 'POST':
        entered_code = request.POST.get('verification_code')
        # Add your logic to validate the entered_code against the expected code
        expected_code = "123456"  # Replace with the actual expected code

        if entered_code == expected_code:
            # Code is correct, redirect to the home page
            return HttpResponseRedirect('/home/')
        else:
            # Code is incorrect, you might want to handle this case
            # For now, redirect back to the verification page with an error message
            return render(request, 'verification.html', {'verifyID': verifyID, 'error': 'Incorrect verification code'})

    # If it's a GET request, render the verification page
    return render(request, 'verification.html', {'verifyID': verifyID})