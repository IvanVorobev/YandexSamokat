import requests
import configuration


def create_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=order_body)


def get_order_information_by_track_number(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_INFORMATION + str(track_number))
