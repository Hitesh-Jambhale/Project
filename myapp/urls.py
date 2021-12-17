from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name="homepage"),
    path('create/', create_view, name="createpage"),
    path('update/<int:pk>/', update_view, name='updatepage'),
    path('delete/<int:pk>/',delete_view, name='deletepage')

]
