from django.contrib import admin
from django.urls import path
from .views import signin, signup, logout, home, about, contact, feedback, facial, cleanup, hairspa, wax, appointment, \
    gallery, showdetail, showfeedback

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',signin),
    path('signup/',signup,name='signup'),
    path('profile/',logout,name='profile'),
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('feedback/', feedback, name='feedback'),
    path('facial/', facial, name='facial'),
    path('cleanup/', cleanup, name='cleanup'),
    path('hairspa/', hairspa, name='hairspa'),
    path('wax/', wax, name='wax'),
    path('appointment/', appointment, name='appointment'),
    path('gallery/', gallery, name='gallery'),
    path('details/',showdetail,name='showdetail'),
    path('showfeedback/', showfeedback, name='showfeedback'),

]
