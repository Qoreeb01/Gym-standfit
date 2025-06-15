from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from Fitlife.models import Contact

# Create your views here.
def Home(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('usernumber')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if len(username) < 10 or len(username) > 10:
            messages.info(request, 'Phone Number must be at least 8 digits')
            return redirect('/signup')
        
        if pass1!=pass2:
            messages.info(request, 'Passwords do not match')
            return redirect('/signup')
        
        try:
            if User.objects.get(username=username):
                messages.warning(request, 'Phone Number already exists')
                return redirect('/signup')
            
        except Exception as identifier:
               pass
        

        try:
            if User.objects.get(email=email):
                messages.warning(request, 'Email already exists')
                return redirect('/signup')
            
        except Exception as identifier:
               pass
    
        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()
        messages.success(request, 'Your account has been created successfully')
        return redirect('/login')   

    return render(request, 'signup.html')

def handlelogin(request):
    if request.method=="POST":
        username = request.POST.get('usernumber')
        pass1 = request.POST.get('pass1')

        myuser=authenticate(username=username, password=pass1)
        if User is not None:
            login(request, myuser)
            messages.success(request, 'Login successful')
            return redirect('/')
        else:  
             messages.error(request, 'Invalid password')
             return redirect('/login')
    
    return render(request, 'handlelogin.html')   

def handlelogout(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('/') 

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        num = request.POST.get('num')
        desc = request.POST.get('desc')
        myquery=Contact(name=name, email=email,phone=num,description=desc)

        myquery.save()

        # Here you would typically save the contact information to the database
        # For now, we will just display a success message
        messages.info(request, 'Thanks for contacting us we will contact you soon')
        return redirect('/')
    return render(request, 'contact.html')

def enroll(request):
    Membership=MembershipPlan.objects.all()
    SelectTrainer=Trainer.objects.all()
    context= {
        "Membership": Membership, "SelectTrainer": SelectTrainer
    }   
    return render(request, 'enroll.html',context)