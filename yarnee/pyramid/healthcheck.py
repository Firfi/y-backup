from pyramid.view import view_config
from pyramid.response import Response

@view_config(route_name='healthcheck', request_method='GET')
def healthcheck(request):
    return Response('')

@view_config(route_name='loadtest', request_method='GET')
def loadtest(request):
    return Response('42')