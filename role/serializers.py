from rest_framework import serializers
from  .models import *
class ChildSerializer(serializers.ModelSerializer):

    class Meta:
        model = Child
        fields = '__all__'

        read_only_fields = ('id',)


class NavSerializer(serializers.ModelSerializer):
    children = ChildSerializer(many=True, read_only=True)
    class Meta:
        model = Nav
        fields = '__all__'
        read_only_fields = ('id',)

class RoleSerializer(serializers.ModelSerializer):
    navs = NavSerializer(many=True, read_only=True)

    class Meta:
        model = Role
        fields = '__all__'
        read_only_fields = ('id',)
