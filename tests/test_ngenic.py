from unittest import mock, TestCase

from const import *
from mock_room import MockRoom
from mock_tune import MockTune
from ngenicpy.models.room import Room
from ngenicpy.models.tune import Tune
from ngenicpy.ngenic import Ngenic


class TestNgenic(TestCase):
    def setUp(self):
        """Setup runs before all test cases."""
        self.ngenic = Ngenic(token="dummy")

    @mock.patch("requests.get", side_effect=MockTune().mock_response)
    def test_tunes_get(self, mock_response):
        ngenic = Ngenic(token=API_TEST_TOKEN)
        tune = ngenic.tune(TUNE_UUID)

        self.assertIsInstance(tune, Tune)
        self.assertEqual(tune["name"], "Johanna Johansson")

    @mock.patch("requests.get", side_effect=MockTune().mock_list_response)
    def test_tunes_get_all(self, mock_list_response):
        ngenic = Ngenic(token=API_TEST_TOKEN)
        tunes = ngenic.tunes()

        self.assertIsInstance(tunes, list)
        self.assertTrue(all(isinstance(x, Tune) for x in tunes))

    @mock.patch("requests.get", side_effect=MockRoom().mock_response)
    def test_rooms_get(self, mock_response):
        tune = MockTune().single_instance()
        room = tune.room(ROOM_UUID)

        self.assertIsInstance(room, Room)
        self.assertEqual(room["name"], "Main hallway")

    @mock.patch("requests.get", side_effect=MockRoom().mock_list_response)
    def test_tunes_get_all(self, mock_list_response):
        tune = MockTune().single_instance()
        rooms = tune.rooms()

        self.assertIsInstance(rooms, list)
        self.assertTrue(all(isinstance(x, Room) for x in rooms))

    @mock.patch("requests.put", side_effect=MockRoom().mock_response)
    def test_rooms_update(self, mock_response):
        tune = MockTune().single_instance()
        room = MockRoom().single_instance(tune=tune)
        room["name"] = "Hallway"
        room.update()

        self.assertIsInstance(room, Room)
        self.assertEqual(room["name"], "Hallway")

    def tearDown(self):
        """Tear down test objects"""
        self.ngenic = None
