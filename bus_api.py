import json
import requests
import utils

class BusAPI:
    def __init__(self, service_key, station_data):
        self.serviceKey = service_key
        self.station_data = station_data
        self.arvl_bus_data = None
        
    def get_arvl_bus_data(self):
        url = 'http://apis.data.go.kr/6410000/busarrivalservice/getBusArrivalList'
        params = {
            'serviceKey': self.serviceKey,
            'stationId': self.station_data['result']['stationId']
        }
        
        result = utils.request_get_http(url, params, ['response', 'msgBody', 'busArrivalList'])
        if type(result['result']) != list:
            result['result'] = [] if result['result'] == None else [result['result']]
        
        self.arvl_bus_data = result
        return result
    
    def get_arvl_bus_info_data(self, _route_id):
        url = 'http://apis.data.go.kr/6410000/busrouteservice/getBusRouteInfoItem'
        params = {
            'serviceKey': self.serviceKey,
            'routeId': _route_id
        }
        
        result = utils.request_get_http(url, params, ['response', 'msgBody', 'busRouteInfoItem'])
        return result
    
    def get_arvl_bus_route_info_data(self, _route_id):
        url = 'http://apis.data.go.kr/6410000/busrouteservice/getBusRouteStationList'
        params = {
            'serviceKey': self.serviceKey,
            'routeId': _route_id
        }
        
        result = utils.request_get_http(url, params, ['response', 'msgBody', 'busRouteStationList'])
        return result
    
    def update_arvl_bus_data(self):
        self.get_arvl_bus_data()
        
        if (self.arvl_bus_data['resCode'] in ['0', '00']) == False:
            return False
        
        arvl_bus_list = self.arvl_bus_data['result']
        if type(arvl_bus_list) != list:
            arvl_bus_list = [arvl_bus_list]
            
        for index, arvl_bus in enumerate(arvl_bus_list):
            route_id = arvl_bus['routeId']
            arvl_bus_info = self.get_arvl_bus_info_data(route_id)
            arvl_bus_route_info = self.get_arvl_bus_route_info_data(route_id)
            
            self.arvl_bus_data['result'][index].update({
                'busInfo': arvl_bus_info['result'],
                'busRouteInfo': arvl_bus_route_info['result']
            })