from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.apiList, name='api-list'),
    path('email-list/', views.emailList, name='email-list'),
    path('email-detail/<str:pk>', views.emailDetail, name='email-detail'),
    path('email-create/', views.emailCreate, name='email-create'),
]