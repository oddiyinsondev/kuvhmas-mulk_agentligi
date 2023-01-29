from django.urls import path
from .views import mulk, uy, haqida, BlogFiyle, aloqa

urlpatterns = [
    path('mulk',mulk, name='mulk' ),
    path('', uy, name='uy'),
    path('haqida', haqida, name='haqida' ),
    path('Blog', BlogFiyle, name='blog'),
    path('aloqa', aloqa, name='aloqa'),
    
]

