#!/usr/bin/python3
"""
Defines the Console class,
which serves as the entry point of the Airbnb Project.
"""

import cmd
from models.base_model import BaseModel
from models import storage
from json import loads


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    __foundClasses = {"BaseModel": BaseModel}

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

    def do_all(self, arg):
        if arg not in self.__foundClasses:
            print("** class doesn't exist **")
        else:
            objects_list = []
            allObjects = storage.all().values()
            for object in allObjects:
                objects_list.append(object.__str__())
            print(objects_list)

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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
