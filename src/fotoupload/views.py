from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.views.generic import TemplateView
from .models import Foto
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from .serializer import FotoSerializer


class HomeView(TemplateView):
    """ Главная страница """
    template_name = 'fotoupload/home.html'


# def upload_foto(request):
#     """ FBV Функция загрузки фотографии """
#     if request.method == 'POST':
#         file_item = request.FILES.get('item')
#         Foto.objects.create(
#             item=file_item,
#             info=file_item.name
#             )
#         return JsonResponse({'data': 'ok'}, safe=False)
#     return JsonResponse({'data': 'error'}, safe=False)


class UploadFotoView(APIView):
    """ CBV Загрузка фотографии """
    parser_classes = (MultiPartParser, )
    
    def post(self, request, format=None):
        serializer = FotoSerializer(data=request.FILES)

        if serializer.is_valid():
            serializer.save(info=request.FILES.get('item').name)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

