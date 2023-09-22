from rest_framework import serializers
from estimate_salary.models import salary_data

class SalaryDataSerializer(serializers.Serializer):
    # id=serializers.IntegerField()
    experience = serializers.IntegerField()
    job_location = serializers.CharField(max_length=15)
    score = serializers.IntegerField()
    subject = serializers.CharField(max_length=15)
    salary = serializers.IntegerField()
    def create(self, validated_data):
        return salary_data.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # instance.id = 
        instance.experience = validated_data.get('experience', instance.experience)
        instance.job_location = validated_data.get('job_location', instance.job_location)
        instance.score = validated_data.get('score', instance.score)
        instance.subject = validated_data.get('subject', instance.subject)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.save() 
        return instance  