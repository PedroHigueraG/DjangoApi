from rest_framework import serializers
from authApp.models.user import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'name', 'email', 'tel','location','address','is_Suscribed','gender']