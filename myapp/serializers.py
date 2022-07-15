from rest_framework import serializers
from .models import UserInfo

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=UserInfo
        fields=('name','branch','city')