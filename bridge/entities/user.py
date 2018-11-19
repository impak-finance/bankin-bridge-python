"""
    Bankin Bridge user entity
    =========================

    This module defines the ``User`` entity allowing to interact with the underlying API methods.
    Documentation: https://docs.bridgeapi.io/reference/

"""

from ..baseapi import BaseApi


class User(BaseApi):
    """ Wraps the user-related API methods. """

    def create(self, email, password):
        """ Creates a new user object.

        :param email: user's email address
        :param password: user's password
        :type email: str
        :type password: password
        :return: dictionary containing the result of the creation operation
        :rtype: dictionary

        """
        return self._client._call(
            'POST', 'users', params={'email': email, 'password': password, },
        )

    def authenticate(self, email, password, set_access_token=False):
        """ Authenticates a user.

        :param email: user's email address
        :param password: user's password
        :param set_access_token: whether to set the obtained access token on the client object
        :type email: str
        :type password: password
        :type set_access_token: bool
        :return: dictionary containing the result of the authentication operation
        :rtype: dictionary

        """
        data = self._client._call(
            'POST', 'authenticate', params={'email': email, 'password': password, },
        )
        if set_access_token:
            self._client.set_access_token(data['access_token'])
        return data
