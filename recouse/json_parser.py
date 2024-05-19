import json
from AbstractFactory import AbstractFactory
from ConcreteFactory import ContinuousFactory, AtomicFactory

class ResourceParser:
    def __init__(self, factory: AbstractFactory):
        self.factory = factory

    def parse(self, json_content: str):
        data = json.loads(json_content)

        req_units = []
        prov_units = []

        for item in data.get("req_units", []):
            if item["type"] == "continuous":
                req_unit = self.factory.create_req_unit()
                req_units.append(req_unit)
            elif item["type"] == "atomic":
                req_unit = self.factory.create_req_unit()
                req_units.append(req_unit)

        for item in data.get("prov_units", []):
            if item["type"] == "continuous":
                prov_unit = self.factory.create_prov_unit()
                prov_units.append(prov_unit)
            elif item["type"] == "atomic":
                prov_unit = self.factory.create_prov_unit()
                prov_units.append(prov_unit)

        return req_units, prov_units