from django.urls import path,include
from .views import ProjectViewSet, TaskViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='projects')
router.register(r'tasks', TaskViewSet, basename='Task')

urlpatterns = [
]

urlpatterns += router.urls