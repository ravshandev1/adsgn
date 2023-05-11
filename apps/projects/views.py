from rest_framework import generics
from .serializers import ProjectDetailSerializer, ProjectSerializer, CategorySerializer
from .models import Category, Project


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProjectView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        qs = self.queryset.all()
        cat = self.request.query_params.get('category', None)
        if cat:
            qs = qs.filter(category__name__exact=cat)
        return qs


class ProjectDetailView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer
