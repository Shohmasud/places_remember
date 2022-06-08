from django.urls import path,include
from travels_notebook.views import LoginUsers

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('login/users/', LoginUsers.as_view(), name='login'),
]
