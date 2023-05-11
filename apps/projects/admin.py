from django.contrib import admin
from .models import Profession, Category, Project, Participant, Video, Image, ParticipantOfProject
from .translations import CustomTranslationsAdmin


@admin.register(Category)
class Admin(CustomTranslationsAdmin):
    list_display = ['id', 'name']


@admin.register(Profession)
class Admin(CustomTranslationsAdmin):
    list_display = ['id', 'name']


class VideoInline(admin.TabularInline):
    model = Video
    extra = 0


class ImageInline(admin.TabularInline):
    model = Image
    extra = 0


class ParticipantOfProjectInline(admin.TabularInline):
    model = ParticipantOfProject
    extra = 0


@admin.register(Participant)
class Admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'profession']


@admin.register(Project)
class Admin(CustomTranslationsAdmin):
    list_display = ['id', 'name', 'category']
    inlines = [VideoInline, ImageInline, ParticipantOfProjectInline]
