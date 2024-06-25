from django.urls import path

from .views import *

urlpatterns = [
    # path('', RoleListApiView.as_view(), name='role-list'),
    # path('roles/create/', RoleCreateApiView.as_view(), name='role-create'),
    # path('roles/<int:pk>/', RoleDetailApiView.as_view(), name='role-detail'),
    # path('roles/update/', RoleUpdateViewApiView.as_view(), name='role-update'),
    path('roles/', RoleView.as_view(), name='role-list'),
]