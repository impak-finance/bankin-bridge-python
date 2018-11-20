"""
    Bankin Bridge item entity
    =========================

    This module defines the ``Item`` entity allowing to interact with the underlying API methods.
    Documentation: https://docs.bridgeapi.io/reference/

"""

from ..baseapi import BaseApi


class Item(BaseApi):
    """ Wraps the item-related API methods. """

    def add_url(self):
        """ Generates a new funnel URL.

        :return: dictionary containing the generated redirect URL
        :rtype: dictionary

        """
        return self._client._call('GET', 'items/add/url')

    def get(self, id):
        """ Retrieves the details of a single item.

        :param id: ID of the considered item
        :type id: str or int
        :return: dictionary containing the item details
        :rtype: dictionary

        """
        return self._client._call('GET', 'items/{}'.format(id))

    def list(self, before=None, after=None, limit=None):
        """ List the items associated with the current user.

        :param before: cursor pointing to the end of the desired set
        :param after: cursor pointing to the start of the desired set
        :param limit: number of records to return (accepted values: 1 - 500)
        :type before: str
        :type after: str
        :type limit: int
        :return: dictionary containing the items
        :rtype: dictionary

        """
        params = {'before': before, 'after': after, 'limit': limit, }
        return self._patch_paginated_response_data(self._client._call(
            'GET', 'items', params={k: v for k, v in params.items() if v is not None},
        ))
