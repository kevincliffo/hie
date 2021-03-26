from django.urls import path, include
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name="index"),
    path('about-us/', views.about, name="about-us"),
    path('my-care-plan/', views.mycareplan, name="my-care-plan"),
    path('my-care-team/', views.mycareteam, name="my-care-team"),
    path('contact/', views.contact, name="contact"),
    path('departments/', views.departments, name="departments"),
    path('doctors/', views.doctors, name="doctors"),
    path('blogs/', views.blogs, name="blogs"),
]
