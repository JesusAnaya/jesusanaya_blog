
def includeme(config):
    config.add_route('home', '/')
    config.include('.admin')
