from django.shortcuts import render, redirect
from todoapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from datetime import date
import time
from django.core.mail import send_mail
from django.conf import settings
import random

# Create your views here.


def home(request):
    from datetime import date
    last = Item.objects.filter(lastdate = date.today())
    last = list(last)
    for i in last:
        i.delete()
    area = request.session.get('area')
    if(area):
        items = list(Item.objects.filter(category__icontains = "Vegetables", area__icontains = area))
        ij = random.sample(items, 3)
        # for fruits
        items = list(Item.objects.filter(category__icontains = "Fruits", area__icontains = area))
        kl = random.sample(items, 3)
        # for electronics
        items = list(Item.objects.filter(category__icontains = "Electronics", area__icontains = area))
        mn = random.sample(items, 3)
        # for clothes
        items = list(Item.objects.filter(category__icontains = "Clothes", area__icontains = area))
        op = random.sample(items, 3)

        so = Item.objects.all()
        context = {'ij': ij, 'kl': kl, 'mn': mn , 'op': op, 'so': so, 'username':request.session.get('username')}
        return render(request, 'home.html', context)

    else:
        # without login
        # for vegetables
        date = date.today()
        items = list(Item.objects.filter(category__icontains = "Vegetables"))
        ab = random.sample(items, 3)
        # for fruits
        items = list(Item.objects.filter(category__icontains = "Fruits"))
        cd = random.sample(items, 3)
        # for electronics
        items = list(Item.objects.filter(category__icontains = "Electronics"))
        ef = random.sample(items, 3)
        # for clothes
        items = list(Item.objects.filter(category__icontains = "Clothes"))
        gh = random.sample(items, 3)

        so = Item.objects.all()
        context = {'ab': ab, 'cd': cd, 'ef': ef, 'gh': gh,'so': so, 'username':request.session.get('username')}
        return render(request, 'home.html', context)




    
def search(request):
    context = {'nopage': False}
    search = request.GET['search']
    area = request.session.get('area')

    so = Item.objects.filter(seller__icontains = search)
    ab = Item.objects.filter(itemname__icontains = search)

    if(area):
        cd = Item.objects.filter(seller__icontains = search, area__icontains = area)
        ef = Item.objects.filter(itemname__icontains = search, area__icontains = area)
        context = {'cd': cd, 'ef': ef, 'username': request.session.get('username')}
        return render(request, 'search.html', context)


    elif(len(so) or len(ab)) == 0:
        context = {'nopage': True}
        return render(request, 'search.html', context)
    
    else:
        so = Item.objects.filter(seller__icontains = search)
        ab = Item.objects.filter(itemname__icontains = search)
        context = {'so': so, 'ab': ab, 'username': request.session.get('username')}
        return render(request, 'search.html', context)
    


def about(request):
        
    return render(request, 'about.html')



def contact(request):

    context = {'success': False }
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
    
        if ( len(name) or len(email) or len(phone) or len(desc) )== 0:
            context={'successs':True,'mssg':"Please enter every field!!"}

        else:
            ins = Contact(name = name, email= email, phone = phone, desc = desc)
            ins.save()
            context = {'success': True }
            return render(request, 'contact.html', context)

    return render(request, 'contact.html', context)


def welcome(request):
    return render(welcome.html)


def seller(request):
    so = Finalowner.objects.filter(username = request.session.get('username'))
    context = {'so': so, 'username': request.session.get('username')}
    return render(request,"seller.html", context)

def loginuser(request):
    context = {'success': False, 'successs':False}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username= username, password = password)
        request.session['username'] = username

        if (Finalowner.objects.filter(username=username, password = password).exists()):
            login(request, user)
            so = Finalowner.objects.filter(username = username)
            context = {'username': request.session.get('username'), 'so': so}
            return redirect("/seller",context)
            context = {'successs':False}

        elif (Customer.objects.filter(username=username, password = password).exists()):
            login(request, user)
            so = Customer.objects.filter(username = username)
            for so in so:
                request.session['state'] = so.state
                request.session['city'] = so.city
                request.session['area'] = so.area
            context = {'username': request.session.get('username'), 'so': so}
            return redirect("/",context)
            context = {'successs':False}



        else:
            context= {'success':True, 'soham':"Please enter correct username or password!!!"}
            return render(request, 'login.html', context)



    return render(request, 'login.html', context)
    


