from django.urls import path
from . import views

app_name='crud'

urlpatterns = [
    path('', views.invoice_list_and_create, name='crud_list')
]