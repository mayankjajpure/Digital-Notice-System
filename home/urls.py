
from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',views.landing),
    path('login',views.loginuser),
    path('logout',views.logoutuser),
    path('feeds',views.feeds),
    path('blog/<slug:url>',views.showpost),
    path('register',views.register),
    path('base',views.base),
    path('about',views.about),
    path('contact',views.contact),
    path('send',views.send),
    path('category/<slug:url>',views.category),
    path('sendnotice',views.sendnotice),
    path('feedback',views.feedbck),
    path('registor',views.registor),

    

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

