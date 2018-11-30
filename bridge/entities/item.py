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

    def delete(self, id):
        """ Deletes an item and all its accounts and transactions.

        :param id: ID of the considered item
        :type id: str or int
        :return: empty dictionary
        :rtype: dictionary

        """
        return self._client._call('DELETE', 'items/{}'.format(id))

    def edit_url(self, id):
        """ Returns the URL to Bridge's Connect funnel to edit an item.

        :param id: ID of the considered item
        :type id: str or int
        :return: dictionary containing the funnel URL
        :rtype: dictionary

        """
        return self._client._call('GET', 'connect/items/edit/url', params={'item_id': id})

    def get(self, id):
        """ Retrieves the details of a single item.

        :param id: ID of the considered item
        :type id: str or int
        :return: dictionary containing the item details
        :rtype: dictionary

        """
        return self._client._call('GET', 'items/{}'.format(id))

    def get_refresh_status(self, id):
        """ Retrieves the refresh status of a single item.

        :param id: ID of the considered item
        :type id: str or int
        :return: dictionary containing the item's refresh status
        :rtype: dictionary

        """
        return self._client._call('GET', 'items/{}/refresh/status'.format(id))

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

    def send_mfa(self, id, otp):
        """ Send an item's MFA.

        :param id: ID of the considered item
        :type id: str or int
        :return: empty dictionary
        :rtype: dictionary

        """
        return self._client._call('POST', 'items/{}/mfa'.format(id), params={'otp': otp})

    def validate_pro(self):
        """ Returns the URL to Bridge's Connect funnel for validating pro items.

        :return: dictionary containing the funnel URL
        :rtype: dictionary

        """
        return self._client._call('GET', 'connect/items/pro/confirmation/url')
