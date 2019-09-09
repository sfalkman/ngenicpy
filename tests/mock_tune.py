from .mock_base import MockBase
from ngenicpy.models import Tune

test_json = """
{
    "isInstalled": true,
    "isNetworkConnected": true,
    "name": "Johanna Johansson",
    "priceArea": 3,
    "tuneName": "Villa Rosebud",
    "tuneUuid": "f453152b-98d9-e611-80c3-0123456789ab",
    "userName": "johanna.johansson@example.domain"
}
"""
class MockTune(MockBase):
    def __init__(self):
        super(MockTune, self).__init__(Tune, test_json)
