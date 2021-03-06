from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import jobs.views

urlpatterns = [
    path('managemywebsiteplease/', admin.site.urls),
    path('', jobs.views.home, name='home'),
    path('cinema/', include('blog.urls')),
    path('game/', include('game.urls')),
    path('words/', include('wordCount.urls'))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