def logout(request):
    try:
        del request.session['username']
        del request.session['state']
        del request.session['city']
        del request.session['area']
    except KeyError:
        pass
    return redirect('/')


def register(request):
    
    context = {'success': False, 'successs':False}
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        state = request.POST['state']
        city = request.POST['city']
        area = request.POST['area']
        pincode = request.POST['pincode']
        phone = request.POST['phone']

        if ( len(username) and len(first_name) and len(last_name) and len(email) and len(password1) and len(phone) and len(pincode)) == 0:
            context={'successs':True,'mssg':"Please enter every field!!"}

        elif (password1 != password2 ):
            context={'successs':True,'mssg':"Both passwords are not same!!"}

        elif (Customer.objects.filter(username=username).exists() ):
            context={'successs':True,'mssg':"Username exists!!"}
    
        elif (Owner.objects.filter(username=username).exists() ):
            context={'successs':True,'mssg':"Username exists!!"}
    
        elif (Finalowner.objects.filter(username=username).exists() ):
            context={'successs':True,'mssg':"Username exists!!"}
        
        elif ( Customer.objects.filter(email=email).exists() ):
            context={'successs':True,'mssg':"Email exists!!"}

        elif ( Owner.objects.filter(email=email).exists() ):
            context={'successs':True,'mssg':"Email exists!!"}

        elif (Finalowner.objects.filter(email=email).exists() ):
            context={'successs':True,'mssg':"Email exists!!"}


        else:
            ins = Customer(username = username, first_name = first_name, last_name = last_name, email = email, password = password1, state = state, city =city, area = area, pincode = pincode, phone = phone)
            ins.save()
            context = {'success': True}
            return render(request, 'register.html', context)


    return render(request, 'register.html', context)



def update(request, obj1, obj2, obj3, obj4, obj5, obj6, obj7, obj8, obj9, obj10):
    context = {'success': False, 'successs':False, 'username': request.session.get('username')}
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        state = request.POST['state']
        city = request.POST['city']
        area = request.POST['area']
        pincode = request.POST['pincode']

        if (len(username) and len(first_name) and len(last_name) and len(state) and len(city) and len(area) and len(pincode) ) == 0:
            context={'successs':True,'mssg':"Please enter every field!!"}

        elif (Customer.objects.filter(username=username).exists() ):
            context={'successs':True,'mssg':"Username exists!!"}
    
        elif (Owner.objects.filter(username=username).exists() ):
            context={'successs':True,'mssg':"Username exists!!"}
    
        elif (Finalowner.objects.filter(username=username).exists() ):
            context={'successs':True,'mssg':"Username exists!!"}
        


        else:
            abc = Customer.objects.get(username = obj1)
            abc.delete()

            ins = Customer(username = username, first_name = first_name, last_name = last_name, email = obj4, password = obj5, state = state, city =city, area = area, pincode = pincode, phone = obj6)
            ins.save()
            context = {'success': True, 'mssg':"Changes made successfully", 'username': request.session.get('username')}
            return render(request, 'home.html', context)


    return redirect('/userprofile', context)






def owner(request):
    
    context = {'success': False, 'successs':False, 'mssg':""}
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        state = request.POST['state']
        city = request.POST['city']
        area = request.POST['area']
        pincode = request.POST['pincode']
        email = request.POST['email']
        phone = request.POST['phone']
        images1 = request.FILES['images1']
        images2 = request.FILES['images2']
        images3 = request.FILES['images3']

        if ( len(username) and len(first_name) and len(phone) and len(last_name) and len(email) and len(state) and len(city) and len(area) and len(pincode) and len(password1) and len(password2) ) == 0:
            context={'successs':True,'mssg':"Please enter every field!!"}

        elif  len(username)>= 21:
            context={'successs':True,'mssg':"Please enter username with less than 20 characters!!"}


        elif (password1 != password2):
            context={'successs':True,'mssg':"Username exists!!"}

        elif (Customer.objects.filter(username=username).exists() ):
            context={'successs':True,'mssg':"Username exists!!"}

        elif (Owner.objects.filter(username=username).exists() ):
            context={'successs':True,'mssg':"Username exists!!"}
            
        elif (Finalowner.objects.filter(username=username).exists() ):
            context={'successs':True,'mssg':"Username exists!!"}

        elif (Customer.objects.filter(email=email).exists() ):
            context={'successs':True,'mssg':"Email exists!!"}

        elif (Owner.objects.filter(email=email).exists() ):
            context={'successs':True,'mssg':"Email exists!!"}

        elif (Finalowner.objects.filter(email=email).exists() ):
            context={'successs':True,'mssg':"email exists!!"}


        else:
            ins = Owner.objects.create(username = username, first_name = first_name, last_name = last_name, password = password1, state = state, city = city, area = area, pincode = pincode, email = email, phone = phone, images1 = images1, images2 = images2, images3 = images3)
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
    try:
        send_mail(
        'Sorry!!!',
        'sorry ur profile is rejected by volo mart due to some documents issued by you are incorrect...',
        'settings.EMAIL_HOST_USER',
        [email], #here it can be also a list of emails
        fail_silently = False)
    except:
        pass
    return redirect("/add")


