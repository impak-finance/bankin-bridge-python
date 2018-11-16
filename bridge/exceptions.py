"""
    Bankin Bridge client exceptions
    ===============================

    This module defines top-level exceptions that can be used by the Bankin Bridge client
    implementation.

"""


class BankinBridgeError(Exception):
    """ Base exception for all exceptions that can be raised by the Bankin Bridge client. """

    def __init__(self, msg=None):
        self.msg = msg

    def __str__(self):
        return self.msg or super().__str__()


class TransportError(BankinBridgeError):
    """ Raised when an error occurs related to the connection with the Bankin Bridge service. """

    def __init__(self, msg, response):
        super().__init__(msg)
        self.response = response


class ProtocolError(BankinBridgeError):
    """ Raised when an error occurs related to the response processing. """

    def __init__(self, msg, response=None, data=None):
        super().__init__(msg)
        self.response = response
        self.data = data
