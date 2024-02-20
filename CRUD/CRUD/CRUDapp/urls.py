from django.contrib import admin
from django.urls import path
from .views import home, show, send, edit, delete

urlpatterns = [
    path('', home.as_view(), name="home"),
    path('show/', show.as_view(), name="show"),
    # path('send/', send.as_view(), name='send'),
    path('edit/<int:pk>/', edit.as_view(), name='edit'),
    path('delete/<int:pk>/', delete.as_view(), name='delete')
]
