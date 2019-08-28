import json
from .base import NgenicBase
from ..const import API_PATH

class Room(NgenicBase):
    def __init__(self, token, json, tune):
        self._parentTune = tune

        super(Room, self).__init__(token, json)

    def update(self):
        """Update this room with its current values"""
        roomUuid = self["uuid"]

        url = API_PATH["rooms"].format(tuneUuid=self._parentTune.uuid(), roomUuid=roomUuid)
        self._put(url, data=self.json())
