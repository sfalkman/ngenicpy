import json
from enum import Enum
from .base import NgenicBase
from .measurement import Measurement
from .node_status import NodeStatus
from ..const import API_PATH
from ..exceptions import ClientException

class NodeType(Enum):
    SENSOR = 0
    CONTROLLER = 1
    GATEWAY = 2
    INTERNAL = 3

class Node(NgenicBase):
    def __init__(self, token, json, tune):
        self._parentTune = tune

        super(Node, self).__init__(token, json)

    def getType(self):
        return NodeType(self["type"])

    def _get_measurement_types(self):
        """Get types of available measurements for this node."""
        url = API_PATH["measurements_types"].format(tuneUuid=self._parentTune.uuid(), nodeUuid=self.uuid())
        return self._parse(self._get(url))

    def latest_measurements(self):
        """Get latest measurements for a Node.
        Usually, you can get measurements from a `NodeType.SENSOR` or `NodeType.CONTROLLER`.

        :return:
            a list of measurements (if supported by the node)
        :rtype:
            `list(~ngenic.models.measurement.Measurement)`
        """
        # get available measurement types for this node
        measurement_types = self._get_measurement_types()

        # retrieve measurement for each type
        return list(self.latest_measurement(t) for t in measurement_types)

    def latest_measurement(self, measurement_type):
        """Get latest measurement for a Node.

        :param str measurement_type:
            (required) type of measurement
        :return:
            the node
        :rtype:
            `~ngenic.models.measurement.Measurement`
        """
        url = API_PATH["measurements_latest"].format(tuneUuid=self._parentTune.uuid(), nodeUuid=self.uuid())
        url += "?type=%s" % measurement_type
        return self._parse_new_instance(url, Measurement, node=self, measurement_type=measurement_type)

    def status(self):
        """Get status about this Node
        There are no API for getting the status for a single node, so we
        will use the list API and find our node in there.

        :return:
            a status object or None if Node doesn't support status
        :rtype:
            `~ngenic.models.node_status.NodeStatus`
        """
        url = API_PATH["node_status"].format(tuneUuid=self._parentTune.uuid())
        rsp_json = self._parse(self._get(url))

        for status_obj in rsp_json:
            if status_obj["nodeUuid"] == self.uuid():
                return self._new_instance(NodeStatus, status_obj, node=self)
        return None
