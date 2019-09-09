"""This module contains the main interfaces to the API."""

from .models import NgenicBase
from .models import Tune
from .models import Room
from .const import API_PATH
from .const import API_URL
from .exceptions import ApiException, ClientException

import logging
import requests
import json

LOG = logging.getLogger(__package__)

class Ngenic(NgenicBase):
    def __init__(self, token):
        super(Ngenic, self).__init__(token, json)

    def tunes(self):
        """Fetch all tunes

        :return:
            a list of tunes
        :rtype:
            `list(~ngenic.models.tune.Tune)`
        """
        url = API_PATH["tunes"].format(tuneUuid="")
        return self._parse_new_instance(url, Tune)

    def tune(self, tuneUuid):
        """Fetch a single tune

        :param str tuneUUid:
            (required) tune UUID
        :return:
            the tune
        :rtype:
            `~ngenic.models.tune.Tune`
        """
        url = API_PATH["tunes"].format(tuneUuid=tuneUuid)
        return self._parse_new_instance(url, Tune)
