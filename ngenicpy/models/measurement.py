import json
from enum import Enum
from .base import NgenicBase
from ..const import API_PATH

# Undocumented in API
class MeasurementType(Enum):
    TEMPERATURE = "temperature_C"
    TARGET_TEMPERATURE = "target_temperature_C"
    HUMIDITY = "humidity_relative_percent"
    CONTROL_VALUE = "control_value_C"
    POWER_KW = "power_kW"
    ENERGY_KWH = "energi_kWH"

class Measurement(NgenicBase):
    def __init__(self, session, json, node, measurement_type):
        self._parentNode = node
        self._measurementType = measurement_type

        super(Measurement, self).__init__(session=session, json=json)

    def get_type(self):
        """Get the measurement type

        :return:
            measurement type
        :rtype:
            `~ngenic.models.measurement.MeasurementType`
        """
        return self._measurementType
