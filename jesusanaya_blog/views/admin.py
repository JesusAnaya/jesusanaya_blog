from pyramid.security import Allow, Everyone, Authenticated
from pyramid.httpexceptions import HTTPFound
from pyramid.security import remember, forget
from pyramid.view import view_config, view_defaults
from .base import View


def includeme(config):
    config.add_route('admin.login', '/admin/login/', factory=AdminLoginContext)
    config.add_route('admin.logout', '/admin/logout/', factory=AdminLoginContext)
    config.add_route('admin.home', '/admin/', factory=AdminContext)
    config.add_route('admin.page', '/admin/*pathpage', factory=AdminContext)


class AdminContext(object):
    __acl__ = [
        (Allow, Authenticated, 'view'),
        (Allow, Authenticated, 'create'),
        (Allow, Authenticated, 'edit'),
    ]

    def __init__(self, request):
        pass


class AdminLoginContext(object):
    __acl__ = [
        (Allow, Everyone, 'view'),
    ]

    def __init__(self, request):
        pass


class AdminView(View):
    pass


@view_defaults(route_name='admin.login')
class AdminLoginView(View):
    @view_config(renderer='admin/login.html', request_method='GET')
    def login_form(self):
        return {}

    @view_config(renderer='string', request_method='POST')
    def login_action(self):
        headers = forget(self.request)
        return HTTPFound(location=self.request.route_url('admin.login', headers=headers))

    @view_config(name='admin.logout', renderer='string')
    def logout_action(self):
        headers = forget(self.request)
        return HTTPFound(location=self.request.route_url('admin.login', headers=headers))
