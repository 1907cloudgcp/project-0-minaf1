import unittest
from service.service import *
import logging


class TestModule(unittest.TestCase):
	logger = logging.getLogger(__name__)

	def setUp(self):
		self.serv = Service()

	def testLogin(self):
		self.assertTrue(self.serv.login('john', 'smith'))
		logger.debug('DEBUG:Test: test login: Completed Successfully')

	def testLoginFail(self):
		self.assertFalse(self.serv.login('john', 'smithhhhh'))
		logger.debug('DEBUG:Test: test login failure: Completed Successfully')

	def testWithdraw(self):
		self.assertTrue(self.serv.withdraw(20))
		logger.debug('DEBUG:Test: test withdrawal: Completed Successfully')

	def testWithdrawFail(self):
		self.assertFalse(self.serv.withdraw(2000000))
		logger.debug('DEBUG:Test: test withdrawal failure: Completed Successfully')


if __name__ == '__main__':
	unittest.main()
