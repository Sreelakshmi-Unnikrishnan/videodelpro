from django.shortcuts import render


from django.shortcuts import render
from . models import *
from .serializers import *
from django.http.response import HttpResponse
from rest_framework import status
def video(request):
    if request.method == 'GET':
        try:
            video = Video.objects.all()
            video_serializer = VideoSerializer(video, many = True)
            return HttpResponse(video_serializer.data, status=status.HTTP_200_OK)
        except:
            return HttpResponse({"Error": "Somthing went wrong!"}, status=status.HTTP_400_BAD_REQUEST) 
              
    if request.method == 'POST':
        try:
            data_video = request.data
            video_serializer = VideoSerializer(data=data_video)
            if video_serializer.is_valid():
                video_serializer.save()
                return HttpResponse(video_serializer.data, status=status.HTTP_200_OK)
            return HttpResponse(video_serializer.error, status=status.HTTP_403_FORBIDDEN)  
        except:
            return HttpResponse({'Error': 'Something went wrong!'}, status=status.HTTP_400_BAD_REQUEST)