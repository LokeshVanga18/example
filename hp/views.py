from django.shortcuts import render , HttpResponse , redirect
# from .models import PersonalInfo , Results , ClientRegister
from hp.forms import AllCoveredForm , Student , another , ClientRegisterForm , UserForm , ContactForm
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail , BadHeaderError

def index(req):
    return render(req , 'index.html')

def register(req):
    if req.method == 'POST':
        user_form = UserForm(req.POST)
        extra_details = ClientRegisterForm(req.POST)

        if user_form.is_valid() and extra_details.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = extra_details.save(commit = False)
            profile.user = user

            if 'profile_pic' in req.FILES:
                profile.profile_pic = req.FILES['profile_pic']
            profile.save()

            return redirect('login')
    else:
        user_form = UserForm
        extra_details = ClientRegisterForm()

    return render(req , 'register.html' , {'user_form' : user_form , 'extra' : extra_details})

def user_login(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')

        user = authenticate(req , username = username , password = password)

        if user:
            login(req , user=user)

            return redirect('home')
        else:
            messages.error(req , 'Invalid username or password.')

    return render(req , 'login.html')


@login_required
def user_logout(req):
    logout(req)

    return render(req , 'index.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            try:
                send_mail(
                    f'New Contact Form Submission from {name}',
                    message,
                    email,
                    ['lokeshone818@example.com'],  # Replace with your own email
                    fail_silently=False,
                )
                messages.success(request, 'Thank you for your message. We will get back to you shortly.')
                return redirect('contact')
            except (ConnectionRefusedError, BadHeaderError):
                messages.error(request, 'Failed to send email. Please try again later.')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


# def example(req):
#     return render(req , 'example.html')

# def RetrivingData(req):
#     model = PersonalInfo
#     objs = model.objects.all()

#     return render(req , 'retrive.html' , {'info' : objs})
# def UserRetrive(req):
#     objs = User.objects.all()
#     return render(req , 'exam.html' , {'info' : objs})

# def showForm(req):
#     form = AllCoveredForm()
#     return render(req , 'all_form.html' , {'form' : form})

# def student(req):
#     if req.method == 'POST':
#         form = Student(req.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             id = form.cleaned_data['std_id']
#             email = form.cleaned_data['email']
#             mob = form.cleaned_data['mobile_num']
#             add = form.cleaned_data['address']

#             k = PersonalInfo(name = name , std_id = id , email = email , mobile_num = mob , address = add)

#             k.save()
#     else:
#         form = Student()
#     return render(req , 'student.html' , {'form' : form})

# def anothe(req):
#     form = another()
#     return render(req , 'all_form.html' , {'form':form})