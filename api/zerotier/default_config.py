import json
import random

randomIp: str = str(random.randint(0, 255)) + "." + str(random.randint(0, 255)) + "." + str(
    random.randint(0, 255))


class ZtNetwork:
    def __init__(self):
        self.name = self.new_name
        self.private = True
        self.enableBroadcast = True
        self.v4AssignMode = self.v4assignmode
        self.v6AssignMode = self.v6assignmode
        self.mtu = 2800
        self.multicastLimit = 32
        self.routes = [self.new_route]
        self.ipAssignmentPools = [self.new_ip_pool]
        self.rules = self.default_rules
        self.capabilities = []
        self.tags = []
        self.remoteTraceTarget = ""
        self.remoteTraceLevel = 0

    def __str__(self):
        return json.dumps(self.__dict__, ensure_ascii=False)

    def __repr__(self):
        return self.__str__()

    @property
    def new_name(self):
        return "Net" + "_" + str(random.randint(100000, 999999))

    @property
    def v4assignmode(self):
        return {"zt": True}

    @property
    def v6assignmode(self):
        return {"6plane": False, "rfc4193": False, "zt": False}

    @property
    def default_rules(self):
        ether_types = [2048, 2054, 34525]
        rules = [{"type": "MATCH_ETHERTYPE", "not": "true", "or": "false", "etherType": et} for et in ether_types]
        rules += [{"type": "ACTION_DROP"}, {"type": "ACTION_ACCEPT"}]
        return rules

    @property
    def new_ip_pool(self):
        return {"ipRangeStart": randomIp + ".1", "ipRangeEnd": randomIp + ".254"}

    @property
    def new_route(self):
        return {"target": randomIp + ".0/24", "via": None, "flags": 0, "metric": 0}


if __name__ == '__main__':
    print(ZtNetwork().__dict__)
