

class View(object):
    provider_class = None
    provider = None

    def __init__(self, request):
        self.request = request
        self.response = request.response
        self.context = request.context

        dbsession = request.dbsession
        settings = request.registry.settings

        if self.provider_class:
            self.provider = self.provider_class(dbsession, settings)
