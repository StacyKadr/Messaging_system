# Tесты сервера

import sys
import os
import unittest
sys.path.append(os.path.join(os.getcwd(), '..'))
from general.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE
from server_part import process_client_message


class TestServer(unittest.TestCase):

    error_dict = {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }
    normal_dict = {RESPONSE: 200}

    def test_unknown_action(self):
        self.assertEqual(process_client_message(
            {ACTION: 'Unknown', TIME: '1.1', USER: {ACCOUNT_NAME: 'Guest'}}), self.error_dict)

    def test_unknown_user(self):
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest123'}}), self.error_dict)

    def test_no_time(self):
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, USER: {ACCOUNT_NAME: 'Guest'}}), self.error_dict)

    def test_no_user(self):
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: '1.1'}), self.error_dict)

    def test_ok_work(self):
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}}), self.normal_dict)


if __name__ == '__main__':
    unittest.main()
