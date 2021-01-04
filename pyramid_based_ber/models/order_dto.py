class OrderDto(object):
    def __init__(self, name, phone_number, address, burger_config):
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.burger_config = burger_config
