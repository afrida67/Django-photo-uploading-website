
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from accounts import views as home_view

urlpatterns = [
    path('gallery/', include('gallery.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('',home_view.login_view, name="mainpage"),
]

urlpatterns += staticfiles_urlpatterns()
# IT MEANS whenever developer mode use media directory
if settings.DEBUG:
     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 