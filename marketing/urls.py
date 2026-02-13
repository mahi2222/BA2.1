from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Updated paths to reflect marketing/templates/marketing/
    path('marketing/templates/marketing/signup.html', views.signup, name='signup'),
    path('marketing/templates/marketing/signin.html', views.signin, name='signin'),
    path('marketing/templates/marketing/dashboard/', views.dashboard, name='dashboard'),

    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('logout/', views.signout, name='signout'),
]