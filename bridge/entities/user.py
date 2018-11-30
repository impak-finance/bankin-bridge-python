"""
    Bankin Bridge user entity
    =========================

    This module defines the ``User`` entity allowing to interact with the underlying API methods.
    Documentation: https://docs.bridgeapi.io/reference/

"""

from ..baseapi import BaseApi


class User(BaseApi):
    """ Wraps the user-related API methods. """

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

    def check_email_validation(self):
        """ Checks whether the logged in user's email should be validated or not.

        :return: dictionary containing the result of the check operation
        :rtype: dictionary

        """
        return self._client._call('GET', 'users/me/email/confirmation')

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

    def delete(self, id, password):
        """ Removes all user objectts.

        :param id: ID of the user
        :param password: user's password
        :type id: str or int
        :type password: password
        :return: empty dictionary
        :rtype: dictionary

        """
        return self._client._call('DELETE', 'users/{}'.format(id), params={'password': password, })

    def delete_all(self):
        """ Removes all user objectts.

        :return: empty dictionary
        :rtype: dictionary

        """
        return self._client._call('DELETE', 'users')

    def logout(self):
        """ Logouts the authenticated user if applicable.

        :return: empty dictionary
        :rtype: dictionary

        """
        response = self._client._call('POST', 'logout')
        self._client.remove_auth()
        return response

    def update_credentials(self, id, current_password, new_password):
        """ Updates the authenticated user's credentials.

        :param id: ID of the user
        :param current_password: the current user's password
        :param new_password: the new user's password
        :type id: str or int
        :type current_password: str
        :type new_password: str
        :return: dictionary containing the result of the update operation
        :rtype: dictionary

        """
        response = self._client._call(
            'PUT',
            'users/{}/password'.format(id),
            {'current_password': current_password, 'new_password': new_password, },
        )
        self._client.remove_auth()
        return response

    def validate_email(self):
        """ Returns the URL to the Bridge's Connect funnel for validating user's email.

        :return: dictionary containing the funnel URL
        :rtype: dictionary

        """
        return self._client._call('GET', 'connect/users/email/confirmation/url')
