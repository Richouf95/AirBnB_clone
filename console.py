#!/usr/bin/python3
"""
    This is the HBnB console module
"""


import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import re
from shlex import split


class HBNBCommand(cmd.Cmd):
    """
        This is my console interpreter
    """

    prompt = "(hbnb) "
    list_available_class = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_quit(self, arg):
        """
            Quit the console with command `quit`
        """
        return True

    def do_EOF(self, arg):
        """
            Quit the console with command `EOF`
        """
        print()
        return True

    def emptyline(self):
        """
            Empty command line
        """
        pass

    def default(self, arg):
        """
            Default action when command is invalid
        """
        allow_args = {
            "all": self.do_all,
            "show": self.do_show,
            "update": self.do_update,
            "destroy": self.do_destroy,
            "count": self.do_count
        }

    def do_create(self, arg):
        """
            Create new instance of a class
        """
        command_args = arg.split()
        if len(command_args) == 0:
            print("** class name missing **")
        elif command_args[0] not in HBNBCommand.list_available_class:
            print("** class doesn't exist **")
        else:
            className = eval(command_args[0])
            print(className().id)
            storage.save()

    def do_show(self, arg):
        """
            Prints the string representation of an instance
        """
        command_args = arg.split()
        data = storage.all()

        if len(command_args) == 0:
            print("** class name missing **")
        elif command_args[0] not in HBNBCommand.list_available_class:
            print("** class doesn't exist **")
        elif len(command_args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(command_args[0], command_args[1]) not in data:
            print("** no instance found **")
        else:
            print(data["{}.{}".format(command_args[0], command_args[1])])

    def do_destroy(self, arg):
        """
            Delete an instance based on the class name and id
        """
        command_args = arg.split()
        data = storage.all()

        if len(command_args) == 0:
            print("** class name missing **")
        elif command_args[0] not in HBNBCommand.list_available_class:
            print("** class doesn't exist **")
        elif len(command_args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(command_args[0], command_args[1]) not in data:
            print("** no instance found **")
        else:
            del data["{}.{}".format(command_args[0], command_args[1])]
            storage.save()

    def do_all(self, arg):
        """
            Prints all string representation of all instances
            based or not on the class name
        """
        command_args = arg.split()
        data = storage.all()
        all_instances = []

        if len(command_args) == 0:
            for x in data.values():
                all_instances.append(x.__str__())
        else:
            if command_args[0] in HBNBCommand.list_available_class:
                for x in data.values():
                    if x.__class__.__name__ == command_args[0]:
                        all_instances.append(x.__str__())
            else:
                print("** class doesn't exist **")
                return False
        print(all_instances)

    def do_update(self, arg):
        """
            Updates an instance based on the class name and id
            by adding or updating attribute
        """
        command_args = arg.split()
        args_length = len(command_args)
        data = storage.all()
        unauthorized = ["id", "created_at", "updated_at"]

        if args_length == 0:
            print("** class name missing **")
            return False
        elif command_args[0] not in HBNBCommand.list_available_class:
            print("** class doesn't exist **")
            return False

        className = command_args[0]

        if args_length < 2:
            print("** instance id missing **")
            return False
        elif "{}.{}".format(className, command_args[1]) not in data.keys():
            print("** no instance found **")
            return False

        instance_id = command_args[1]

        key = "{}.{}".format(className, instance_id)

        if args_length < 3:
            print("** attribute name missing **")
            return False

        if args_length < 4 and args_length == 3:
            try:
                type(eval(command_args[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        instance_target = data[key]
        attribute = command_args[2]

        if attribute in unauthorized:
            return False

        if args_length == 4:
            value = command_args[3]
            if attribute in instance_target.__class__.__dict__.keys():
                parse_to = type(instance_target.__class__.__dict__[attribute])
                instance_target.__dict__[attribute] = parse_to(value)
            else:
                instance_target.__dict__[attribute] = value
        elif type(eval(attribute)) == dict:
            pass

        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
