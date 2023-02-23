from django.shortcuts import render, redirect
from todoapp.models import Contact
from todoapp.models import Owner
from todoapp.models import Finalowner
from todoapp.models import Item
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.



def home(request):
    so = Item.objects.all()
    context = {'so':so}
    return render(request, 'home.html', context)



def about(request):
        
    return render(request, 'about.html')



def contact(request):
    
    context = {'success': False }
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        ins = Contact(name = name, email= email, phone = phone, desc = desc)
        ins.save()
        context = {'success': True }

    return render(request, 'contact.html', context)


def welcome(request):
    return render(welcome.html)

def loginuser(request):
    context = {'success': False, 'successs':False}
    if request.method == "POST":
        global glo
        username = request.POST['username']
        glo = username
        password = request.POST['password']
        user = authenticate(username= username, password = password)

        if (Finalowner.objects.filter(username=glo).exists()):
            login(request, user)
            # return redirect("/todo")      
            context = {'name':username}
            return render(request, 'seller.html',context)
            context = {'successs':False}


        elif user is not None:
            login(request, user)
            # return redirect("/todo")      
            context = {'name':username}
            return render(request, 'welcome.html',context)
            context = {'successs':False}


        else:
            context= {'success':True, 'soham':"Please enter correct username or password!!!"}
            return render(request, 'login.html', context)



    return render(request, 'login.html', context)
    


def register(request):
    
    context = {'success': False, 'successs':False, 'mssg':""}
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if ( len(username) or len(first_name) or len(last_name) or len(email) or len(password1)) == 0:
            context={'successs':True,'mssg':"Please enter every field!!"}

        elif (password1 != password2 ):
            context={'successs':True,'mssg':"Both passwords are not same!!"}

        elif (User.objects.filter(username=username).exists() ):
            context={'successs':True,'mssg':"Username exists!!"}
        
        elif (Finalowner.objects.filter(username=username).exists() ):
            context={'successs':True,'mssg':"Username exists!!"}

        elif ( User.objects.filter(email=email).exists() ):
            context={'successs':True,'mssg':"Email exists!!"}

        elif (Finalowner.objects.filter(email=email).exists() ):
            context={'successs':True,'mssg':"Email exists!!"}


        else:
            ins = User.objects.create_user(username = username, first_name = first_name, last_name = last_name, email = email, password = password1)
            ins.save()
            context = {'success': True}

    return render(request, 'register.html', context)






def owner(request):
    
    context = {'success': False, 'successs':False, 'mssg':""}
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        images = request.POST['images']

        if ( len(username) or len(first_name) or len(last_name) or len(email)  )== 0:
            context={'successs':True,'mssg':"Please enter every field!!"}


        elif (images) == 0:
            context={'successs':True,'mssg':"Please enter every field!!"}


        elif (Owner.objects.filter(username=username).exists() ):
            context={'successs':True,'mssg':"Username exists!!"}
            

        elif (Finalowner.objects.filter(username=username).exists() ):
            context={'successs':True,'mssg':"Username exists!!"}

        elif ( Owner.objects.filter(email=email).exists() ):
            context={'successs':True,'mssg':"Email exists!!"}


        elif ( Finalowner.objects.filter(email=email).exists() ):
            context={'successs':True,'mssg':"Email exists!!"}

        else:
            print(images)
            ins = Owner(username = username, first_name = first_name, last_name = last_name, email = email, images = images)
            ins.save()
            context = {'success': True}
            return render(request, 'owner.html', context)


    return render(request, 'owner.html', context)


def add(request):
    so = Owner.objects.all()
    context = {'so': so}
    return render(request, 'admin.html', context)


def delete(request, name, email):
    abc = Owner.objects.get(username = name)
    abc.delete()
    send_mail(
        'title is here',
        'sorry but ur profile is rejected by volo mart...',
        'settings.EMAIL_HOST_USER',
        [email], #here it can be also a list of emails
        fail_silently = False
    )
    return redirect("/add")


def view(request, obj, obj2, obj3, obj4):
    context = {'name': obj, 'first_name': obj2, 'last_name': obj3, 'email': obj4}
    return render(request, 'view.html', context)


def accept(request, obj, obj2, obj3, obj4):
    xyz = Finalowner(username = obj, first_name = obj2, last_name = obj3, email = obj4)
    xyz.save()
    abc = Owner.objects.get(username = obj)
    abc.delete()
    send_mail(
        'title is here',
        'message is here',
        'settings.EMAIL_HOST_USER',
        [obj4], #here it can be also a list of emails
        fail_silently = False
    )
    return redirect("/add")
    

def addproduct(request):
    
    if request.method == "POST":
        itemname = request.POST['itemname']
        category = request.POST['category']
        itemprice = request.POST['itemprice']
        lastdate = request.POST['lastdate']
        images = request.POST['images']

        if ( len(itemname) or len(itemprice) or len(category) or len(lastdate)) == 0:
            context={'successs':True,'mssg':"Please enter every field!!"}
            return render(request, 'seller.html', context)

        elif (images) == "":
            context={'successs':True,'mssg':"Please enter every field!!"}
            return render(request, 'seller.html', context)


        else:
            ins = Item(itemname = itemname, category = category, itemprice = itemprice, lastdate = lastdate, images = images)
            ins.save()
            context = {'success': True}
    return render(request, 'seller.html', context)


def select(request,obj1,obj2,obj3):
    context = {'name': obj1, 'price': obj2, 'lastdate': obj3}
    so = Item.objects.filter(itemname=obj1) 
    return render(request, 'select.html', context)

