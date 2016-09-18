#!/usr/bin/python

class WaiterAssigner():
	def __init__(self):
		self.MessageSender = None

	def request_waiter(self, data):
		return MessageSender.request_new_waiter(data)
