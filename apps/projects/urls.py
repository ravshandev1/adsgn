from django.urls import path
from .views import CategoryView, ProjectView, ProjectDetailView

urlpatterns = [
    path('', ProjectView.as_view()),
    path('<int:pk>/', ProjectDetailView.as_view()),
    path('categories/', CategoryView.as_view()),
]
