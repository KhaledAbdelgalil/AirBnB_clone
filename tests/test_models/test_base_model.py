#!/usr/bin/python3
"""Defines unittests for models/base_model.py.

Unittest classes:
    TestBaseModel
    TestBaseModelSave
"""
from models.base_model import BaseModel
import models
import unittest
from datetime import datetime
from time import sleep
import os


class TestBaseModel(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_type(self):
        self.assertEqual(type(BaseModel()), BaseModel)

    def test_baseModelStorage(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_type_id(self):
        self.assertEqual(type(BaseModel().id), str)

    def test_type_created_at(self):
        self.assertEqual(type(BaseModel().created_at), datetime)

    def test_type_updated_at(self):
        self.assertEqual(type(BaseModel().updated_at), datetime)

    def test_id_unique(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_different_created_at(self):
        obj1 = BaseModel()
        sleep(0.1)
        obj2 = BaseModel()
        self.assertLess(obj1.created_at, obj2.created_at)

    def test_different_updated_at(self):
        obj1 = BaseModel()
        sleep(0.1)
        obj2 = BaseModel()
        self.assertLess(obj1.updated_at, obj2.updated_at)

    def test_baseModelStr(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        obj1 = BaseModel()
        obj1.id = "123456"
        obj1.created_at = obj1.updated_at = dt
        obj1Str = obj1.__str__()
        self.assertIn("[BaseModel] (123456)", obj1Str)
        self.assertIn("'id': '123456'", obj1Str)
        self.assertIn("'created_at': " + dt_repr, obj1Str)
        self.assertIn("'updated_at': " + dt_repr, obj1Str)

    def test_args_unused(self):
        obj = BaseModel(None)
        self.assertNotIn(None, obj.__dict__.values())

    def test_construction_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        obj = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(obj.id, "345")
        self.assertEqual(obj.created_at, dt)
        self.assertEqual(obj.updated_at, dt)

    def test_construction_with_args_and_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        obj = BaseModel("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(obj.id, "345")
        self.assertEqual(obj.created_at, dt)
        self.assertEqual(obj.updated_at, dt)

    def test_type_to_dict(self):
        obj = BaseModel()
        self.assertTrue(dict, type(obj.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        obj = BaseModel()
        self.assertIn("id", obj.to_dict())
        self.assertIn("created_at", obj.to_dict())
        self.assertIn("updated_at", obj.to_dict())
        self.assertIn("__class__", obj.to_dict())

    def test_to_dict_contains_added_attributes(self):
        obj = BaseModel()
        obj.name = "Holberton"
        obj.my_number = 98
        self.assertIn("name", obj.to_dict())
        self.assertIn("my_number", obj.to_dict())

    def test_type_to_dict_created_updated_attributes(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertEqual(str, type(obj_dict["created_at"]))
        self.assertEqual(str, type(obj_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        obj = BaseModel()
        obj.id = "123456"
        obj.created_at = obj.updated_at = dt
        tdict = {
            "id": "123456",
            "__class__": "BaseModel",
            "created_at": dt.isoformat(),
            "updated_at": dt.isoformat(),
        }
        self.assertDictEqual(obj.to_dict(), tdict)

    def test_to_dict_dunder_dict(self):
        obj = BaseModel()
        self.assertNotEqual(obj.to_dict(), obj.__dict__)

    def test_to_dict_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.to_dict(None)


class TestBaseModelSave(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

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
        obj = BaseModel()
        sleep(0.1)
        initial_updated_at = obj.updated_at
        obj.save()
        self.assertLess(initial_updated_at, obj.updated_at)

    def test_save_with_arg(self):
        obj = BaseModel()
        with self.assertRaises(TypeError):
            obj.save(None)

    def test_save_updates_file(self):
        obj = BaseModel()
        obj.save()
        objId = "BaseModel." + obj.id
        with open("file.json", "r") as f:
            self.assertIn(objId, f.read())


if __name__ == "__main__":
    unittest.main()
