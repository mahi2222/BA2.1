from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup.html', views.signup, name='signup'), # Keeping .html for backward compatibility with existing links
    path('signin.html', views.signin, name='signin'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('logout/', views.signout, name='signout'),
]
