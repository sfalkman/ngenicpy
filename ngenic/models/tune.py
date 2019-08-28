import json
from .base import NgenicBase
from .room import Room
from ..const import API_PATH

class Tune(NgenicBase):
    def __init__(self, token, json):
        super(Tune, self).__init__(token, json)

    def uuid(self):
        """Get the tune UUID"""
        
        # If a tune was fetched with the list API, it contains "tuneUuid"
        # If it was fetched directly (with UUID), it contains "uuid"
        try:
            return self["tuneUuid"]
        except AttributeError:
            return self["uuid"]

    def rooms(self):
        """List all Rooms associated with a Tune. A Room contains an indoor sensor.

        :return:
            a list of rooms
        :rtype:
            `list(~ngenic.models.room.Room)`
        """
        url = API_PATH["rooms"].format(tuneUuid=self.uuid(), roomUuid="")
        return self._parse_new_instance(url, Room, tune=self)

    def room(self, roomUuid):
        """Get data about a Room. A Room contains an indoor sensor.

        :param str roomUuid:
            (required) room UUID
        :return:
            the room
        :rtype:
            `~ngenic.models.room.Room`
        """
        url = API_PATH["rooms"].format(tuneUuid=self.uuid(), roomUuid=roomUuid)
        return self._parse_new_instance(url, Room, tune=self)
