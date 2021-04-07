from django.contrib import admin
from django.urls import path
from app_price_prediction  import views

urlpatterns = [
    path('',views.home),
    path('feedback/',views.feedback),

]