from django.urls import path, include
from .views import IstUserListView

urlpatterns = [
    path('', IstUserListView.as_view()),
]