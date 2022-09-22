# Тесты клиента

import sys
import os
import unittest

sys.path.append(os.path.join(os.getcwd(), '..'))
from general.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE
from client_part import create_presence, process_answer


class TestClass(unittest.TestCase):

    def test_def_presense(self):
        test = create_presence()
        test[TIME] = 1.1
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})

    def test_ok_answer(self):
        self.assertEqual(process_answer({RESPONSE: 200}), '200 : OK')

    def test_bad_answer(self):
        self.assertEqual(process_answer({RESPONSE: 400, ERROR: 'Bad Request'}), '400 : Bad Request')


if __name__ == '__main__':
    unittest.main()
