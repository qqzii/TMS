import unittest
from unittest.mock import Mock

import task

class Tests(unittest.TestCase):
    def test_fn1(self):
        task.fn2 = Mock(
            return_value=True
        )
        assert task.fn1(2) == 'OK'
