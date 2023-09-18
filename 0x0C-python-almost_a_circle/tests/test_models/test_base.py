#!/usr/bin/python3
""" make a unittest class"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """the unittest class to check code"""
    def test_base_id(self):
        b1 = Base()
        b2 = Base()
        b3 = Base(10)
        b4 = Base(0)
        b5 = Base(-5)

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 10)
        self.assertEqual(b4.id, 0)
        self.assertEqual(b5.id, -5)

    def test_base_to_json_string(self):
        b1 = Base(1)
        b2 = Base(2)
        b3 = Base(3)

        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{}]), "[{}]")
        self.assertEqual(Base.to_json_string([{'id': 1}, {'id': 2}]), '[{"id": 1}, {"id": 2}]')

    def test_base_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"id": 1}, {"id": 2}]'), [{'id': 1}, {'id': 2}])

    def test_base_save_to_file(self):
        b1 = Base(1)
        b2 = Base(2)
        b3 = Base(3)

        Base.save_to_file([b1, b2, b3])
        with open("Base.json", "r") as file:
            content = file.read()
            self.assertEqual(content, '[{"id": 1}, {"id": 2}, {"id": 3}]')

    def test_base_load_from_file(self):
        b1 = Base(1)
        b2 = Base(2)
        b3 = Base(3)

        Base.save_to_file([b1, b2, b3])
        instances = Base.load_from_file()
        self.assertEqual(len(instances), 3)
        self.assertEqual(instances[0].id, 1)
        self.assertEqual(instances[1].id, 2)
        self.assertEqual(instances[2].id, 3)

if __name__ == '__main__':
    unittest.main()
