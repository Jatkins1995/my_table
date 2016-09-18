#!/usr/bin/python

import unittest
from my_table.customer.modules.waiter_assigner.waiter_assigner import *

class Test_Waiter_Assigner(unittest.TestCase):
	
	def test_waiter_assigner_is_proper_type(self):
		target = WaiterAssigner()
		self.assertTrue(isinstance(target,  WaiterAssigner))

	def test_waiter_request__succeeds(self):
		target = WaiterAssigner()
		data = {}
		data["resturant_name"] = "Bobs Burgers"
		data["section_id"] = "A"
		data["table_id"] = "2"
		return_val = target.request_waiter(data)
		self.assertTrue(return_val)
		
		
	

if __name__ == "__main__":
	unittest.main()
