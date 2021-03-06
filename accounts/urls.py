from . import views
from django.conf.urls import url
from django.contrib.auth.views import (
LoginView,
LogoutView,
PasswordResetView,
PasswordResetDoneView,
PasswordResetConfirmView,
PasswordResetCompleteView,
)
from django.urls import path



urlpatterns = [
    path('',views.home,name="home"),
    path('login',LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('logout',LogoutView.as_view(template_name='accounts/logout.html'), name="logout"),
    path('register',views.register,name='register'),
    path('profile',views.profile,name='profile'),
    path('edit_profile',views.edit_profile,name='edit_profile'),
    path('change_password',views.change_password,name='change_password'),
    path('reset-password', PasswordResetView.as_view(template_name='accounts/reset_password.html'),name='reset_password'),
    path('reset-password/done',PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>',PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset-password/complete',PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]
#    python -m smtpd -n -c DebuggingServer localhost:1025

