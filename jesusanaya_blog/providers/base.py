

class Provider(object):
    def __init__(self, dbsession, settings):
        self.dbsession = dbsession
        self.settings = settings
