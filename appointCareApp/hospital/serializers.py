from rest_framework import serializers
from ..models import Hospital,HospitalDetails,DoctorsDetails,PatientDetails

class HospitalRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ('email', 'phone_number', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        hospital = Hospital(**validated_data)
        hospital.set_password(password)
        hospital.save()
        return hospital

class HospitalLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)



class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model=HospitalDetails
        fields=("id","hospital_Image","hospital_Location","hospital_Slogan","hospital_Description",)



class DoctorsSerializer(serializers.ModelSerializer):
    class Meta:
        model=DoctorsDetails
        fields=('id','doctorImage','doctorName','doctorSpeciality',)


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDetails
        fields = ['id', 'patientName', 'patientAge', 'patientContact','patientDisease','timeBooked','patientDoctor',]        
