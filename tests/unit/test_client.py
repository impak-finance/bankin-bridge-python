import unittest.mock

import pytest
from requests.exceptions import HTTPError

from bridge import Client
from bridge.exceptions import ProtocolError, TransportError


class TestClient:
    @unittest.mock.patch('requests.Session.get')
    def test_raises_a_transport_error_if_an_unsuccessful_is_sent_back_from_the_service(
        self, mocked_post,
    ):
        mocked_response = unittest.mock.Mock(status_code=500, content='ERROR')
        mocked_response.raise_for_status.side_effect = HTTPError(response=mocked_response)
        mocked_post.return_value = mocked_response
        client = Client('id-123456789', 'secret-123456789')
        with pytest.raises(TransportError):
            client.item.list()

    @unittest.mock.patch('requests.Session.get')
    def test_raises_a_protocol_error_if_a_response_cannot_be_deserialized(self, mocked_post):
        mocked_response = unittest.mock.Mock(status_code=200, content='BAD')
        mocked_response.json.side_effect = ValueError()
        mocked_post.return_value = mocked_response
        client = Client('id-123456789', 'secret-123456789')
        with pytest.raises(ProtocolError):
            client.item.list()

    @unittest.mock.patch('requests.Session.post')
    def test_raises_a_protocol_error_if_an_error_is_present_in_the_response(self, mocked_post):
        mocked_response = unittest.mock.Mock(status_code=400, content='{}')
        mocked_response.json.return_value = {'type': 'bad'}
        mocked_post.return_value = mocked_response
        client = Client('id-123456789', 'secret-123456789')
        with pytest.raises(ProtocolError):
            client.user.authenticate('test@example.com', 'pwd123456')

    def test_can_set_authentication_with_an_access_token(self):
        client = Client('id-123456789', 'secret-123456789')
        client.set_access_token('accesstoken-123456789')
        assert client.auth
        r = unittest.mock.MagicMock()
        r.headers = {}
        client.auth(r)
        assert r.headers['Authorization'] == 'Bearer accesstoken-123456789'

    def test_can_remove_configured_authentication(self):
        client = Client('id-123456789', 'secret-123456789')
        client.set_access_token('accesstoken-123456789')
        client.remove_auth()
        assert not client.auth
