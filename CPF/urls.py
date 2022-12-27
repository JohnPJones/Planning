from django.urls import path 
from .views import CPFPlanning

urlpatterns = [

path('',CPFPlanning,name = 'Planning')

]