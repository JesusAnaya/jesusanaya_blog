

class View(object):
    provider_class = None
    provider = None

    def __init__(self, request):
        self.request = request
        self.response = request.response
        self.context = request.context
        self.dbsession = request.dbsession
        self.settings = request.registry.settings

        if self.provider_class:
            self.provider = self.provider_class(request, self.dbsession)
