from django.urls import path

from app.file_writer.views import FileWriterView

urlpatterns = [
    path('write/', FileWriterView)
]