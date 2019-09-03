from .mock_base import MockBase
from ngenic.models import Room

test_json = """
{
    "uuid": "f8600246-1fdf-e611-80c3-123456789abc",
    "hasDefaultValues": false,
    "name": "Main hallway",
    "nodeUuid": "78668e1c-1fdf-e611-80c3-23456789abd",
    "targetTemperature": 21.5
}
"""
class MockRoom(MockBase):
    def __init__(self):
        super(MockRoom, self).__init__(Room, test_json)
