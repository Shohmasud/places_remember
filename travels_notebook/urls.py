from django.urls import path, include
from travels_notebook.views import LoginUsers, \
    PlacesList, ShowPostRemember, GetMap

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('login/users/', LoginUsers.as_view(), name='login'),
    path('show/list/remembers/', PlacesList.as_view(), name='home'),
    path('page/form/map/<slug:slug>', GetMap.as_view(), name='form-page'),
    path('show/post/<slug:slug>', ShowPostRemember.as_view(), name='show-post'),
]
