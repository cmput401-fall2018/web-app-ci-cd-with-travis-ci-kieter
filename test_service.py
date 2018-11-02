import unittest
from service import Service
from unittest.mock import patch

class TestService(unittest.TestCase):

    @patch("test_service.Service.bad_random")
    def test_bad_random(self, mock_bad_random):
        mock_bad_random.return_value = 10
        assert Service.bad_random() == 10

    @patch("test_service.Service.bad_random")
    def test_divide(self, mock_bad_random):
        mock_bad_random.return_value = 10
        service = Service()
        assert service.divide(2) == 5

    def test_abs_plus(self):
        service = Service()
        assert service.abs_plus(-1) == 2

    @patch("test_service.Service.bad_random")
    def test_complicated_function(self, mock_bad_random):
        mock_bad_random.return_value = 10
        service = Service()
        assert service.complicated_function(2) == (5, 0)
        
TestService()