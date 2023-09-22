from rest_framework import serializers
from schools.models import SchoolData

class SchoolDataSerializer(serializers.Serializer):
    location = serializers.CharField(max_length = 50)
    sid = serializers.IntegerField()
    name = serializers.CharField()
    strength = serializers.IntegerField()
    typeOfSchool = serializers.CharField()
    adress = serializers.CharField()
    achievements = serializers.CharField()
    capacity = serializers.IntegerField()
    contactInfo = serializers.IntegerField()
    enteredBy = serializers.SlugRelatedField(read_only = True,slug_field='username')

    def create(self,validated_data):
        print('Creating')
        print(**validated_data)
        # return salary_data.objects.create(**validated_data)
        return SchoolData(**validated_data)

    def update(self, instance, validated_data):
        instance.location = validated_data.get('location', instance.location)
        instance.sid = validated_data.get('sid', instance.sid)
        instance.name = validated_data.get('name', instance.name)
        instance.strength = validated_data.get('strength', instance.strength)
        instance.typeOfSchool = validated_data.get('typeOfSchool', instance.typeOfSchool)
        instance.adress = validated_data.get('adress', instance.adress)
        instance.achievements = validated_data.get('achievements', instance.achievements)
        instance.capacity = validated_data.get('capacity', instance.capacity)
        instance.contactInfo = validated_data.get('contactInfo', instance.contactInfo)
        instance.save()
        return instance  
