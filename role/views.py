import uuid

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Role
from .serializers import RoleSerializer


# class RoleListApiView(generics.ListAPIView):
#     queryset = Role.objects.all()
#     serializer_class = RoleSerializer

# class RoleDetailApiView(generics.RetrieveAPIView):
#
#     queryset = Role.objects.all()
#     serializer_class = RoleSerializer
#
# class RoleCreateApiView(generics.CreateAPIView):
#     queryset = Role.objects.all()
#     serializer_class = RoleSerializer
#
# class RoleUpdateViewApiView(generics.RetrieveUpdateAPIView):
#     queryset = Role.objects.all()
#     serializer_class = RoleSerializer
#
# class RoleDeleteApiView(generics.RetrieveDestroyAPIView):
#     queryset = Role.objects.all()
#     serializer_class = RoleSerializer


class RoleView(APIView):
    def get(self, request, format=None):
        roles = Role.objects.all()
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data)
