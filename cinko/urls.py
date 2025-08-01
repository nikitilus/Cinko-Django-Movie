
from django.contrib import admin
from django.urls import path, include
from main import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('accounts/', include('accounts.urls')),
    # path('sets/', include('sets.urls')),
    path('create/', include('sets.urls')),
]