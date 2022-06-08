from django.urls import path
from travels_notebook.views import LoginUsers

urlpatterns = [
    path('login/users/', LoginUsers.as_view(), name='login'),
]
