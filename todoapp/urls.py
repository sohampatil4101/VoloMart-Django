from django.urls import path
from todoapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name="home" ),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('login', views.loginuser, name="loginuser"),
    path('logout', views.logout, name="logout"),
    path('welcome', views.welcome, name="welcome"),
    path('register', views.register, name="register"),
    path('owner', views.owner, name="owner"),
    path('add', views.add, name="add"),
    path('seller', views.seller, name="seller"),
    path('addproduct/<str:obj1>/<str:obj2>/<str:obj3>/<str:obj4>', views.addproduct, name="addproduct"),
    path('delete/<str:name>/<str:email>', views.delete, name="delete"),
    path('deleteproduct/<str:obj1>/<str:obj2>/<str:obj3>', views.deleteproduct, name="deleteproduct"),
    path('select/<str:obj1>/<str:obj2>/<str:obj3>/<str:obj4>/<str:obj5>', views.select, name="select"),
    path('selectt/<str:obj1>/<str:obj2>/<str:obj3>/<str:obj4>', views.selectt, name="selectt"),
    path('view/<str:obj>/<str:obj2>/<str:obj3>/<str:obj4>', views.view, name="view"),
    path('accept/<str:obj1>/<str:obj2>/<str:obj3>/<str:obj4>/<str:obj5>/<str:obj6>/<str:obj7>/<str:obj8>/<str:obj9>/<str:obj10>', views.accept, name="accept"),
    path('update/<str:obj1>/<str:obj2>/<str:obj3>/<str:obj4>/<str:obj5>/<str:obj6>/<str:obj7>/<str:obj8>/<str:obj9>/<str:obj10>', views.update, name="update"),
    path('order/<str:obj1>/<str:obj2>/<int:obj3>', views.order, name="order"),
    path('ordering/<str:obj1>/<str:obj2>/<str:obj3>/<str:obj4>', views.ordering, name="ordering"),
    path('productlist', views.productlist, name="productlist"),
    path('more/<str:obj1>', views.more, name="more"),
    path('userprofile', views.userprofile, name="userprofile"),
    path('search', views.search, name="search"),
    path('checkorders', views.checkorders, name="checkorders"),
    path('deleteorders/<str:obj1>/<str:obj2>/<str:obj3>/<str:obj4>', views.deleteorders, name="deleteorders"),
    path('placeorders/<str:obj1>/<str:obj2>/<str:obj3>/<str:obj4>', views.placeorders, name="placeorders"),
    path('deletesave/<str:obj1>/<str:obj2>/<str:obj3>', views.deletesave, name="deletesave"),
    path('savee/<str:obj1>/<str:obj2>/<str:obj3>/<str:obj4>/<str:obj5>/<str:obj6>', views.savee, name="savee")

]

if settings.DEBUG :
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


# latest 14-03-2023