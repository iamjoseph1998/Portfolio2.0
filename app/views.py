from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from app.models import Profile, Education
from app.serializers import ProfileSerializer, EducationSerializer


class GetProfile(generics.ListAPIView):
    serializer_class = ProfileSerializer

    def get(self, request, *args, **kwargs):
        profile = Profile.objects.all().first()
        serializer = ProfileSerializer(profile, many=False)
        return Response({'message': serializer.data}, status=status.HTTP_200_OK)


class GetEducation(generics.ListAPIView):
    serializer_class = EducationSerializer

    def get(self, request, *args, **kwargs):
        education_list = Education.objects.all()
        serializer = EducationSerializer(education_list, many=True)
        return Response({'message': serializer.data}, status=status.HTTP_200_OK)
