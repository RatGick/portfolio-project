from django.urls import path
from . import views

urlpatterns = [
    path('', views.motherblog, name='motherblog'),
    path('<int:blog_id>/', views.detail, name='detail'),
]