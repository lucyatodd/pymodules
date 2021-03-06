"""
Test for Fibonacci implementations logic.
"""

import unittest
import logging
import logging.config

from fibonaci.goldenratio import sequence

logging.config.fileConfig("logging.properties")
logger = logging.getLogger()


class TestFibonacciImplementations(unittest.TestCase):
  """
  Tests for Fibonacci implementations.
  """

  def test_implementations_same_result(self):
    """
    Verify that all implementations have same result.
    """
    logger.info("Test fib")
    result = sequence(6)
    self.assertEqual([0, 1, 1, 2, 3, 5, 8], result)



if __name__ == '__main__':
    unittest.main()
