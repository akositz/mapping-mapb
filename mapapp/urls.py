from django.conf.urls import url
from mapapp import views

urlpatterns = [
    url(r'pointdata/', views.point_data),
    url(r'^', views.index),
]
