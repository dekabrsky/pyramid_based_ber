from pyramid.view import view_config


@view_config(route_name='home', renderer='../templates/main.jinja2')
def my_view(request):
    return {'project': 'pyramid_based_ber'}
