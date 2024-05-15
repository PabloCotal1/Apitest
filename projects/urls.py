from django.urls import path
from rest_framework import routers
from .api import ProjectViewSet
from .views import project_list, project_create, project_detail, project_update, project_delete

# Definimos el enrutador de DRF
router = routers.DefaultRouter()
router.register('api/projects', ProjectViewSet, 'projects')

# Definimos las URL
urlpatterns = [
    # Rutas de las vistas basadas en funciones
    path('', project_list, name='project_list'),
    path('create/', project_create, name='project_create'),
    path('<int:pk>/', project_detail, name='project_detail'),
    path('<int:pk>/update/', project_update, name='project_update'),
    path('<int:pk>/delete/', project_delete, name='project_delete'),

    # Agregamos las URL generadas por el enrutador de DRF
    *router.urls,
]
