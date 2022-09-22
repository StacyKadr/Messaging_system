# Тесты утилит

import sys
import os
import unittest
import json
sys.path.append(os.path.join(os.getcwd(), '..'))
from general.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE, ENCODING
from general.utils import get_message, send_message


class TestSocket:

    def __init__(self, test_dictionary):
        self.test_dictionary = test_dictionary
        self.encoded_message = None
        self.received_message = None

    def send(self, message_to_send):
        json_test_message = json.dumps(self.test_dictionary)
        self.encoded_message = json_test_message.encode(ENCODING)
        self.received_message = message_to_send

    def recv(self, max_len):
        json_test_message = json.dumps(self.test_dictionary)
        return json_test_message.encode(ENCODING)


class Tests(unittest.TestCase):

    test_dictionary_send = {
        ACTION: PRESENCE,
        TIME: 111111.111111,
        USER: {
            ACCOUNT_NAME: 'test_test'
        }
    }
    test_dict_recv_check = {RESPONSE: 200}
    test_dict_recv_error = {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }

    def test_send_message(self):

        test_socket = TestSocket(self.test_dictionary_send)
        send_message(test_socket, self.test_dictionary_send)
        self.assertEqual(test_socket.encoded_message, test_socket.received_message)
        with self.assertRaises(Exception):
            send_message(test_socket, test_socket)

    def test_get_message(self):

        test_sock_check = TestSocket(self.test_dict_recv_check)
        test_sock_error = TestSocket(self.test_dict_recv_error)
        self.assertEqual(get_message(test_sock_check), self.test_dict_recv_check)
        self.assertEqual(get_message(test_sock_error), self.test_dict_recv_error)


if __name__ == '__main__':
    unittest.main()
