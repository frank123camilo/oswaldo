from django.urls import path
from . import views as v

urlpatterns = [
    path('base/', v.base, name='base'),
    path('', v.aprendices, name='aprendices'),
    path('agregar/', v.agregar, name='agregar'),
    path('editar/<int:id>/', v.editar, name='editar'),
    path('eliminar/<int:id>/', v.eliminar, name='eliminar'),
]
