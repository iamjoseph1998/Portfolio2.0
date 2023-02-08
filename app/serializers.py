from rest_framework import serializers
from app.models import Profile, Education


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'


class EducationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Education
        fields = '__all__'
