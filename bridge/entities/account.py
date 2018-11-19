"""
    Bankin Bridge account entity
    ============================

    This module defines the ``Item`` entity allowing to interact with the underlying API methods.
    Documentation: https://docs.bridgeapi.io/reference/

"""

from ..baseapi import BaseApi


class Account(BaseApi):
    """ Wraps the account-related API methods. """

    def list(self, access_token, before=None, after=None, limit=None):
        """ List the bank accounts associated with the considered user.

        :param access_token: a valid token identifying the considered app and user
        :param before: cursor pointing to the end of the desired set
        :param after: cursor pointing to the start of the desired set
        :param limit: number of records to return (accepted values: 1 - 500)
        :type access_token: str
        :type before: str
        :type after: str
        :type limit: int
        :return: dictionary containing the generated redirect URL
        :rtype: dictionary

        """
        params = {'before': before, 'after': after, 'limit': limit, }
        return self._client._call(
            'GET',
            'accounts',
            access_token=access_token,
            params={k: v for k, v in params.items() if v is not None},
        )
