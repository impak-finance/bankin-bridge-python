bankin-bridge-python
====================

**Bankin-bridge-python** is a Python module for communicating with the
`Bridgeapi.io API <https://docs.bridgeapi.io/>`_.

.. contents:: Table of Contents
    :local:

Main requirements
-----------------

Python_ 3.4+, Requests_ 2.0+.

Installation
------------

To install Bankin Bridge, please use pip_ (or pipenv_) as follows:

.. code-block:: shell

    $ pip install --pre bankin-bridge

Basic usage
-----------

The first step to interact with the Bankin Bridge API interface is to initialize a ``bridge.Client``
instance. You'll need a client ID and client secret this initialization:

.. code-block:: python

    >>> from bridge import Client
    >>> client = Client('<CLIENT_ID>', '<CLIENT_SECRET>')

Then you can easily register a new user, authenticate them and interact with the implemented
entities and the underlying API endpoints. Here are some examples:

.. code-block:: python

    >>> client.user.create('test@example.com', '<PWD>')
    {'uuid': 'c3b140ad-aa85-49ca-a254-de77de521bbf',
     'resource_uri': '/v2/users/c3b140ad-aa85-49ca-a254-de77de521bbf',
     'resource_type': 'user',
     'email': 'text@example.com'}
    >>> client = client.user.authenticate('test@example.com', '<PWD>')
    {'access_token': '<ACCESS_TOKEN>',
     'expires_at': '2018-11-19T17:20:33.546Z',
     'user': {'uuid': '12f34ca5-da8c-4ac2-8882-3e428033f300',
      'resource_uri': '/v2/users/12f34ca5-da8c-4ac2-8882-3e428033f300',
      'resource_type': 'user',
      'email': 'test@example.com'}}
    >>> client.set_access_token('<ACCESS_TOKEN>')
    >>> client.item.add_url()
    {'redirect_url': 'https://connect.bankin.com?token_uuid=fb12c345-b1ae-234a-1cc2-123456789dac'}
    >>> client.account.list()
    ...

Authors
-------

impak Finance <tech@impakfinance.com>.

License
-------

MIT. See ``LICENSE`` for more details.


.. _pip: https://github.com/pypa/pip
.. _pipenv: https://github.com/pypa/pipenv
.. _Python: https://www.python.org/
.. _Requests: http://docs.python-requests.org/en/master/
