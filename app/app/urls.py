from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('autenticacion/', include('autenticacion.urls')),
                  path('', include('products.urls')),
                  path('cart/', include('cart.urls')),
                  path('orders/', include('orders.urls')),
                  path('oauth/', include('social_django.urls', namespace='social')),
                  path('', include('pwa.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Administración de Zafiro"
admin.site.index_title = "Modulos de administración"
admin.site.site_title = "Zafiro"