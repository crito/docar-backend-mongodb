from docar.exceptions import BackendError

import pymongo


class ConnectionMeta(type):
    def __new__(meta, classname, bases, class_dict):
        klass = type.__new__(meta, classname, bases, class_dict)

        # We don't do anything special when the normal Connection class is
        # defined
        if classname == 'Connection':
            return klass

        # Every connection handler must have the dbname configured.
        if not 'name' in class_dict:
            # name must be specified, we can't guess the db name
            raise BackendError

        if not klass.id:
            # This is the default handler name
            name = ''
        else:
            name = klass.id

        # store the connection handler
        klass._connections[name] = klass

        return klass


class Connection(object):
    """Get the correct mongodb connection handler.

    To define a connection handler, write a class that inerits from
    ``Connection``.

        >>> class MyConnection(Connection):
        ...     name = 'dbname'
        ...     host = 'localhost'    # defaults to localhost
        ...     port = 27017          # defaults to 27017
        ...     user = None           # defaults to None, optional
        ...     password = None       # defaults to None, optional
        ...     id = 'connection_id'  # defaults to None, default handler

    ``name`` is the only attribute that *must* be specified. All the other
    attributes have a default values.

    Requesting a connection always returns the mongo connection object mapped
    to the pymongo connection handler.

        >>> connection = Connection('connection_id')
        >>> connection = Connection()  # returns default connection handler
        >>> isinstance(connection, pymongo.Connection)
        True

    """
    __metaclass__ = ConnectionMeta

    _connections = {}

    id = None
    host = 'localhost'
    port = 27017
    user = None
    password = None

    def __new__(self, connection=None, *args, **kwargs):
        """Return the mongo connection object."""
        try:
            Handler = self._connections[connection if connection else '']
            # connection = object.__new__(Connection)
            mongo = pymongo.Connection(
                    host=Handler.host,
                    port=Handler.port)
            connection = mongo[Handler.name]
        except KeyError:
            # FIXME: Maybe raise an exception here?
            pass
        return connection
