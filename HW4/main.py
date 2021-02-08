from average import*
from volume import*
from fullname import*
from statistics import*
import unittest
"""
main.py (this file) contains tests for all programs in the assignment
"""

class TestCase(unittest.TestCase):
  #tests on volume
  def test_case_1(self):
    self.assertEqual (volume(2,2,2), 8)
  def test_case_2(self):
    self.assertEqual (volume(2,2,"h"),TypeError)
  def test_case_3(self):
    self.assertEqual (volume(2,2,-1),"bad inputs result was negative")
  #tests on average
  def test_case_1a(self):
    self.assertEqual (average([1,2,3]), 2)
  def test_case_2a(self):
    self.assertEqual (average([1,2,"h"]), TypeError)
  def test_case_3a(self):
    self.assertEqual (average([]), "no inputs")
  #tests on fullname
  def test_case_1b(self):
    self.assertEqual (fullname("hello", "world"), "hello world")
  def test_case_2b(self):
    self.assertEqual (fullname(None, None), "bad input")
  def test_case_3b(self):
    self.assertEqual (fullname("¡","¡"), "¡ ¡")




if __name__ == '__main__':unittest.main()