from django.conf import settings
from django.core.files.storage import FileSystemStorage


class PrivateMediaStorage(FileSystemStorage):
    """Simplification of the FileSystemStorage with the given private media root and url."""

    def __init__(self, location=None, base_url=None):
        if location is None:
            location = settings.PRIVATE_MEDIA_ROOT
        if base_url is None:
            base_url = settings.PRIVATE_MEDIA_URL
        return super(PrivateMediaStorage, self).__init__(location, base_url)