def view(request, obj, obj2, obj3, obj4):
    context = {'name': obj, 'first_name': obj2, 'last_name': obj3, 'email': obj4}
    return render(request, 'view.html', context)


def accept(request, obj1, obj2, obj3, obj4, obj5, obj6, obj7, obj8, obj9, obj10):
    xyz = Finalowner(username = obj1, first_name = obj2, last_name = obj3, password = obj10,  state = obj4, city = obj5, area = obj6, pincode = obj7, email = obj8, phone = obj9)
    xyz.save()
    abc = Owner.objects.get(username = obj1)
    abc.delete()
    try:
        send_mail(
        'Conguratulation!!!',
        'Your profile is been selected by volomart, Now you can add your products into volomart with your volomart username.',
        'settings.EMAIL_HOST_USER',
        [obj8], #here it can be also a list of emails
        fail_silently = False)
    except:
        pass
    return redirect("/add")
    

def addproduct(request, obj1, obj2, obj3, obj4):

    if request.method == "POST":
        seller = obj1
        itemname = request.POST['itemname']
        category = request.POST['category']
        old_itemprice = request.POST['old_itemprice']
        new_itemprice = request.POST['new_itemprice']
        discription = request.POST['discription']
        key_features1 = request.POST['key_features1']
        key_features2 = request.POST['key_features2']
        key_features3 = request.POST['key_features3']
        key_features4 = request.POST['key_features4']
        lastdate = request.POST['lastdate']
        images = request.FILES['images']
        state = obj2
        city = obj3
        area = obj4
        address = (f"{obj4},{obj3},{obj2}")
        percentage =  100-((int(new_itemprice)/int(old_itemprice))*100)
        

        if (len(itemname) or len(new_itemprice) or len(category) or len(lastdate)) == 0:
            context={'successs':True,'mssg':"Please enter every field!!"}
            return render(request, 'seller.html', context)


        elif (int(old_itemprice) < int(new_itemprice)):
            context={'successs':True,'mssg':"new item price should be less than old item price!!"}
            return render(request, 'seller.html', context)


        elif (images) == "":
            context={'successs':True,'mssg':"Please enter every field!!"}
            return render(request, 'seller.html', context)


        else:
            ins = Item(seller = seller, itemname = itemname, category = category, old_itemprice = old_itemprice, new_itemprice = new_itemprice, percentage = percentage, discription = discription, key_features1 = key_features1, key_features2 = key_features2, key_features3 = key_features3, key_features4 = key_features4, lastdate = lastdate, state = state, city = city, area = area, address = address, images = images)
            ins.save()
            context = {'success': True, 'username':obj1}
            return redirect('/seller', context)
    return render(request, 'seller.html', context)


def select(request,obj1,obj2,obj3,obj4,obj5):
    so = Item.objects.filter(itemname = obj1, old_itemprice = obj2, new_itemprice = obj3, discription = obj5)
    context = {'name': obj1, 'old_price': obj2, 'new_price': obj3, 'lastdate': obj4, 'username': request.session.get('username'),'so': so}
    return render(request, 'select.html', context)


def ordering(request, obj1, obj2, obj3, obj4):
    context = {'success': False, 'sellername':obj1, 'productname':obj2, 'oldprice': obj3, 'newprice':obj4, 'username':  request.session.get('username')}
    return render(request, 'ordering.html', context)
    

