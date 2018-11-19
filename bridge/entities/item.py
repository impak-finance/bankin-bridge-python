"""
    Bankin Bridge item entity
    =========================

    This module defines the ``Item`` entity allowing to interact with the underlying API methods.
    Documentation: https://docs.bridgeapi.io/reference/

"""

from ..baseapi import BaseApi


class Item(BaseApi):
    """ Wraps the item-related API methods. """

    def add_url(self, access_token):
        """ Generates a new funnel URL.

        :param access_token: a valid token identifying the considered app and user
        :type access_token: str
        :return: dictionary containing the generated redirect URL
        :rtype: dictionary

        """
        return self._client._call('GET', 'items/add/url', access_token=access_token)
