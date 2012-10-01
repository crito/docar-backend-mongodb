from nose.tools import eq_
from mock import patch, Mock

# from docar.exceptions import BackendError
from docar_backend_mongodb import Connection

import unittest


class describe_a_mongodb_connection_object(unittest.TestCase):
    def setUp(self):
        self.connections = Connection._connections
        Connection._connections = {}

    def tearDown(self):
        Connection._connections = self.connections

    def it_has_default_values_for_some_connection_details(self):
        """Most connection parameters have defaults."""
        class ConnectionA(Connection):
            name = 'A'

        eq_(None, ConnectionA.id)
        eq_('localhost', ConnectionA.host)
        eq_(27017, ConnectionA.port)
        eq_(None, ConnectionA.user)
        eq_(None, ConnectionA.password)

    def it_adds_a_connections_configuration_to_the_connection_object(self):
        """Every connection is stored on the Connection object."""
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
        """Creating a connection object returns None or the pymongo connection
        object."""
        # Access the default connection handler
        class ConnectionF(Connection):
            name = 'F'

        with patch('docar_backend_mongodb.pymongo') as mock_mongo:
            mongo_con = Mock()
            mock_mongo.Connection.return_value = {'F': mongo_con}
            connection = Connection()

        eq_(mongo_con, connection)

        # Now access the connection handler per id
        class ConnectionG(Connection):
            name = 'G'
            id = 'id_G'

        with patch('docar_backend_mongodb.pymongo') as mock_mongo:
            mongo_con = Mock()
            mock_mongo.Connection.return_value = {'G': mongo_con}
            connection = Connection('id_G')

        eq_(mongo_con, connection)
