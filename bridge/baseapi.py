"""
    Bankin Bridge base API abstraction
    ==================================

    This module defines the ``BaseApi`` class allowing to construct various endpoint paths.

"""

from itertools import chain
from urllib.parse import parse_qsl, urlparse


class BaseApi:
    """ Simple class to buid path for entities. """

    def __init__(self, client):
        """ Initializes the class using a Bankin Bridge client. """
        self._client = client
        self.endpoint = ''

    def _build_path(self, *args):
        """ Builds a path using the configured endpoint and path arguments. """
        return '/'.join(chain((self.endpoint, ), map(str, args)))

    def _patch_paginated_response_data(self, data):
        """ Patches the given paginated data in order to extract paginated values from the next or
            previous URI.
        """
        def _parse_paginated_uri(uri):
            parsed_uri = urlparse(uri)
            parsed_querystring = parse_qsl(parsed_uri.query)
            pagination_params = ('before', 'after', 'limit', )
            return {p[0]: p[1] for p in parsed_querystring if p[0] in pagination_params}

        if 'pagination' in data and data['pagination']['next_uri']:
            next_uri = data['pagination']['next_uri']
            data['pagination']['next'] = _parse_paginated_uri(next_uri)
        if 'pagination' in data and data['pagination']['previous_uri']:
            previous_uri = data['pagination']['previous_uri']
            data['pagination']['previous'] = _parse_paginated_uri(previous_uri)
        return data
