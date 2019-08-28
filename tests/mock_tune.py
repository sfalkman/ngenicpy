from .mock_base import MockBase
import json

tune_json = """
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
        super(MockTune, self).__init__()

    def mock_get_all(*args, **kwargs):
        return MockBase.MockGetResponse(json.loads("[%s,%s]" % (tune_json, tune_json)), 200)

    def mock_get(*args, **kwargs):
        return MockBase.MockGetResponse(json.loads("%s" % tune_json), 200)