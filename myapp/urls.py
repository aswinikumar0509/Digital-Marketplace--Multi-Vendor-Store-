from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index , name='index'),
    path('product/<int:id>',views.detail , name='detail'),
    path('create_product/',views.create_product,name ='create_product'),
    path('editproduct/<int:id>/',views.product_edit,name='editproduct'),
    path('delete/<int:id>/',views.product_delete,name='delete'),
    
]