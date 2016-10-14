from pyramid.config import Configurator
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    # Auth system
    secret_key = settings.get('secret.key', 'secretkey')
    authentication_policy = AuthTktAuthenticationPolicy(secret_key, hashalg='sha512')
    authorization_policy = ACLAuthorizationPolicy()

    config = Configurator(settings=settings, authentication_policy=authentication_policy, authorization_policy=authorization_policy)
    config.set_default_permission('view')

    # Including packages
    config.include('pyramid_jinja2')
    config.include('.models')
    config.include('.views')

    # Configuring jinja2
    config.add_jinja2_search_path('jesusanaya_blog:templates/', name='.html')
    config.add_jinja2_renderer('.html', settings_prefix='jinja2.')

    config.add_static_view(name='static', path='jesusanaya_blog:static', cache_max_age=3600)
    config.add_request_method(request_static_method, 'static')

    config.scan()
    return config.make_wsgi_app()


def request_static_method(request, path):
    return request.static_url('jesusanaya_blog:static/{0}'.format(path))
