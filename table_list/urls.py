from django.urls import path
from . import views

urlpatterns = [
    path('api/list/', views.TableListCreate.as_view() ),
]