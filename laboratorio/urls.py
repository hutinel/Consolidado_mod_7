from django.urls import path
from . import views


#La caracteristica de poner int:id permite usar el numero de id para buscar un laboratorio mediante la url
#Ejemplo: http://localhost:8000/1/update/ accede a la vista de actualización del laboratorio con id 1.
urlpatterns = [
    path('', views.index, name='index'),
    path('lista/', views.laboratorio_list, name='laboratorio_list'),
    path('<int:id>/', views.laboratorio_detail, name='laboratorio_detail'),
    path('create/', views.laboratorio_create, name='laboratorio_create'),
    path('<int:id>/update/', views.laboratorio_update, name='laboratorio_update'),
    path('<int:id>/delete/', views.laboratorio_delete, name='laboratorio_delete'),
]
