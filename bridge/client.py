"""
    Bankin Bridge client
    ====================

    This module defines the ``Client`` class allowing to interact with the Bankin Bridge API
    endpoints and methods.
    Documentation: https://docs.bridgeapi.io/

"""

from urllib.parse import urljoin

import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import HTTPError

from .exceptions import ProtocolError, TransportError


class Client:
    """ The Bankin Bridge API client class. """

    def __init__(
        self, client_id, client_secret, access_token=None, base_url=None, http_max_retries=None,
    ):
        """ Initializes the Bankin Bridge client.

        :param client_id: application's client id
        :param client_secret: application's client secret
        :param base_url: base URL of the API endpont (eg. "https://sync.bankin.com/v2/")
        :param http_max_retries: maximum number of retries each connection should attempt
        :type client_id: str
        :type client_secret: str
        :type base_url: str
        :type http_max_retries: int
        :return: :class:`Client <Client>` object
        :rtype: bridge.client.Client

        """
        # Initializes attributes related to the client settings.
        self.client_id = client_id
        self.client_secret = client_secret
        self.api_endpoint = base_url or 'https://sync.bankin.com/v2/'
        self.api_version = '2018-06-15'
        self.session = requests.Session()
        self.session.mount(self.api_endpoint, HTTPAdapter(max_retries=http_max_retries or 3))

        # Initializes auth-related classes.
        self.auth = None
        if access_token:
            self.set_access_token(access_token)

        # Set up entities attributes.
        self._account = None
        self._bank = None
        self._item = None
        self._transaction = None
        self._user = None

    def set_access_token(self, access_token):
        """ Sets up authentication to use a specific access token. """
        self.auth = BankinBridgeOAuth(access_token)

    ##########################
    # BANKIN BRIDGE ENTITIES #
    ##########################

    @property
    def account(self):
        """ Allows to access the account entity.

        :return: :class:`Account <Account>` object
        :rtype: bridge.entities.account.Account

        """
        if self._account is None:
            from .entities.account import Account
            self._account = Account(self)
        return self._account

    @property
    def bank(self):
        """ Allows to access the bank entity.

        :return: :class:`Bank <Bank>` object
        :rtype: bridge.entities.bank.Bank

        """
        if self._bank is None:
            from .entities.bank import Bank
            self._bank = Bank(self)
        return self._bank

    @property
    def item(self):
        """ Allows to access the item entity.

        :return: :class:`Item <Item>` object
        :rtype: bridge.entities.item.Item

        """
        if self._item is None:
            from .entities.item import Item
            self._item = Item(self)
        return self._item

    @property
    def transaction(self):
        """ Allows to access the transaction entity.

        :return: :class:`Transaction <Transaction>` object
        :rtype: bridge.entities.transaction.Transaction

        """
        if self._transaction is None:
            from .entities.transaction import Transaction
            self._transaction = Transaction(self)
        return self._transaction

    @property
    def user(self):
        """ Allows to access the user entity.

        :return: :class:`User <User>` object
        :rtype: bridge.entities.user.User

        """
        if self._user is None:
            from .entities.user import User
            self._user = User(self)
        return self._user

    ##################################
    # PRIVATE METHODS AND PROPERTIES #
    ##################################

    def _call(self, http_method, path, params=None, data=None):
        """ Calls the API endpoint. """
        # Prepares the headers and parameters that will be used to forge the request.
        headers = {'Bankin-Version': self.api_version, }
        params = params or {}
        params.update({'client_id': self.client_id, 'client_secret': self.client_secret, })

        # Calls the API endpoint!
        request = getattr(self.session, http_method.lower())

        try:
            response = request(
                urljoin(self.api_endpoint, path).strip('/'),
                headers=headers, params=params, json=data, auth=self.auth,
            )
            response.raise_for_status()
        except HTTPError:
            if response.status_code != 400:
                raise TransportError(
                    'Got unsuccessful response from server (status code: {})'.format(
                        response.status_code,
                    ),
                    response=response,
                )

        # Ensures the response body can be deserialized to JSON.
        try:
            response_data = response.json()
        except ValueError as e:
            raise ProtocolError(
                'Unable to deserialize response body: {}'.format(e), response=response,
            )

        # Properly handles potential errors.
        if response.status_code > 299 and response_data.get('type'):
            raise ProtocolError(
                response_data['type'],
                response=response,
                data=response_data,
            )

        return response_data


class BankinBridgeOAuth(requests.auth.AuthBase):
    """ Authentication class for authentication with Bankin Bridge OAuth2. """

    def __init__(self, access_token):
        self._access_token = access_token

    def __call__(self, r):
        """ Authorizes with the considered access token. """
        r.headers['Authorization'] = 'Bearer ' + self._access_token
        return r
