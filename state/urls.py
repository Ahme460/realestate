
from django.urls import path
from .views import ProjectListView
urlpatterns = [

path('api/projects/', ProjectListView.as_view(), name='project-list'),

]
