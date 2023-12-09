import httpx
import json


class ZeroTierApi:
    def __init__(self, url: str, node_id: str, token: str, network_id: str=None, number_id: str=None,):
        self.node_id = node_id
        self.token = token
        self.networkId = network_id
        self.url = url + "/controller/network"
        self.number_id = number_id
        self.headers = {"ZT1-Auth": self.token}

    def create_network(self):
        path = self.url + self.node_id + "______"
        data = {}
        response = httpx.post(path, headers=self.headers, data=data)
        return response.json()

    def list_networks(self):
        path = self.url
        responese = httpx.post(path, headers=self.headers)
        return responese.json()

    def list_network_members(self):
        path = self.url + self.networkId + "/member"
        response = httpx.get(path, headers=self.headers)
        return response.json()

    def get_number_info(self):
        path = self.url + self.networkId + "/member/" + self.number_id
        response = httpx.get(path, headers=self.headers)
        return response.json()

    def config_network(self):
        path = self.url + self.networkId + "/config"
        data = {}
        response = httpx.post(path, headers=self.headers, data=data)
        return response.json()

    def auth_member(self):
        path = self.url + self.networkId + "/member/" + self.number_id
        data = {"authorized": True}
        response = httpx.post(path, headers=self.headers, data=data)
        return response.json()

