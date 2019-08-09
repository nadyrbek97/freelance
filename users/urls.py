from django.urls import path

from .views import (UserRegistrationView,
                    UserLoginView,)


urlpatterns = [
    path('registration/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login')
]
