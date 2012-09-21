from nose.tools import eq_

# from docar.exceptions import BackendError
from docar_backend_mongo import Connection

import unittest


class describe_a_mongodb_connection_object(unittest.TestCase):
    def setUp(self):
        self.connections = Connection._connections
        Connection._connections = {}

    def tearDown(self):
        Connection._connections = self.connections

    def it_has_default_values_for_some_connection_details(self):
        class ConnectionA(Connection):
            name = 'A'

        eq_(None, ConnectionA.id)
        eq_('localhost', ConnectionA.host)
        eq_(27017, ConnectionA.port)
        eq_(None, ConnectionA.user)
        eq_(None, ConnectionA.password)

    def it_adds_a_connections_configuration_to_the_connection_object(self):
        class ConnectionB(Connection):
            name = 'B'

        eq_(1, len(Connection._connections.keys()))

    def it_stores_one_connection_as_default_id(self):
        """If no id is supplied, only one connection is assumed the default
        connection."""
        # Declare the first 2 connections, without id. There should be one
        # connection available.
        class ConnectionC(Connection):
            name = 'C'

        class ConnectionD(Connection):
            name = 'D'

        eq_(1, len(Connection._connections.keys()))

        class ConnectionE(Connection):
            name = 'E'
            id = 'id_E'

        eq_(2, len(Connection._connections.keys()))

    def it_can_return_the_correct_connection(self):
        """Creating a connection object returns None or the connection."""
        class ConnectionF(Connection):
            name = 'F'

        connection = Connection()

        eq_(True, isinstance(connection, ConnectionF))
