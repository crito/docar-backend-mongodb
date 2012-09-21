# from docar.exceptions import BackendError


def raise_(exc):
    raise exc


class ConnectionMeta(type):
    def __new__(meta, classname, bases, class_dict):
        klass = type.__new__(meta, classname, bases, class_dict)

        if classname != 'Connection':
            if not klass.id:
                name = ''
            else:
                name = klass.id

            klass._connections[name] = klass

        return klass


class Connection(object):
    __metaclass__ = ConnectionMeta

    _connections = {}

    id = None
    host = 'localhost'
    port = 27017
    user = None
    password = None

    def __new__(self, connection=None, *args, **kwargs):
        """Access the connection."""
        try:
            Connection = self._connections[connection if connection else '']
            connection = object.__new__(Connection)
        except KeyError:
            # FIXME: Maybe raise an exception here?
            pass
        return connection
