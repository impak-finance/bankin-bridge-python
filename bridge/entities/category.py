"""
    Bankin Bridge category entity
    =============================

    This module defines the ``Category`` entity allowing to interact with the underlying API
    methods.
    Documentation: https://docs.bridgeapi.io/reference/

"""

from ..baseapi import BaseApi


class Category(BaseApi):
    """ Wraps the category-related API methods. """

    def get(self, id):
        """ Retrieves the details of a single category.

        :param id: ID of the considered category
        :type id: str or int
        :return: dictionary containing the category details
        :rtype: dictionary

        """
        return self._client._call('GET', 'categories/{}'.format(id))

    def list(self, before=None, after=None, limit=None):
        """ Returns a cursor-paginated list of categories.

        :param before: cursor pointing to the end of the desired set
        :param after: cursor pointing to the start of the desired set
        :param limit: number of records to return (accepted values: 1 - 500)
        :type before: str
        :type after: str
        :type limit: int
        :return: dictionary containing the categories
        :rtype: dictionary

        """
        params = {'before': before, 'after': after, 'limit': limit, }
        return self._patch_paginated_response_data(self._client._call(
            'GET', 'categories', params={k: v for k, v in params.items() if v is not None},
        ))
