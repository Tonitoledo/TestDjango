from django.urls import path
from . import views

app_name='crud'

urlpatterns = [
    path('create/', views.invoice_create, name='crud_create'),
    path('list/', views.invoice_list, name='crud_list')
]