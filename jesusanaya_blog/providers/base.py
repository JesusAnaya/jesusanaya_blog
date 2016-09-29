

class Provider(object):
    def __init__(self, request, dbsession):
        self.request = request
        self.dbsession = dbsession
