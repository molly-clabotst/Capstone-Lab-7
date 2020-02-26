import unittest 
from unittest import TestCase
from unittest.mock import patch 

import bitcoin

class TestBitcoin(TestCase):

    @patch('builtins.input', side_effect=['stuff', '123moreStuff', '5.00'])
    def test_range_of_input_types(self, mock_input):
        bitcoinNumber = bitcoin.userInput()
        self.assertEqual(5.00, bitcoinNumber)

    @patch('bitcoin.getData')
    def test_conversion_based_off_api(self, mock_rates):
        mock_rate = 121212.00
        example_api_response = {'time': {'updated': 'Feb 26, 2020 22:12:00 UTC', 'updatedISO': '2020-02-26T22:12:00+00:00', 'updateduk': 'Feb 26, 2020 at 22:12 GMT'}, 'disclaimer': 'This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org', 'chartName': 'Bitcoin', 'bpi': {'USD': {'code': 'USD', 'symbol': '&#36;', 'rate': '8,788.4483', 'description': 'United States Dollar', 'rate_float': mock_rate}, 'GBP': {'code': 'GBP', 'symbol': '&pound;', 'rate': '6,812.1548', 'description': 'British Pound Sterling', 'rate_float': 6812.1548}, 'EUR': {'code': 'EUR', 'symbol': '&euro;', 'rate': '8,077.0586', 'description': 'Euro', 'rate_float': 8077.0586}}}
        mock_rates.side_effect = [example_api_response]
        converted = bitcoin.convert(100)
        self.assertEqual(12121200.00, converted)
