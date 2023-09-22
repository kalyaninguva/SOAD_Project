from rest_framework import serializers
from noticeboard.models import NoticeBoard

class NoticeBoardSerializer(serializers.Serializer):
    name_of_organisation = serializers.CharField()
    date = serializers.DateField()
    title = serializers.CharField()
    notice_text = serializers.CharField()
    name = serializers.CharField()
    designation = serializers.CharField()
    enteredBy = serializers.SlugRelatedField(read_only= True, slug_field='username')

    def create(self, validated_data):
        return NoticeBoard(**validated_data)

    def update(self, instance, validated_data):
        instance.name_of_organisation = validated_data.get('name_of_organisation', instance.name_of_organisation)
        instance.date = validated_data.get('date', instance.date)
        instance.title = validated_data.get('title', instance.title)
        instance.notice_text = validated_data.get('notice_text', instance.notice_text)
        instance.name = validated_data.get('name', instance.name)
        instance.designation = validated_data.get('designation', instance.designation)
        instance.save()
        return instance  