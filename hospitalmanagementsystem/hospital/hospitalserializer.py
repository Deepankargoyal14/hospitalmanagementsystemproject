from rest_framework import serializers
from hospital.models import Patient,LoginTable


class SignupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ['Patient_name', 'email','password','gender','phonenumber','address','birthdate','bloodgroup']

class LoginTableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LoginTable
        fields = ['csrfmiddlewaretoken', 'email']