from django.urls import path
from . import views


#mit views.hello wird funktion hello aufgerufen
urlpatterns =[
    path('', views.hello),
    path('einträge/', views.einträge)
]