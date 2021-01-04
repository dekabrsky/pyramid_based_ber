from pyramid_based_ber.models.burger import Burger
from pyramid_based_ber.models.order_dto import OrderDto


def parse_order_info(params) -> OrderDto:
    burger = parse_burger_info(params)
    return OrderDto(remove_unnecessary_whitespaces(params['name']),
                    remove_unnecessary_whitespaces(params['phone_number']),
                    remove_unnecessary_whitespaces(params['address']), burger)


def parse_burger_info(params) -> Burger:
    return None


def remove_unnecessary_whitespaces(string: str) -> str:
    result = string
    for char in string:
        if char.isspace():
            result = result.replace(char, '', 1)
        else:
            return result
