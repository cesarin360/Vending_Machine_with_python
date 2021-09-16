from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('maquina-expendedora/', permanent=False)),
    path('admin/', admin.site.urls),
    path('maquina-expendedora/', include('store.urls')),
    path('carro/', include('carro.urls'))
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)