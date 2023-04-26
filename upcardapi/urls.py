from django.contrib import admin
from django.urls import path, include
from upcardapi import settings
from django.conf.urls.static import static

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    
    #auth
    path('auth/', include('authorization.urls')),
    
    path('', include('landing.urls')),
    
    # api
    path('api/v1/', include('api.urls')),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # static