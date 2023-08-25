from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import *
from .serializers import *


class HelloAPI(APIView):
    def get(self, request):
        d = {
            "success":True,
            "xabar":"Salom, dunyo!"
        }
        return Response(d)
    def post(self, request):
        d = request.data
        javob = {
            "asosiy":"Post qabul qilindi",
            "ma'lumot":d
        }
        return Response(javob)

class AktyorlarAPIView(APIView):
    def get(self, request):
        aktyorlar = Aktyor.objects.all()
        serializer = AktyorSerializer(aktyorlar,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AktyorSerializer(data=request.data)
        if serializer.is_valid():
            Aktyor.objects.create(
                ism = serializer.validated_data.get("ism"),
                davlat=serializer.validated_data.get("davlat"),
                jins=serializer.validated_data.get("jins"),
                t_yil=serializer.validated_data.get("t_yil")
            )
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

class AktyorAPIView(APIView):
    def get(self, request, son):
        aktyor = Aktyor.objects.get(id=son)
        serializer = AktyorSerializer(aktyor)
        return Response(serializer.data)

    def delete(self, instance, son):
        aktyor = Aktyor.objects.filter(id=son).delete()
        d = {
            "success":True,
            "xabar":"Aktyor o'chirildi!"
        }
        return Response(d, status=status.HTTP_200_OK)

    def put(self, request, son):
        aktyor = Aktyor.objects.get(id=son)
        serializer = AktyorSerializer(aktyor, data=request.data)
        if serializer.is_valid():
            aktyor.ism = serializer.validated_data.get("ism")
            aktyor.davlat = serializer.validated_data.get("davlat")
            aktyor.jins = serializer.validated_data.get("jins")
            aktyor.t_yil = serializer.validated_data.get("t_yil")
            aktyor.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

class KinolarAPIView(APIView):
    def get(self, request):
        kinolar = Kino.objects.all()
        serializer = KinoSerializer(kinolar,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = KinoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)

class KinoAPIView(APIView):
    def get(self, request, son):
        kino = Kino.objects.get(id=son)
        serializer = KinoSerializer(kino)
        return Response(serializer.data)

    def put(self, request, son):
        kino = Kino.objects.get(id=son)
        serializer = KinoSerializer(kino, data=request.data)
        if serializer.is_valid():
            kino.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


class TariflarAPIView(APIView):
    def get(self, request):
        tariflar = Tarif.objects.all()
        serializer = TarifSerializer(tariflar,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TarifSerializer(data=request.data)
        if serializer.is_valid():
            Tarif.objects.create(
                nom=serializer.validated_data.get("nom"),
                narx=serializer.validated_data.get("narx"),
                davomiylik=serializer.validated_data.get("davomiylik")
            )
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

class TarifAPIView(APIView):
    def get(self, request, son):
        tarif = Tarif.objects.get(id=son)
        serializer = TarifSerializer(tarif)
        return Response(serializer.data)

    def delete(self, instance, son):
        tarif = Tarif.objects.filter(id=son).delete()
        d = {
            "success": True,
            "xabar": "Tarif o'chirildi!"
        }
        return Response(d, status=status.HTTP_200_OK)

    def put(self, request, son):
        tarif = Tarif.objects.get(id=son)
        serializer = TarifSerializer(tarif, data=request.data)
        if serializer.is_valid():
            tarif.nom = serializer.validated_data.get("nom")
            tarif.narx = serializer.validated_data.get("narx")
            tarif.davomiylik = serializer.validated_data.get("davomiylik")
            tarif.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)