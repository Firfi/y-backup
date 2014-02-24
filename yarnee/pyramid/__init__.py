"""
Pyramid application for Yarnee
"""
from pyramid.config import Configurator
from sqlalchemy import engine_from_config



from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.renderers import JSON

from pyramid.events import ContextFound
from pyramid.events import NewResponse

from pyramid.view import notfound_view_config
from pyramid.view import view_config


import json

import pyramid.httpexceptions as exc
from pyramid.response import Response


routes = [

    # network
    ['healthcheck',                      '/healthcheck'],
    ['loadtest',                         '/mu-e9850d85-5a870b44-32975f4e-fa4234d0']

]


def response_schema(event):
    pass  # do not pass schema second time in response, do it in controllers

def main(global_config, **settings):
    """
    This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings)


    secret = 'azazayourmom'
    authentication_policy = AuthTktAuthenticationPolicy(secret=secret)
    authorization_policy = ACLAuthorizationPolicy()
    config = Configurator(authentication_policy=authentication_policy,
                          authorization_policy=authorization_policy,
                          settings=settings)
    config.include('pyramid_chameleon')

    config.add_renderer('indentedjson', DebugRendererFactory(
        indent=4, sort_keys=True, ensure_ascii=False)
    )
    #config.add_route('appindex', 'app/\!')

    config.add_static_view('app', 'app', cache_max_age=3600)

    for name, pattern in routes:
        config.add_route(name, pattern)


    config.scan()
    config.end()

    return config.make_wsgi_app()


@notfound_view_config(renderer='indentedjson')
def not_found(self, request):
    if request.matched_route:
        # do not override custom 404 exceptions statuses raised from views
        msg = 'not found'
    else:
        msg = 'api not defined'
        request.response.status = 501
    return {
        'message': msg
    }



@view_config(context=Exception, renderer='indentedjson')
def exception_handler(exc, request):
    msg = str(exc)
    request.response.status_int = 500
    return {
        'error': msg
    }


class DebugRendererFactory(JSON):

    def __init__(self, serializer=json.dumps, adapters=(), **kw):
        super(DebugRendererFactory, self).__init__(serializer, adapters, **kw)

    def __call__(self, info):

        _render = super(DebugRendererFactory, self).__call__(info)

        def __render(value, system):
            request = system.get('request')
            if request.params.get('debug') or request.headers.get('YarneeDebug'):
                if isinstance(value, dict):
                    if value.get('debug'):
                        if not isinstance(value['debug'], dict):
                            value['debug'] = {}
                    else:
                        value['debug'] = {}


            return _render(value, system)

        return __render


