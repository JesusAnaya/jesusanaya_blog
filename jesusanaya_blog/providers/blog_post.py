from jesusanaya_blog.services.storage import StorageService
from .base import Provider


class BlogPostProvider(Provider):

    def __init__(self, dbsession, settings):
        super(BlogPostProvider, self).__init__(dbsession, settings)
        self.storage = StorageService(settings)

    def create(self, post_data):
        pass
