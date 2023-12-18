from django.shortcuts import render,redirect
from .models import UserProfile
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
import uuid
# Create your views here.


def index(request):
    return render(request,'index.html')


def dashboard(request):

    if 'user_email' in request.session:

        session_email = request.session.get('user_email')

        # Retrieve the UserProfile associated with the current user
        user_profile = UserProfile.objects.get(email=session_email)
        context = {
            'email':user_profile
        }
       

        return render(request, 'dashboard/dashboard.html',context)


    else:
        return redirect('/login') 


def vehicles(request):

    session_email = request.session.get('user_email')

    user_profile = UserProfile.objects.get(email=session_email)
    celermont_id = user_profile.cleremont_id

    context = {
        "email":user_profile,
        'celermont_id': celermont_id
    }


    return render(request,'dashboard/vehicle.html',context)


def maps(request):
    session_email = request.session.get('user_email')

    user_profile = UserProfile.objects.get(email=session_email)

    context = {
        "email":user_profile
    }
    return render(request,'dashboard/maps.html',context)


def deliveries(request):
    session_email = request.session.get('user_email')

    user_profile = UserProfile.objects.get(email=session_email)

    context = {
        "email":user_profile
    }
    
    return render(request,'dashboard/deliveries.html',context)


def signup(request):
    if request.method == 'POST':
        print('Print statement called')
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        raw_password = request.POST.get('password')

        if UserProfile.objects.filter(email=email).exists():
            context = {
                "error_message":"User with this email already exists. Please use a different email."
            }
            return render(request, 'signup.html',context)


        # Generate a unique 15-digit identifier using uuid
        cleremontID = str(uuid.uuid4().int)[:15]

        # Hash the password using make_password
        hashed_password = make_password(raw_password)

        user_profile = UserProfile(
            cleremont_id=cleremontID,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=hashed_password
        )

        user_profile.save()



        return render(request, 'success_page.html')

    return render(request, 'signup.html') 





def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Retrieve the user from the database based on the provided email
        user = UserProfile.objects.filter(email=email).first()

        if user is not None and check_password(password, user.password):
            # Passwords match, store the user's email in the session
            request.session['user_email'] = user.email
            return redirect('/dashboard/vehicles')  # Replace '/dashboard' with the actual URL of your dashboard or home page
        else:
            context = {
                "error_message": "Invalid email or password. Please try again."
            }
            return render(request, 'login.html', context)

    return render(request, 'login.html')





def logout(request):
    # Remove the user_email key from the session to logout the user
    if 'user_email' in request.session:
        del request.session['user_email']

    # Optionally, you can also use request.session.flush() to clear all session data
    # request.session.flush()

    # Redirect the user to the login page or any other page after logout
    return redirect('/login')  # Replace '/login' with the actual URL of your login page



def add_delivery(request):
    
    return render(request,'dashboard/deliveries.html')



def vehicle_table(request):
    if request.method == 'POST':
        # Access form data using request.POST
        celermont_id = request.POST.get('celermont_id')
        vehicle_name = request.POST.get('vehicle_name')
        speed_limit = request.POST.get('speed_limit')
        stat_limit = request.POST.get('stat_limit')
        mobile_no = request.POST.get('mobile_no')
        groups = request.POST.get('groups')
        zones = request.POST.get('zones')
        vehicle_type = request.POST.get('vehicle_type')



    session_email = request.session.get('user_email')

    user_profile = UserProfile.objects.get(email=session_email)

    context = {

        "email":user_profile
    }

    return render(request,'dashboard/vehicleTable.html',context)



