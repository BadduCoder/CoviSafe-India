from django.urls import path
from . import views

urlpatterns = [
    path('', views.RequirementListView.as_view()),
    path('<int:pk>', views.RequirementDetailView.as_view())
]
