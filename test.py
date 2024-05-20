# Иван Воробьёв, 16-я когорта - Финальный проект. Инженер по тестированию плюс.
import sender_request
import data

def get_track_number(order_body):
    track_number = sender_request.create_order(order_body).json()['track']
    return track_number


def test_get_order_information_by_track():
    new_track_number = get_track_number(data.order_body)
    assert sender_request.get_order_information_by_track_number(new_track_number).status_code == 200
