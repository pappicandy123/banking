from django.urls import path
from .views import *


urlpatterns = [
    path('',index,name='index'),
    path('main', main, name='main'),
    path('signup', signup, name='signup'),
    path('savings', savings, name='savings'),
    path('checkings', checkings, name='checkings'),
    path('sucesspage', sucesspage, name='sucesspage'),
    path('credit', credit, name='credit'),
    path('credit_saving', credit_saving, name='credit_saving'),
    path('transfer', transfer, name='transfer'),
    path('transferbank', transferbank, name='transferbank')



]
