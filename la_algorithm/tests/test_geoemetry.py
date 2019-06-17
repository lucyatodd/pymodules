"""
Test for Fibonacci implementations logic.
"""
import unittest
import logging
import logging.config

from geometry.circle import area, circumference, volume
from geometry.trig import sin_angle, cos_angle, tan_angle

logging.config.fileConfig("logging.properties")
logger = logging.getLogger()

class TestCircle(unittest.TestCase):
    """
    Tests for area and circumference
    """

    def test_area(self):
      """
      Verify that all implementations have same result.
      """
      name = "Area: "
      a = area(5)
      logger.info("%s %f", name, a )
      self.assertGreater(a, 78)
      self.assertGreater(a, 78.5)

    def test_circumference(self):
          """
          Verify that all implementations have same result.
          """
          name = "Circumference: "
          c = circumference(5)
          logger.info("%s %f", name, c )
          self.assertGreater(c, 31)
          self.assertLess(c, 32)

    def test_volume(self):
          """
          Verify that all implementations have same result.
          """
          name = "Volume: "
          v = volume(5)
          logger.info("%s %f", name, v )
          self.assertGreater(v, 523)
          self.assertLess(v, 524)

    def test_sin_angle(self):
          """
          Verify that all implementations have same result.
          """
          name = "Sin angle: "
          a = sin_angle(5, 10)
          logger.info("%s %f", name, a )
          self.assertEqual(a, 30)

if __name__ == '__main__':
    unittest.main()
