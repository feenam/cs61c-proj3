#!/usr/bin/env python

import os
import os.path
import tempfile
import subprocess
import time
import signal
import re
import sys
import shutil

file_locations = os.path.expanduser(os.getcwd())
logisim_location = os.path.join(os.getcwd(),"logisim.jar")


class TestCase():
  """
      Runs specified circuit file and compares output against the provided reference trace file.
  """

  def __init__(self, circfile, tracefile):
    self.circfile  = circfile
    self.tracefile = tracefile

  def __call__(self):
    output = tempfile.TemporaryFile(mode='r+')
    proc = subprocess.Popen(["java","-jar",logisim_location,"-tty","table",os.path.join('.',os.path.basename(self.circfile))],
                            stdin=open('/dev/null'),
                            stdout=subprocess.PIPE)
    try:
      reference = open(self.tracefile)
      passed = compare_unbounded(proc.stdout,reference)
    finally:
      os.kill(proc.pid,signal.SIGTERM)
    if passed:
      return (True, "Matched expected output")
    else:
      return (False, "Did not match expected output")

def compare_unbounded(student_out, reference_out):
  while True:
    line1 = student_out.readline()
    line2 = reference_out.readline()
    if line2 == '':
      break
    if line1 != line2:
      return False
  return True

def run_tests(tests):
  # actual submission testing code
  print "Testing files..."
  tests_passed = 0
  tests_failed = 0

  for description,test in tests:
    test_passed, reason = test()
    if test_passed:
      print "\tPASSED test: %s" % description
      tests_passed += 1
    else:
      print "\tFAILED test: %s (%s)" % (description, reason)
      tests_failed += 1
  
  print "Passed %d/%d tests" % (tests_passed, (tests_passed + tests_failed))

tests = [
  ("ALU add (with overflow) test",
        TestCase(os.path.join(file_locations,'alu-add.circ'),
                 os.path.join(file_locations,'reference_output/alu-add.out'))),
  ("ALU multu test",
        TestCase(os.path.join(file_locations,'alu-multu.circ'),
                 os.path.join(file_locations,'reference_output/alu-multu.out'))),
  ("RegFile insert test",
        TestCase(os.path.join(file_locations,'regfile-insert.circ'),
                 os.path.join(file_locations,'reference_output/regfile-insert.out'))),
  ("RegFile $zero test",
        TestCase(os.path.join(file_locations,'regfile-zero.circ'),
                 os.path.join(file_locations,'reference_output/regfile-zero.out'))),
]

if __name__ == '__main__':
  run_tests(tests)
