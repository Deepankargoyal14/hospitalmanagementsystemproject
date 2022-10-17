from rest_framework import serializers
from hospital.models import Patient


class SignupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ['Patient_name', 'email','password','gender','phonenumber','address','birthdate','bloodgroup']