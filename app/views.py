from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from app.models import Profile
from app.serializers import ProfileSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class AddProfile(generics.CreateAPIView):
    serializer_class = ProfileSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request, *args, **kwargs):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            first_name = data['first_name']
            last_name = data['last_name']
            email = data['email']
            phone = data['phone']
            address = data['address']
            photo = data['photo']
            profile_exists =  Profile.objects.all()
            if not profile_exists:
                obj = Profile.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    phone=phone,
                    address=address,
                    photo=photo
                )
                obj.save()
                return Response({'message': 'Profile added successfully!'}, status=status.HTTP_200_OK)
            return Response({'message': 'You cannot add more than one profile'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
