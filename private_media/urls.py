from django.conf import settings
from django.conf.urls import url
from private_media.views import serve_private_file

app_name = 'private_media'
urlpatterns = [
    url(
        r'^{0}(?P<path>.*)$'.format(
            settings.PRIVATE_MEDIA_URL.lstrip('/')
        ),
        serve_private_file,
    ),
]
