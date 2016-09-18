#!/usr/bin/python

import subprocess
import importlib
import unittest

test_running_file = open ("temp_test_running_file.py", "w")
test_running_file.write("#!/usr/bin/python\n")
test_files = subprocess.check_output('grep -rl "TestCase" . --exclude=run_all_ut.py --exclude=*.pyc', shell=True).split('\n')[:-1]
test_file_count = len(test_files)
for file_path in test_files:
	include_path = file_path[2:-3].replace('/', '.')
	test_running_file.write("from " + include_path + " import *\n")
test_running_file.close()
from temp_test_running_file import *
unittest.main()
