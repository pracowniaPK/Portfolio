from django.test import TestCase


class InitTestCase(TestCase):
    def test_sanity_check(self):
        self.assertAlmostEqual(1, 1)
