"""
    Bankin Bridge bank entity
    =========================

    This module defines the ``Bank`` entity allowing to interact with the underlying API methods.
    Documentation: https://docs.bridgeapi.io/reference/

"""

from ..baseapi import BaseApi


class Bank(BaseApi):
    """ Wraps the bank-related API methods. """

    def get(self, id):
        """ Retrieves the details of a single bank.

        :param id: ID of the considered bank
        :type id: str or int
        :return: dictionary containing the bank details
        :rtype: dictionary

        """
        return self._client._call('GET', 'banks/{}'.format(id))

    def list(self, before=None, after=None, limit=None):
        """ List the available banks.

        :param before: cursor pointing to the end of the desired set
        :param after: cursor pointing to the start of the desired set
        :param limit: number of records to return (accepted values: 1 - 500)
        :type before: str
        :type after: str
        :type limit: int
        :return: dictionary containing the banks
        :rtype: dictionary

        """
        params = {'before': before, 'after': after, 'limit': limit, }
        return self._patch_paginated_response_data(self._client._call(
            'GET', 'banks', params={k: v for k, v in params.items() if v is not None},
        ))
