import unittest
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestContinent(TestBase):
    def test_continent(self):
        response = self.client.get(url_for)