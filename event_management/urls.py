from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('', views.event_list, name='event_list'),  # UPDATED LINE
    path('events/<int:pk>/', views.event_detail, name='event_detail'),
    path('events/<int:event_id>/register/', views.register_event, name='register_event'),
    path('registrations/', views.registration_list, name='registration_list'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('register/', views.user_register_view, name='register'),
]

 