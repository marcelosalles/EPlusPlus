import unittest
from eplusplus.model.platformManager import PlatformManager

class TestPlatformManager(unittest.TestCase):
	def testCheckAndInstallLinux(self, pM):
		self.assertEqual(pM.checkAndInstall(), True)

	def testCheckAndInstallWindows(self, pM):
		self.assertEqual(pM.checkAndInstall(), True)
