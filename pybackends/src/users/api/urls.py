from django.urls import path

from .views import (
    UserListView,
    UserDetailView,
    UserUpdateView,
    UserDeleteView,
    UserCreateView
)

urlpatterns = [
    path('', UserListView.as_view()),
    path('create/', UserCreateView.as_view()),
    path('update/<pk>', UserUpdateView.as_view()),
    path('delete/<pk>', UserDeleteView.as_view()),
    path('<pk>', UserDetailView.as_view())
]
