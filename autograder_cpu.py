#!/usr/bin/env python

import autograder_base
import os.path

from autograder_base import file_locations, AbsoluteTestCase, FractionalTestCase, main

tests = [
  ("CPU sll test",FractionalTestCase(os.path.join(file_locations,'CPU-sll.circ'),os.path.join(file_locations,'out-files/CPU-sll.out'),1)),
  ("CPU add/lui test",FractionalTestCase(os.path.join(file_locations,'CPU-add_lui.circ'),os.path.join(file_locations,'out-files/CPU-add_lui.out'),1)),
  ("CPU branches test",FractionalTestCase(os.path.join(file_locations,'CPU-branches.circ'),os.path.join(file_locations,'out-files/CPU-branches.out'),1)),
  ("CPU jump test",FractionalTestCase(os.path.join(file_locations,'CPU-jump.circ'),os.path.join(file_locations,'out-files/CPU-jump.out'),1)),
  ("CPU mem test",FractionalTestCase(os.path.join(file_locations,'CPU-mem.circ'),os.path.join(file_locations,'out-files/CPU-mem.out'),1)),
  ("CPU swinc test",FractionalTestCase(os.path.join(file_locations,'CPU-swinc.circ'),os.path.join(file_locations,'out-files/CPU-swinc.out'),1))
]

if __name__ == '__main__':
  main(tests)
