import httpx
import json

from api.zerotier.default_config import ZtNetwork


class ZeroTierApi:
    def __init__(self, url: str, node_id: str, token: str, network_id: str = None, number_id: str = None):
        self.node_id = node_id
        self.token = token
        self.networkId = network_id
        self.url = url
        self.number_id = number_id
        self.headers = {"ZT1-Auth": self.token}

    def get_node_info(self):
        path = self.url + "/status" + self.node_id
        response = httpx.get(path, headers=self.headers)
        return response.json()

    def create_network(self):
        path = self.url + "/controller/network" + self.node_id + "______"
        data = ZtNetwork().__dict__
        response = httpx.post(path, headers=self.headers, data=data)
        return response.json()

    def list_networks(self):
        path = self.url + "/controller/network"
        response = httpx.post(path, headers=self.headers)
        return response.json()

    def config_network(self, request: dict):
        path = self.url + "/controller/network" + self.networkId + "/config"
        data = request
        response = httpx.post(path, headers=self.headers, data=data)
        return response.json()

    def delete_network(self):
        path = self.url + "/controller/network" + self.networkId
        response = httpx.delete(path, headers=self.headers)
        return response.json()

    @property
    def list_network_members(self):
        path = self.url + "/controller/network" + self.networkId + "/member"
        response = httpx.get(path, headers=self.headers)
        return response.json()

    @property
    def get_number_info(self):
        path = self.url + "/controller/network" + self.networkId + "/member/" + self.number_id
        response = httpx.get(path, headers=self.headers)
        return response.json()

    def config_member(self, request: dict):
        path = self.url + "/controller/network" + self.networkId + "/member/" + self.number_id
        data = request
        response = httpx.post(path, headers=self.headers, data=data)
        return response.json()

    def delete_number(self):
        path = self.url + "/controller/network" + self.networkId + "/member/" + self.number_id
        response = httpx.delete(path, headers=self.headers)
        return response.json()
