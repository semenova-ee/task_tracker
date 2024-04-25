
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('members.urls')),
    path('api/', include('tasks.urls')),
    path('auth/', include('djoser.urls')),
    path('api-auth/', include('rest_framework.urls')),
]