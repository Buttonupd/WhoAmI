from django.test import TestCase

from __future__ import unicode_literals



class SimpleTest(TestCase):

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
