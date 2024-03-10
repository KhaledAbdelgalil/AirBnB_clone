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
    """Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    __foundClasses = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
    }

    def default(self, line):
        """Default behavior for cmd module when input is invalid"""
        args = re.findall(r"(.*)\.(.*)\((.*)\)", line)
        if args and len(args[0]) >= 2:
            foundFunctions = {
                "all": self.do_all,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "count": self.do_count,
                "update": self.do_update,
            }
            class_name = args[0][0]
            method_name = args[0][1]
            rest_args = ""
            if len(args[0]) > 2:
                if (
                    method_name == "update"
                    and args[0][2] != ""
                    and args[0][2][-1] == "}"
                ):
                    id_dict_list = args[0][2].split(",", 1)
                    updated_id, updated_dict = id_dict_list
                    updated_dict = loads(updated_dict.replace("'", '"'))
                    for k, v in updated_dict.items():
                        if type(v) is str:
                            v = f'"{v}"'
                        arg = (
                            str(class_name)
                            + " "
                            + str(updated_id)
                            + " "
                            + str(k)
                            + " "
                            + str(v)
                        )
                        if self.do_update(arg) is False:
                            break
                    return
                else:
                    rest_args = args[0][2].split(",")
            if method_name in foundFunctions.keys():
                arg = str(class_name)
                if rest_args != "":
                    for element in rest_args:
                        arg = arg + " " + str(element)
                arg = arg.rstrip(" ")
                return foundFunctions[method_name](arg)

        print("*** Unknown syntax: {}".format(line))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        return

    def help_quit(self):
        """help of quit"""
        print("Quit command to exit the program.\n")

    def help_EOF(self):
        """"help of EOF"""
        print("EOF\n")

    def do_create(self, arg):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        if len(arg) == 0:
            print("** class name missing **")
        elif arg in self.__foundClasses:
            obj = self.__foundClasses[arg]()
            print(obj.id)
            storage.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
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
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id."""
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
        """"bring instances based on class_type from storage file"""
        objects_list = []
        allObjects = storage.all().values()
        for object in allObjects:
            if class_type is None or class_type == object.__class__.__name__:
                objects_list.append(object.__str__())
        print(objects_list)

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        if arg == "":
            self.bring_classes()
        elif arg not in self.__foundClasses:
            print("** class doesn't exist **")
        else:
            self.bring_classes(arg)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
        <class>.update(<id>, <attribute_name>, <attribute_value>) or
        <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return False
        else:
            if args[0] in self.__foundClasses:
                if len(args) < 2:
                    print("** instance id missing **")
                    return False
                else:
                    allObjects = storage.all()
                    object_key = "{}.{}".format(args[0], args[1])
                    if object_key in allObjects:
                        obj = allObjects[object_key]
                        if len(args) < 3:
                            print("** attribute name missing **")
                            return False
                        elif len(args) < 4:
                            print("** value missing **")
                            return False
                        else:
                            obj.__dict__[args[2]] = loads(
                                args[3].replace("'", '"')
                            )
                            obj.save()
                    else:
                        print("** no instance found **")
                        return False
            else:
                print("** class doesn't exist **")
                return False

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        if arg not in self.__foundClasses:
            print("** class doesn't exist **")
            return
        count = 0
        allObjects = storage.all().values()
        for object in allObjects:
            if arg == object.__class__.__name__:
                count = count + 1
        print(count)

    def help_all(self):
        """help of all"""
        print(
            "Prints the string representation of "
            "all instances based or not on the class name"
        )

    def help_update(self):
        """help of update"""
        print("Updates an instance based on the class name " "and id")

    def help_show(self):
        """help of show"""
        print(
            "Prints the string representation of "
            "an instance based on class name and id"
        )

    def help_destroy(self):
        """help of destroy"""
        print("Deletes an instance based on class name and id")

    def help_create(self):
        """help of create"""
        print("Creates a new instance and prints the id")

    def help_count(self):
        """help of count"""
        print("counts the number of instances of a class or all classes")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
