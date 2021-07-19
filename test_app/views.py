from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserData
from django.core.mail import send_mail
from django.http import JsonResponse
import datetime


# show all details
# get all details from db and update
def all_user(request):
    if request.method == 'POST':
        # get all data
        user_id = request.POST.get('userId', None)
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        number = request.POST.get('number', None)
        dob = request.POST.get('dob', None)

        # update all data
        obj = UserData.objects.get(id=user_id)
        obj.name = name
        obj.number = number
        obj.email = email
        obj.dob = dob
        obj.date_of_modification = datetime.datetime.now()
        obj.save()
        messages.add_message(request, messages.SUCCESS, "User Details Update Successfully")
        # send mail to user
        send_mail(
            'Add User Successfully',
            'Hello {}, User Details Update Successfully , your number= {}'.format(
                name, number),
            'ks8094238@gmail.com',
            ['{}'.format(email)],
            fail_silently=False,
        )
        return redirect('all_user')
    else:
        # get all data from db
        value = UserData.objects.all()
        print(value)
        users = []
        for x in value:
            val = {
                'id': x.id,
                'name': x.name,
                'email': x.email,
                'number': x.number,
                'dob': x.dob
            }
            users.append(val)
        return render(request, "allUser.html", {'users': users})


# add new user
def add_user(request):
    if request.method == 'POST':
        # get all details
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        number = request.POST.get('number', None)
        dob = request.POST.get('dob', None)

        # save user details
        UserData(
            name=name,
            email=email,
            number=number,
            dob=dob
        ).save()
        # success messages
        messages.add_message(request, messages.SUCCESS, "User Add Successfully")
        # send mail to user
        send_mail(
            'Add User Successfully',
            'Hello {}, Your add record Successfully , your number= {}'.format(
                name, number),
            'ks8094238@gmail.com',
            ['{}'.format(email)],
            fail_silently=False,
        )

        return redirect('all_user')
    return render(request, 'addUser.html')


# delete user
def delete_user(request):
    id1 = request.GET.get('id', None)
    UserData.objects.get(id=id1).delete()
    data = {
        'deleted': True
    }
    return JsonResponse(data)
