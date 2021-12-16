from django.urls import path
from izzi import views

urlpatterns = [
    path('users/', views.UsersListApiView.as_view()),
]
