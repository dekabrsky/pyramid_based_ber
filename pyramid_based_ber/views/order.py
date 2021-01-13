from pyramid.view import view_config
from pyramid_based_ber.infrastructure.order_info_parser.info_parser import parse_order_info
from pyramid_based_ber.infrastructure.order_manager.order_manager import register_order
from pyramid_based_ber.infrastructure.validation.info_validator import validate


@view_config(route_name='order')
def make_order(request):
    order_info = parse_order_info(request.params)
    if validate(order_info):
        register_order(order_info)
        return
    else:
        return {'': 'Incorrect data'}
