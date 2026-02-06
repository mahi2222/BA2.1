from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup.html', views.signup, name='signup'), # Keeping .html for backward compatibility with existing links
    path('signin.html', views.signin, name='signin'),
]
