from django.urls import path
from django.conf.urls import url
from . import views

from rest_framework.urlpatterns import format_suffix_patterns

# app_name = 'surgery' 

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('surgery/', views.index.as_view()),
    path('info/', views.Info.as_view()),
    path('info/<str:animalid>/', views.Info.as_view(), name='info'),
    # path(r'^info/(?P<animalid>\w+)/$', views.Info.as_view()),
    # path('/info/', views.Info.as_view()),
    # path('aav_inject', views.aav_inject, name='aav_inject'),
    # path('animalinfo/<str:pk>', views.AnimalInfo.as_view(), name = 'animalinfo'),
    # path('animallist', views.AnimalList.as_view(), name = 'animallist'),  
    # path('add', views.AddAnimalView, name = 'add_animal'),
    # path('animallist/', views.AnimalList.as_view()),
    ]