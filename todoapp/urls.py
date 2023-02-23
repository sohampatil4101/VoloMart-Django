from django.urls import path
from todoapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name="home" ),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('login', views.loginuser, name="loginuser"),
    path('welcome', views.welcome, name="welcome"),
    path('register', views.register, name="register"),
    path('owner', views.owner, name="owner"),
    path('add', views.add, name="add"),
    path('addproduct', views.addproduct, name="addproduct"),
    path('delete/<str:name>/<str:email>', views.delete, name="delete"),
    path('select/<str:obj1>/<str:obj2>/<str:obj3>', views.select, name="select"),
    path('view/<str:obj>/<str:obj2>/<str:obj3>/<str:obj4>', views.view, name="view"),
    path('accept/<str:obj>/<str:obj2>/<str:obj3>/<str:obj4>', views.accept, name="accept")

]

if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


    # latest changes made