"""
    Bankin Bridge stock entity
    =========================

    This module defines the ``Stock`` entity allowing to interact with the underlying API methods.
    Documentation: https://docs.bridgeapi.io/reference/

"""

from ..baseapi import BaseApi


class Stock(BaseApi):
    """ Wraps the stock-related API methods. """

    def get(self, id):
        """ Retrieves the details of a single stock.

        :param id: ID of the considered stock
        :type id: str or int
        :return: dictionary containing the stock details
        :rtype: dictionary

        """
        return self._client._call('GET', 'stocks/{}'.format(id))

    def list(self, before=None, after=None, limit=None):
        """ Returns a user's cursor-paginated list of stocks.

        :param before: cursor pointing to the end of the desired set
        :param after: cursor pointing to the start of the desired set
        :param limit: number of records to return (accepted values: 1 - 500)
        :type before: str
        :type after: str
        :type limit: int
        :return: dictionary containing the stocks
        :rtype: dictionary

        """
        params = {'before': before, 'after': after, 'limit': limit, }
        return self._patch_paginated_response_data(self._client._call(
            'GET', 'stocks', params={k: v for k, v in params.items() if v is not None},
        ))

    def list_updated(self, since=None, before=None, after=None, limit=None):
        """ Returns a user's cursor-paginated list of stocks.

        :param since: datetime to use to retrieve the stocks
        :param before: cursor pointing to the end of the desired set
        :param after: cursor pointing to the start of the desired set
        :param limit: number of records to return (accepted values: 1 - 500)
        :type since: date or datetime
        :type before: str
        :type after: str
        :type limit: int
        :return: dictionary containing the stocks
        :rtype: dictionary

        """
        params = {
            'since': since.isoformat() if since is not None else None,
            'before': before,
            'after': after,
            'limit': limit,
        }
        return self._patch_paginated_response_data(self._client._call(
            'GET', 'stocks/updated', params={k: v for k, v in params.items() if v is not None},
        ))
