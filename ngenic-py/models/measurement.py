import json
from .base import NgenicBase
from ..const import API_PATH

class Measurement(NgenicBase):
    def __init__(self, token, json, node, measurement_type):
        self._parentNode = node
        self._measurementType = measurement_type

        super(Measurement, self).__init__(token, json)

    def getType(self):
        """Get the measurement type"""
        return self._measurementType
