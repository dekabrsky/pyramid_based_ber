from pyramid_based_ber.models.burger import Burger
from pyramid_based_ber.models.order_dto import OrderDto


class InfoParser(object):
    @staticmethod
    def parse(params) -> OrderDto:
        burger = parse_burger_info(params)
        return OrderDto(params['name'], params['phone_number'], params['address'], burger)


def parse_burger_info(params) -> Burger:
    return None
