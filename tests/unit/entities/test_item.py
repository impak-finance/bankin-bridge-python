import unittest.mock

from bridge import Client


class TestItem:
    @unittest.mock.patch('requests.Session.get')
    def test_can_return_a_new_add_url(self, mocked_get):
        mocked_response = unittest.mock.Mock(status_code=200, content='{}')
        mocked_response.json.return_value = {
            'redirect_url': 'https://example.com',
        }
        mocked_get.return_value = mocked_response

        client = Client('id-123456789', 'secret-123456789', access_token='accesstoken-123456789')
        result = client.item.add_url()

        assert result == {'redirect_url': 'https://example.com'}
        assert mocked_get.call_args[0][0] == 'https://sync.bankin.com/v2/items/add/url'

    @unittest.mock.patch('requests.Session.delete')
    def test_can_delete_an_item(self, mocked_delete):
        mocked_response = unittest.mock.Mock(status_code=200, content='{}')
        mocked_response.json.return_value = {}
        mocked_delete.return_value = mocked_response

        client = Client('id-123456789', 'secret-123456789', access_token='accesstoken-123456789')
        result = client.item.delete(42)

        assert result == {}
        assert mocked_delete.call_args[0][0] == 'https://sync.bankin.com/v2/items/42'

    @unittest.mock.patch('requests.Session.get')
    def test_can_return_an_edit_url(self, mocked_get):
        mocked_response = unittest.mock.Mock(status_code=200, content='{}')
        mocked_response.json.return_value = {
            'redirect_url': 'https://example.com',
        }
        mocked_get.return_value = mocked_response

        client = Client('id-123456789', 'secret-123456789', access_token='accesstoken-123456789')
        result = client.item.edit_url(42)

        assert result == {'redirect_url': 'https://example.com'}
        assert mocked_get.call_args[0][0] == 'https://sync.bankin.com/v2/connect/items/edit/url'
        assert mocked_get.call_args[1]['params']['item_id'] == 42

    @unittest.mock.patch('requests.Session.get')
    def test_can_return_the_details_of_a_single_item(self, mocked_get):
        mocked_response = unittest.mock.Mock(status_code=200, content='{}')
        mocked_response.json.return_value = {
            'id': '42',
        }
        mocked_get.return_value = mocked_response

        client = Client('id-123456789', 'secret-123456789', access_token='accesstoken-123456789')
        result = client.item.get(42)

        assert result == {'id': '42'}
        assert mocked_get.call_args[0][0] == 'https://sync.bankin.com/v2/items/42'

    @unittest.mock.patch('requests.Session.get')
    def test_can_return_the_refresh_status_of_a_single_item(self, mocked_get):
        mocked_response = unittest.mock.Mock(status_code=200, content='{}')
        mocked_response.json.return_value = {
            'id': '42',
        }
        mocked_get.return_value = mocked_response

        client = Client('id-123456789', 'secret-123456789', access_token='accesstoken-123456789')
        result = client.item.get_refresh_status(42)

        assert result == {'id': '42'}
        assert mocked_get.call_args[0][0] == 'https://sync.bankin.com/v2/items/42/refresh/status'

    @unittest.mock.patch('requests.Session.get')
    def test_can_return_lists_of_items(self, mocked_get):
        mocked_response = unittest.mock.Mock(status_code=200, content='{}')
        mocked_response.json.return_value = {
            'results': [],
        }
        mocked_get.return_value = mocked_response

        client = Client('id-123456789', 'secret-123456789', access_token='accesstoken-123456789')
        result = client.item.list()

        assert result == {'results': []}
        assert mocked_get.call_args[0][0] == 'https://sync.bankin.com/v2/items'

    @unittest.mock.patch('requests.Session.post')
    def test_can_send_mfa(self, mocked_post):
        mocked_response = unittest.mock.Mock(status_code=200, content='{}')
        mocked_response.json.return_value = {}
        mocked_post.return_value = mocked_response

        client = Client('id-123456789', 'secret-123456789', access_token='accesstoken-123456789')
        result = client.item.send_mfa(42, 'otp')

        assert result == {}
        assert mocked_post.call_args[0][0] == 'https://sync.bankin.com/v2/items/42/mfa'

    @unittest.mock.patch('requests.Session.get')
    def test_can_return_a_url_to_validate_pro_items(self, mocked_get):
        mocked_response = unittest.mock.Mock(status_code=200, content='{}')
        mocked_response.json.return_value = {'redirect_url': 'https://example.com'}
        mocked_get.return_value = mocked_response

        client = Client('id-123456789', 'secret-123456789', access_token='accesstoken-123456789')
        result = client.item.validate_pro()

        assert result == {'redirect_url': 'https://example.com'}
        assert (
            mocked_get.call_args[0][0] ==
            'https://sync.bankin.com/v2/connect/items/pro/confirmation/url'
        )
