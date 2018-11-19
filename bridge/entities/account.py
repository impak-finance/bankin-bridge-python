"""
    Bankin Bridge account entity
    ============================

    This module defines the ``Item`` entity allowing to interact with the underlying API methods.
    Documentation: https://docs.bridgeapi.io/reference/

"""

from ..baseapi import BaseApi


class Account(BaseApi):
    """ Wraps the account-related API methods. """

    def get(self, id):
        """ Retrieves the details of a single account.

        :param id: ID of the considered bank account
        :type id: str or int
        :return: dictionary containing the bank account details
        :rtype: dictionary

        """
        return self._client._call('GET', 'accounts/{}'.format(id))

    def list(self, before=None, after=None, limit=None):
        """ Lists the bank accounts associated with the considered user.

        :param before: cursor pointing to the end of the desired set
        :param after: cursor pointing to the start of the desired set
        :param limit: number of records to return (accepted values: 1 - 500)
        :type before: str
        :type after: str
        :type limit: int
        :return: dictionary containing the bank accounts
        :rtype: dictionary

        """
        params = {'before': before, 'after': after, 'limit': limit, }
        return self._patch_paginated_response_data(self._client._call(
            'GET', 'accounts', params={k: v for k, v in params.items() if v is not None},
        ))
