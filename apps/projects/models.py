from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Profession(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Participant(models.Model):
    name = models.CharField(max_length=250)
    image = models.FileField(upload_to='participants')
    profession = models.ForeignKey(Profession, models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def get_image(self):
        return f"{settings.SITE_URL}{self.image.url}"


class Project(models.Model):
    category = models.ForeignKey(Category, models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=250)
    about = models.TextField()

    def __str__(self):
        return self.name


class ParticipantOfProject(models.Model):
    project = models.ForeignKey(Project, models.CASCADE, related_name='participants')
    participant = models.ForeignKey(Participant, models.CASCADE, related_name='participants')


class Image(models.Model):
    project = models.ForeignKey(Project, models.CASCADE, related_name='images')
    image = models.FileField(upload_to='projects')

    def __str__(self):
        return self.project.name

    @property
    def get_image(self):
        return f"{settings.SITE_URL}{self.image.url}"


class Video(models.Model):
    project = models.ForeignKey(Project, models.CASCADE, related_name='videos')
    video = models.FileField(upload_to='projects')

    def __str__(self):
        return self.project.name

    @property
    def get_video(self):
        return f"{settings.SITE_URL}{self.video.url}"
