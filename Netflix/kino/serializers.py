from rest_framework  import serializers
from .models import *

class AktyorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    ism = serializers.CharField()
    davlat = serializers.CharField()
    jins = serializers.CharField()
    t_yil = serializers.DateField()

class KinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kino
        fields = ['id','nom','janr','yil','aktyorlar']  # yoki "__all__"

class TarifSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nom = serializers.CharField()
    narx = serializers.IntegerField()
    davomiylik = serializers.CharField()