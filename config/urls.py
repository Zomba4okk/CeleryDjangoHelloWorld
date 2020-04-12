from django.contrib import admin
from django.urls import path, include


apipatterns = [
    path('file', include('app.file_writer.urls'))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include((apipatterns, 'api'), namespace='api'))
]
