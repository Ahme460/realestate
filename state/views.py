from django.shortcuts import render

from rest_framework.generics import ListAPIView
from .models import Project
from .serializers import ProjectSerializer
from .pagination import ProjectPagination

class ProjectListView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = ProjectPagination