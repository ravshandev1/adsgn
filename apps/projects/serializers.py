from rest_framework import serializers
from .models import Project, ParticipantOfProject, Category, Video, Image


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ParticipantOfProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipantOfProject
        fields = ['name', 'image', 'profession']

    profession = serializers.CharField(source='participant.profession.name')
    name = serializers.CharField(source='participant.name')
    image = serializers.CharField(source='participant.get_image')


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['get_video']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['get_image']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'category', 'image']

    image = serializers.SerializerMethodField()
    category = serializers.CharField(source='category.name')

    @staticmethod
    def get_image(obj):
        if obj.images:
            return obj.images.first().get_image
        return ''


class ProjectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'images', 'videos', 'about', 'participants']

    videos = VideoSerializer(many=True)
    images = ImageSerializer(many=True)
    participants = ParticipantOfProjectSerializer(many=True)