def order(request, obj1, obj2, obj3):
    if request.method == "POST":
        piece = request.POST['piece']
        productname = obj2
        username =  request.session.get('username')
        sellername = obj1
        paymentmode = request.POST['paymentmode']
        price = obj3
        abc = Order_placed( username = username, sellername = sellername, itemname = productname, paymentmode = paymentmode, piece = piece, price = price)
        abc.save()
        context = {'success': True}

        if(paymentmode == "online"):
            return redirect(f'/payment/{productname}/{int(price)}')
        else:
            abc = Order_placed.objects.get( username = username, sellername = sellername, itemname = productname, paymentmode = paymentmode, piece = piece, price = price)
            abc.delete()
        
            abc = Final_order_placed( username = username, sellername = sellername, itemname = productname, paymentmode = paymentmode, piece = piece, price = price)
            abc.save()
            return redirect("/")


    return render(request, 'order.html')




def productlist(request):
    so = Item.objects.filter(seller = request.session.get('username'))
    context = {'so': so}
    return render(request, 'productlist.html', context)






def userprofile(request):
    so = Customer.objects.filter(username = request.session.get('username'))
    ab = Save.objects.filter(username = request.session.get('username'))
    context = {'username': request.session.get('username'), 'so': so, 'ab': ab}
    return render(request, 'userprofile.html', context)


def more(request, obj1):
    context = {'nopage': False}
    so = Item.objects.all()
    ab = Item.objects.filter(category = obj1)
    cd = Item.objects.filter(category = obj1, state = "Maharashtra", city = "Mumbai", area = "Vasairoad(west)")
    if (len(ab) or len(cd)) == 0:
        context = {'obj': obj1, 'ab': ab, 'cd': cd, 'so': so, 'username': request.session.get('username'), 'nopage': True}
        return render(request, 'more.html', context)
    else:
        context = {'obj': obj1, 'ab': ab, 'cd': cd, 'so': so, 'username': request.session.get('username')}
        return render(request, 'more.html', context)

    context = {'obj': obj1, 'ab': ab, 'cd': cd, 'so': so, 'username': request.session.get('username')}
    return render(request, 'more.html', context)



def deleteproduct(request, obj1, obj2, obj3):
    abc = Item.objects.get(seller = obj1, itemname = obj2, new_itemprice = obj3)
    abc.delete()
    return redirect("/productlist")


def checkorders(request):
    context = {'so': Final_order_placed.objects.filter(sellername = request.session.get('username'))}
    return render(request, 'checkorders.html', context)


def deleteorders(request, obj1, obj2, obj3, obj4):
    obj1 = obj1
    obj2 = obj2
    obj3 = obj3
    obj4 = obj4
    ab = Order_placed.objects.filter(username = obj1, sellername = obj2, itemname = obj3, price = obj4)
    ab.delete()
    so = Customer.objects.filter(username = obj1)
    for so in so:
        email = so.email
    mssg = "Sorry your order for "+ obj3 + " is canceled!!!"
    try:
        send_mail(
        'Sorry!!!',
        mssg,
        'settings.EMAIL_HOST_USER',
        [email], #here it can be also a list of emails
        fail_silently = False)
    except:
        pass
    return redirect("/checkorders")

def placeorders(request, obj1, obj2, obj3, obj4):
    obj1 = obj1
    obj2 = obj2
    obj3 = obj3
    obj4 = obj4
    ab = Order_placed.objects.filter(username = obj1, sellername = obj2, itemname = obj3, price = obj4)
    ab.delete()
    so = Customer.objects.filter(username = obj1)
    for so in so:
        email = so.email
    mssg = "Hey your order for "+ obj3 + " is send for delivery!!!"
    try:
        send_mail(
        'Hey!!!',
        mssg,
        'settings.EMAIL_HOST_USER',
        [email], #here it can be also a list of emails
        fail_silently = False)
    except:
        pass
    return redirect("/checkorders")


def deletesave(request, obj1, obj2, obj3):
    ins = Save.objects.filter(username = request.session.get('username'), seller = obj1 ,category = obj2 , itemname = obj3)
    ins.delete()
    return redirect("/userprofile")

def savee(request, obj1, obj2, obj3, obj4, obj5, obj6):
    ins = Save(username = request.session.get('username'), seller = obj1, category = obj2, itemname = obj3, old_itemprice = obj4, new_itemprice = obj5, lastdate = obj6)
    ins.save()
    return redirect("/")


def selectt(request,obj1,obj2,obj3,obj4):
    so = Item.objects.filter(itemname = obj1, old_itemprice = obj2, new_itemprice = obj3)
    context = {'name': obj1, 'old_price': obj2, 'new_price': obj3, 'lastdate': obj4, 'username': request.session.get('username'),'so': so}
    return render(request, 'select.html', context)