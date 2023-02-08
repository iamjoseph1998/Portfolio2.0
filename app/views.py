from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from app.models import Profile
from app.serializers import ProfileSerializer


class GetProfile(generics.ListAPIView):
    serializer_class = ProfileSerializer

    def get(self, request, *args, **kwargs):
        profile = Profile.objects.all().first()
        serializer = ProfileSerializer(profile, many=False)
        return Response({'message': serializer.data}, status=status.HTTP_200_OK)
