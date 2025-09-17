# Дарья Матушкина, 34-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request as api
import data   

def test_track_order():
    
    create_resp = api.post_new_order(data.order_body)


    create_json = create_resp.json()
    track = create_json["track"]

   
    track_resp = api.get_track_order(track)
    assert track_resp.status_code == 200