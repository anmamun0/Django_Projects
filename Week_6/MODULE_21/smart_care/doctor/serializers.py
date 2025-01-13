from rest_framework import serializers
from .models import (
    Specialization,
    Designation,
    AvailableTime,
    Doctor,
    Review,
)

class DoctorSerialier(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    designation = serializers.StringRelatedField(many=True)
    specialization = serializers.StringRelatedField(many=True)
    AvailableTime = serializers.StringRelatedField(many=True)
    class Meta:
        model = Doctor
        fields = '__all__'

class SpecializationSerialier(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(many=False)
    class Meta:
        model = Specialization
        fields = '__all__'

class DesignationSerialier(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(many=False)
    class Meta:
        model = Designation
        fields = '__all__'

class AvailableTimeSerialier(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(many=False)
    class Meta:
        model = AvailableTime
        fields = '__all__'

class ReviewSerialier(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(many=False)
    class Meta:
        model = Review
        fields = '__all__'