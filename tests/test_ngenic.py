from unittest import mock
import pytest

from ngenic import Ngenic
from ngenic.models import Tune

from .const import *
from .mock_tune import MockTune
from . import UnitTest

class TestNgenic(UnitTest):
    @mock.patch("requests.get", side_effect=MockTune().mock_get)
    def test_tunes_get(self, mock_get):
        ngenic = Ngenic(token=API_TEST_TOKEN)
        tune = ngenic.tune(TUNE_UUID)
        
        assert isinstance(tune, Tune)
        assert tune["name"] == "Johanna Johansson"

    @mock.patch("requests.get", side_effect=MockTune().mock_get_all)
    def test_tunes_get_all(self, mock_get):
        ngenic = Ngenic(token=API_TEST_TOKEN)
        tunes = ngenic.tunes()
        
        assert isinstance(tunes, list)
        assert all(isinstance(x, Tune) for x in tunes)

        assert isinstance(tunes[0], Tune)