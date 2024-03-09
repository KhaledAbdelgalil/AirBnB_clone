#!/usr/bin/python3
"""
Defines the Console class,
which serves as the entry point of the Airbnb Project.
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models import storage
from json import loads
import re


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    __foundClasses = {"BaseModel": BaseModel, "User": User, "State":State,
                      "City": City, "Amenity":Amenity, "Place":Place, "Review": Review}
   
    def default(self, line):
        args = re.findall("(.*)\.(.*)\((.*)\)", line)
        if args and len(args[0]) >= 2:
            foundFunctions =  {
                "all": self.do_all,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "count": self.do_count,
                "update": self.do_update
            }
            class_name = args[0][0]
            method_name = args[0][1]
            rest_args = ""
            if len(args[0]) > 2:
                rest_args = args[0][2].split(',')
            if method_name in foundFunctions.keys():
                arg = str(class_name)
                if rest_args != "":
                    for element in rest_args:
                        arg = arg + " " + str(element)
                arg = arg.rstrip(' ')
                return foundFunctions[method_name](arg)
        
        print("*** Unknown syntax: {}".format(line))
        return False

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        return True

    def emptyline(self):
        return

    def help_quit(self):
        print("Quit command to exit the program\n")

    def help_EOF(self):
        print("EOF\n")

    def do_create(self, arg):
        if len(arg) == 0:
            print("** class name missing **")
        elif arg in self.__foundClasses:
            obj = self.__foundClasses[arg]()
            print(obj.id)
            storage.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
        else:
            if args[0] in self.__foundClasses:
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    allObjects = storage.all()
                    object_key = "{}.{}".format(args[0], args[1])
                    if object_key in allObjects:
                        object = allObjects[object_key]
                        print(object)
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
        else:
            if args[0] in self.__foundClasses:
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    allObjects = storage.all()
                    object_key = "{}.{}".format(args[0], args[1])
                    if object_key in allObjects:
                        del allObjects[object_key]
                        storage.save()
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def bring_classes(self, class_type=None):
        objects_list = []
        allObjects = storage.all().values()
        for object in allObjects:
            if class_type == None or class_type == object.__class__.__name__:
                objects_list.append(object.__str__())
        print(objects_list)

    def do_all(self, arg):
        if arg == "":
            self.bring_classes()
        elif arg not in self.__foundClasses:
            print("** class doesn't exist **")
        else:
           self.bring_classes(arg)

    def do_update(self, arg):
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
        else:
            if args[0] in self.__foundClasses:
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    allObjects = storage.all()
                    object_key = "{}.{}".format(args[0], args[1])
                    if object_key in allObjects:
                        obj = allObjects[object_key]
                        if len(args) < 3:
                            print("** attribute name missing **")
                        elif len(args) < 4:
                            print("** value missing **")
                        else:
                            obj.__dict__[args[2]] = loads(args[3].replace("'", '"'))
                            obj.save()
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")
    
    def do_count(self, arg):
        count = 0
        allObjects = storage.all().values()
        for object in allObjects:
            if arg == object.__class__.__name__:
                count = count + 1
        print(count)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
