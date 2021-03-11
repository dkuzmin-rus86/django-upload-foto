from rest_framework import serializers
from .models import Foto


class FotoSerializer(serializers.ModelSerializer):
    ''' Сериализация модели Foto '''
    
    class Meta:
        model = Foto
        fields = ('item', )
