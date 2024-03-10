#!/usr/bin/python3

from models.amenity import Amenity
import models
import unittest
from datetime import datetime
from time import sleep
import os

class TestAmenity(unittest.TestCase):
    def test_type(self):
        self.assertEqual(type(Amenity()), Amenity)

    def test_Storage(self):
        self.assertIn(Amenity(), models.storage.all().values())
    
    def test_type_id(self):
        self.assertEqual(type(Amenity().id), str)
    
    def test_type_created_at(self):
        self.assertEqual(type(Amenity().created_at), datetime)

    def test_type_updated_at(self):
        self.assertEqual(type(Amenity().updated_at), datetime)
    
    def test_id_unique(self):
        obj1 = Amenity()
        obj2 = Amenity()
        self.assertNotEqual(obj1.id, obj2.id)
    
    def test_different_created_at(self):
        obj1 = Amenity()
        sleep(0.1)
        obj2 = Amenity()
        self.assertLess(obj1.created_at, obj2.created_at)
    
    def test_different_updated_at(self):
        obj1 = Amenity()
        sleep(0.1)
        obj2 = Amenity()
        self.assertLess(obj1.updated_at, obj2.updated_at)
    
    def tst_Str(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        obj1 = Amenity()
        obj1.id = "123456"
        obj1.created_at = obj1.updated_at = dt
        obj1.name = "temp"
        obj1Str = obj1.__str__()
        self.assertIn("[Amenity] (123456)", obj1Str)
        self.assertIn("'id': '123456'", obj1Str)
        self.assertIn("'created_at': " + dt_repr, obj1Str)
        self.assertIn("'updated_at': " + dt_repr, obj1Str)
        self.assertIn("name: temp", obj1Str)
    
    def test_args_unused(self):
        obj = Amenity(None)
        self.assertNotIn(None, obj.__dict__.values())

    def test_construction_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        obj = Amenity(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(obj.id, "345")
        self.assertEqual(obj.created_at, dt)
        self.assertEqual(obj.updated_at, dt)

    def test_construction_with_args_and_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        obj = Amenity("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(obj.id, "345")
        self.assertEqual(obj.created_at, dt)
        self.assertEqual(obj.updated_at, dt)
    
    def test_type_to_dict(self):
        obj = Amenity()
        self.assertTrue(dict, type(obj.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        obj = Amenity()
        self.assertIn("id", obj.to_dict())
        self.assertIn("created_at", obj.to_dict())
        self.assertIn("updated_at", obj.to_dict())
        self.assertIn("__class__", obj.to_dict())

    def test_to_dict_contains_added_attributes(self):
        obj = Amenity()
        obj.name = "Holberton"
        obj.my_number = 98
        self.assertIn("name", obj.to_dict())
        self.assertIn("my_number", obj.to_dict())

    def test_type_to_dict_created_updated_attributes(self):
        obj = Amenity()
        obj_dict = obj.to_dict()
        self.assertEqual(str, type(obj_dict["created_at"]))
        self.assertEqual(str, type(obj_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        obj = Amenity()
        obj.id = "123456"
        obj.created_at = obj.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'Amenity',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(obj.to_dict(), tdict)

    def test_to_dict_dunder_dict(self):
        obj = Amenity()
        self.assertNotEqual(obj.to_dict(), obj.__dict__)

    def test_to_dict_with_arg(self):
        bm = Amenity()
        with self.assertRaises(TypeError):
            bm.to_dict(None)

class TestAmenitySave(unittest.TestCase):
    """Unittests for testing save method of the Amenity class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "testTmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("testTmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        obj = Amenity()
        sleep(0.1)
        initial_updated_at = obj.updated_at
        obj.save()
        self.assertLess(initial_updated_at, obj.updated_at)

    def test_save_with_arg(self):
        obj = Amenity()
        with self.assertRaises(TypeError):
            obj.save(None)

    def test_save_updates_file(self):
        obj = Amenity()
        obj.save()
        objId = "Amenity." + obj.id
        with open("file.json", "r") as f:
            self.assertIn(objId, f.read())

if __name__ == "__main__":
    unittest.main()