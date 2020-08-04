from django.urls import path
from dp8app import views

app_name="dp8app"


urlpatterns=[
    path('trial/',views.trial,name="trial"),
    path('profile/',views.profile,name="profile"),
]