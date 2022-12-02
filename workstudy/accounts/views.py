from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from accounts.models import Account, CustomUser
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist

from organizations.models import Organization
# from django.shortcuts import render_to_response


LOGIN_URL = 'sign-in'

# Create your views here.

def sign_in(request):
    if request.method =='POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect(organization)
        else:
            # error loging in
            return render(request,"pages-login.html",{'message':"incorrect login"})

    elif request.method == "GET":        
        return render(request,"pages-login.html") 

def sign_up(request):
    if request.method =='POST':
        email = request.POST['email']
        # user = CustomUser.user_exists(email)
        if CustomUser.user_exists(email): 
            return render(request,"pages-login.html",{'message':"Email exists, please login"})
            
        else: 

            """
            if user does not exist, save detail
            """

            phone_number = request.POST['phone_number']
            password = request.POST['password']
            user = CustomUser(  email = email,
                                phone_number = phone_number)
            user.set_password(password)
            user.save()
            if user is not None:
                return render(request,"pages-login.html",{"message":"Please login"})
            else:
                """
                if user exist, redirect to login page.
                """
                return render(request,"pages-register.html",{'message':"Error creating user, try again or call support"})

        
    elif request.method == "GET":
        return render(request,"pages-register.html")


@login_required(login_url=LOGIN_URL)  # type: ignore
def createprofile(request):
    if request.method == "POST":
        user = request.user
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        try:
            newAccount =  Account(last_name = lastName,first_name=firstName,user = user)
            newAccount.save()
            return redirect(organization)
        except IntegrityError:
            return render(request,"createprofile.html", {"message": "Your account alreadt exists"})
    elif request.method == "GET":
        return render(request,"createprofile.html")


@login_required(login_url=LOGIN_URL)  # type: ignore
def organization(request):
    try:
        user = Account.get_account(request.user)
        ogranizatioin_list = Organization.get_organizations(user)
        suggestion_list = ogranizatioin_list
        print(suggestion_list)
        return render(request,"choose_organization.html", {"context":suggestion_list})
    except ObjectDoesNotExist as e:
            return render(request,"createprofile.html",{"message": "you do not have a profile, please creat one" })


@login_required(login_url=LOGIN_URL)  # type: ignore
def create_organization(request):
    if request.method == "POST":
        
        organizationName = request.POST['organizationname']
        scale = request.POST['scale']
        try:
            user = request.user
            user = Account.get_account(request.user)
            newOrganization =  Organization(name = organizationName,scale=scale,supervisor = user)
            newOrganization.save()
            return redirect(organization)
        except ObjectDoesNotExist as e:
            return render(request,"createprofile.html",{"message": "you do not have a profile, please creat one" })        
        except IntegrityError as e:
            return render(request,"create_organization.html", {"message": e })
    elif request.method == "GET":
        return render(request,"create_organization.html")


@login_required(login_url=LOGIN_URL)  # type: ignore
def account(request):
    return render(request,"users-profile.html")

@login_required(login_url=LOGIN_URL)  # type: ignore
def schedule(request):
    return render(request,"datepicker.html")

@login_required(login_url=LOGIN_URL)
def dashboard(request):
    organization = request.GET['orgSelected']
    print(organization)
    userAccount = Account.get_account(request.user)
    username = " ".join([userAccount.first_name,userAccount.last_name])  # type: ignore

    context = {
        "username":username
    }
    
    return render(request,"dashboard.html",context = context)

