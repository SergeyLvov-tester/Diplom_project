# Сергей Львов, 17+ когорта — Финальный проект. Инженер по тестированию плюс

import send_request
import data

def test_get_order_info_by_track():
    track = send_request.create_order(data.order_body).json()['track']
    response = send_request.get_order_info_by_track(track)
    assert response.status_code == 200