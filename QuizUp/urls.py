from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # for all-auth
    path('', include('quiz.urls')),
    path('authentication/', include('authentication.urls')),
]
