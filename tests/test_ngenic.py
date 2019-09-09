from unittest import mock
import pytest

from ngenicpy import Ngenic
from ngenicpy.models import Tune
from ngenicpy.models import Room

from .const import *
from .mock_tune import MockTune
from .mock_room import MockRoom
from . import UnitTest

class TestNgenic(UnitTest):
    @mock.patch("requests.get", side_effect=MockTune().mock_response)
    def test_tunes_get(self, mock_response):
        ngenic = Ngenic(token=API_TEST_TOKEN)
        tune = ngenic.tune(TUNE_UUID)

        assert isinstance(tune, Tune)
        assert tune["name"] == "Johanna Johansson"

    @mock.patch("requests.get", side_effect=MockTune().mock_list_response)
    def test_tunes_get_all(self, mock_list_response):
        ngenic = Ngenic(token=API_TEST_TOKEN)
        tunes = ngenic.tunes()

        assert isinstance(tunes, list)
        assert all(isinstance(x, Tune) for x in tunes)

    @mock.patch("requests.get", side_effect=MockRoom().mock_response)
    def test_rooms_get(self, mock_response):
        tune = MockTune().single_instance()
        room = tune.room(ROOM_UUID)

        assert isinstance(room, Room)
        assert room["name"] == "Main hallway"

    @mock.patch("requests.get", side_effect=MockRoom().mock_list_response)
    def test_tunes_get_all(self, mock_list_response):
        tune = MockTune().single_instance()
        rooms = tune.rooms()

        assert isinstance(rooms, list)
        assert all(isinstance(x, Room) for x in rooms)

    @mock.patch("requests.put", side_effect=MockRoom().mock_response)
    def test_rooms_update(self, mock_response):
        tune = MockTune().single_instance()
        room = MockRoom().single_instance(tune=tune)
        room["name"] = "Hallway"
        room.update()

        assert isinstance(room, Room)
        assert room["name"] == "Hallway"
