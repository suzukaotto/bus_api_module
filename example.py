import json
import os
import bus_api as _bus_api

service_key = os.getenv('SERVICE_KEY')
station_data = {
    'result': {
        'centerYn': 'N',
        'districtCd': '2',
        'mobileNo': '29412',
        'regionName': '용인',
        'stationId': '228000446',
        'stationName': '중앙지구대',
        'x': '127.1988167',
        'y': '37.23475'
    }
}

bus_api = _bus_api.BusAPI(service_key, station_data)
bus_api.update_arvl_bus_data()

with open('arvl_bus_data.json', 'w', encoding='utf-8') as f:
    json.dump(bus_api.arvl_bus_data, f, ensure_ascii=False, indent=4)