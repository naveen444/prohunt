"""producthuntclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from . import views
from django.contrib.auth.views import(
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)


urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('update-profile/<int:user_id>/', views.chgprofile, name='chgprofile'),
    path('change-password/<int:user_id>/', views.chgpassword, name='chgpassword'),
]

# path('accounts/password/reset/',PasswordResetView.as_view(),name="password_reset"),
# path('accounts/password/reset/done/',PasswordResetDoneView.as_view(),name="password_reset_done"),
# path('accounts/password/reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
# path('accounts/password/done',PasswordResetCompleteView.as_view(),name="password_reset_complete"),
# path('accounts/', include('registration.backends.simple.urls')),
# path('admin/', admin.site.urls),



# path(‘accounts/password/reset/’, PasswordResetView.as_view(template_name=‘registration/password_reset_form.html’), name=‘password_reset’),
