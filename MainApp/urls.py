from django.urls import path
from . import views
urlpatterns = [

    path('',views.homepage,name='homepage'),
    path('index/',views.homepage,name='homepage'),
    path('about/', views.about, name='about'),
    path('contact/',views.contact,name='contact'),
    path('recipes/',views.recipes,name='recipes'),
    path('reviews/',views.reviews,name='reviews'),
]