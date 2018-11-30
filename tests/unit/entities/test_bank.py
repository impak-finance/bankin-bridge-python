import unittest.mock

from bridge import Client


class TestBank:
    @unittest.mock.patch('requests.Session.get')
    def test_can_return_the_details_of_a_single_bank(self, mocked_get):
        mocked_response = unittest.mock.Mock(status_code=200, content='{}')
        mocked_response.json.return_value = {
            'id': '42',
        }
        mocked_get.return_value = mocked_response

        client = Client('id-123456789', 'secret-123456789', access_token='accesstoken-123456789')
        result = client.bank.get(42)

        assert result == {'id': '42'}
        assert mocked_get.call_args[0][0] == 'https://sync.bankin.com/v2/banks/42'

    @unittest.mock.patch('requests.Session.get')
    def test_can_return_lists_of_banks(self, mocked_get):
        mocked_response = unittest.mock.Mock(status_code=200, content='{}')
        mocked_response.json.return_value = {
            'results': [],
        }
        mocked_get.return_value = mocked_response

        client = Client('id-123456789', 'secret-123456789', access_token='accesstoken-123456789')
        result = client.bank.list()

        assert result == {'results': []}
        assert mocked_get.call_args[0][0] == 'https://sync.bankin.com/v2/banks'
