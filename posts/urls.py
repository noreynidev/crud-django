from django.urls import path
from . import views

app_name='posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('listings', views.listings, name='listings'),
    path('details/<int:pk>', views.details, name='details'),
    path('create', views.create, name='create'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),
]