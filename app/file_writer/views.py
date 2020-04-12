from django.http import HttpResponseBadRequest, HttpResponse
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny


class FileWriterView(APIView):
    authentication_classes = [AllowAny, ]

    def post(self):
        text = self.kwargs.get('q')

        if text:
            return HttpResponse(b'Text successfully written')
        else:
            return HttpResponseBadRequest(b'Text to write to file is required.')
