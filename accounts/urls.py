from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from . import views
app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="registration/login.html"),name='login'),
    path('logout/', auth_views.LoginView.as_view(template_name='registration/login.html'), name="logout"),
    
    # path('', include('django.contrib.auth.urls')),
    # path('password_change/', auth_views.PasswordChangeView.as_view(), name="password_change"),
    # path('password_reset/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset_form.html"), name="password_reset"),
    path(
        'password_reset/',
        auth_views.PasswordResetView.as_view(email_template_name='registration/password_reset_emails.html',
        success_url='done',
        subject_template_name='registration/password_reset_subjects.txt',
        ),
        name='password_reset',
    ),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('accounts:login')), name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),      

    path('password_change/', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('home')),name='password_change',),
    # path(
    #     'admin/password_reset/done/',
    #     auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_done.html"),
    #     name='password_reset_done',
    # ),
    # path(
    #     'reset/<uidb64>/<token>/',
    #     auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"),
    #     name='password_reset_confirm',
    # ),
    # path(
    #     'reset/done/',
    #     auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_form.html"),
    #     name='password_reset_complete',
    # ),

]
