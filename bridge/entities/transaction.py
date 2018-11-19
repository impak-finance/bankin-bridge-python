"""
    Bankin Bridge transaction entity
    ================================

    This module defines the ``Transaction`` entity allowing to interact with the underlying API
    methods.
    Documentation: https://docs.bridgeapi.io/reference/

"""

from ..baseapi import BaseApi


class Transaction(BaseApi):
    """ Wraps the transaction-related API methods. """

    def get(self, id):
        """ Retrieves the details of a single transaction.

        :param id: ID of the considered transaction
        :type id: str or int
        :return: dictionary containing the transaction details
        :rtype: dictionary

        """
        return self._client._call('GET', 'transactions/{}'.format(id))

    def list(self, before=None, after=None, limit=None):
        """ Lists the transactions associated with the current user.

        :param before: cursor pointing to the end of the desired set
        :param after: cursor pointing to the start of the desired set
        :param limit: number of records to return (accepted values: 1 - 500)
        :type before: str
        :type after: str
        :type limit: int
        :return: dictionary containing the transactions
        :rtype: dictionary

        """
        params = {'before': before, 'after': after, 'limit': limit, }
        return self._client._call(
            'GET', 'transactions', params={k: v for k, v in params.items() if v is not None},
        )

    def list_by_account(self, account_id, before=None, after=None, limit=None):
        """ Lists the transactions associated with the current user for a given bank account.

        :param account_id: ID of the considered bank account
        :param before: cursor pointing to the end of the desired set
        :param after: cursor pointing to the start of the desired set
        :param limit: number of records to return (accepted values: 1 - 500)
        :type account_id: str or int
        :type before: str
        :type after: str
        :type limit: int
        :return: dictionary containing the transactions
        :rtype: dictionary

        """
        params = {'before': before, 'after': after, 'limit': limit, }
        return self._client._call(
            'GET',
            'accounts/{}/transactions'.format(account_id),
            params={k: v for k, v in params.items() if v is not None},
        )

    def list_updated(self, timesince=None, before=None, after=None, limit=None):
        """ Lists the transactions of the current user that were updated after a datetime.

        :param timesince: datetime to use to retrieve the transactions
        :param before: cursor pointing to the end of the desired set
        :param after: cursor pointing to the start of the desired set
        :param limit: number of records to return (accepted values: 1 - 500)
        :type timesince: datetime
        :type before: str
        :type after: str
        :type limit: int
        :return: dictionary containing the transactions
        :rtype: dictionary

        """
        params = {
            'timesince': timesince.isoformat() if timesince else None,
            'before': before,
            'after': after,
            'limit': limit,
        }
        return self._client._call(
            'GET',
            'transactions/updated',
            params={k: v for k, v in params.items() if v is not None},
        )

    def list_updated_by_account(
        self, account_id, timesince=None, before=None, after=None, limit=None,
    ):
        """ Lists the transactions of the current user for a given bank account that were updated
            after a datetime.

        :param account_id: ID of the considered bank account
        :param timesince: datetime to use to retrieve the transactions
        :param before: cursor pointing to the end of the desired set
        :param after: cursor pointing to the start of the desired set
        :param limit: number of records to return (accepted values: 1 - 500)
        :type account_id: str or int
        :type timesince: datetime
        :type before: str
        :type after: str
        :type limit: int
        :return: dictionary containing the transactions
        :rtype: dictionary

        """
        params = {
            'timesince': timesince.isoformat() if timesince else None,
            'before': before,
            'after': after,
            'limit': limit,
        }
        return self._client._call(
            'GET',
            'accounts/{}/transactions/updated'.format(account_id),
            params={k: v for k, v in params.items() if v is not None},
        )
