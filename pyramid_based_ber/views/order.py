from pyramid.view import view_config
from pyramid_based_ber.infrastructure.order_info_parser.info_parser import InfoParser
from pyramid_based_ber.infrastructure.order_manager.order_manager import OrderManager


@view_config(route_name='order', renderer='../templates/layout.jinja2')
def make_order(request):
    order_info = InfoParser().parse(request.params)
    OrderManager.make_order(order_info)
    return {}
