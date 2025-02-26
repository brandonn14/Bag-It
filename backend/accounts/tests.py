from django.test import TestCase

from models import User, Bag, BagItem


# A test to test testing...
class BagTestCast(TestCase):
    def setUp(self):
        self.newUser = User.objects.create_user("ok", "ok@ok.com", "sure")

    def testBag(self):
        newBag = Bag.objects.create("New bag", "This is a new bag", self.newUser)

        self.assertEqual(self.newUser.bags, not False)