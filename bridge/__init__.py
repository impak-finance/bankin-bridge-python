"""
    Bankin Bridge client
    ====================

    The Bankin Bridge client implements the endpoints/methods of the REST API provided by the
    Bridgeapi.io service (https://docs.bridgeapi.io/). Bankin Bridge is a service that connects
    applications with european financial accounts.

"""

# Deploying a new version:
# 1. remove the ".dev" from the current version number
# 2. create a new commit (eg. "Prepared 0.1.1 release")
# 3. run "git tag x.y.z" (eg. "git tag 0.1.1")
# 4. run "python setup.py sdist bdist_wheel upload"
# 5. bump the version (increment the version and append a ".dev" to it). eg. "0.1.2.dev"
# 6. create a new commit (eg. "Bumped version to 0.1.2.dev")
# 7. run "git push" and "git push --tags"


__version__ = '0.1.0a2'


from .client import Client  # noqa: F401
