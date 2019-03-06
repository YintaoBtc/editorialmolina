from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    
    # Paths del core
    path('', include('docker_django.apps.core.urls')),
    #Paths de books
    path("books/", include('docker_django.apps.books.urls')),
    
    # Paths de blog
    #path('blog/', include('docker_django.apps.blog.urls')),

    # Paths de pages
    path('page/', include('docker_django.apps.pages.urls')),

    # Paths de contact
    path('contact/', include('docker_django.apps.contact.urls')),

    # Paths del admin
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)