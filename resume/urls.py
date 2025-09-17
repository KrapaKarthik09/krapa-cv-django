from django.urls import path
from . import views

app_name = 'resume'
urlpatterns = [
    path('', views.cv_view, name='cv'),
    path('about/', views.about_view, name='about'),
]
