from django.test import TestCase

# Create your tests here.
class MyTestCases(TestCase):
    def test_add(self):
        self.assertEquals(1 + 1, 2)

    def test_sub(self):
        self.assertEquals(2 - 1, 1)

    def test_product(self):
        self.assertEquals(2 * 2, 4)

    def test_div(self):
        self.assertEquals(4 / 2, 2)

