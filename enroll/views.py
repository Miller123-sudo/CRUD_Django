from django.shortcuts import render, HttpResponseRedirect
from enroll.forms import StudentRegistration
from enroll.models import User

# Create your views here.


def add_show(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)

        if fm.is_valid():
            # Get imputed data from form
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']

            # Create an object of imported User class and save data by passing in User object
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration()

    else:
        fm = StudentRegistration()

        # Get data from database to show
    userData = User.objects.all()

    return render(request, 'enroll/addAndShow.html', {"form": fm, 'data': userData})

# To update user


def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)

    return render(request, 'enroll/updateStudent.html', {"form": fm})

# To delete data from table


def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
