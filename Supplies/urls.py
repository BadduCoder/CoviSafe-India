from django.urls import path
from . import views

urlpatterns = [
    path('', views.SupplyListView.as_view()),
]
