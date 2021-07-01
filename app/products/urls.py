from django.urls import path, include 
from .views import listado_productos, read, agregar, eliminar, ProductoViewset,CategoryViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('producto', ProductoViewset)
router.register('categoria',CategoryViewset)

urlpatterns = [
    path('', listado_productos, name='listado_productos'),
    path('products/read/', read, name='read'),
    path('products/agregar/', agregar, name='agregar'),
    path('products/eliminar/<id>/', eliminar, name='eliminar'),
    path('api/', include(router.urls)),
]
