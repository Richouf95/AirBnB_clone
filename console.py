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

        match = re.search(r"\.", arg)
        if match is None:
            print("*** Unknown syntax: {}".format(arg))
            return False

        args_splited = [arg[:match.span()[0]], arg[match.span()[1]:]]

        match = re.search(r"\((.*?)\)", args_splited[1])
        if match is not None:
            command = [args_splited[1][:match.span()[0]], match.group()[1:-1]]
            if command[0] in allow_args.keys():
                run_command = allow_args[command[0].lower()](
                        "{} {}".format(args_splited[0], command[1])
                        )
                return run_command

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

        is_object = re.search(r"\{(.*?)\}", arg)
        if is_object is not None:
            arg_split = split(arg[:is_object.span()[0]])
            command_args = [i.strip(",") for i in arg_split]
            command_args.append(is_object.group())
        else:
            command_args = [i.strip(",") for i in split(arg)]

        args_length = len(command_args)
        data = storage.all()
        unauthorized = ["id", "created_at", "updated_at"]

        if args_length == 0:
            print("** class name missing **")
            return False
        elif args_length == 1:
            if command_args[0] not in HBNBCommand.list_available_class:
                print("** class doesn't exist **")
                return False
            else:
                print("** instance id missing **")
                return False
        elif args_length == 2:
            chack_intance = "{}.{}".format(command_args[0], command_args[1])
            if chack_intance not in data.keys():
                print("** no instance found **")
            else:
                print("** attribute name missing **")
            return False
        elif args_length == 3:
            try:
                type(eval(command_args[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        className = command_args[0]
        instance_id = command_args[1]
        attribute = command_args[2]

        if attribute in unauthorized:
            return False

        if args_length == 4:
            instance_target = data["{}.{}".format(className, instance_id)]
            if attribute in instance_target.__class__.__dict__.keys():
                typeOf = type(instance_target.__class__.__dict__[attribute])
                instance_target.__dict__[attribute] = typeOf(command_args[3])
            else:
                instance_target.__dict__[attribute] = command_args[3]
        else:
            if type(eval(attribute)) == dict:
                the_instance = data["{}.{}".format(className, instance_id)]
                for key, value in eval(attribute).items():
                    if key in the_instance.__class__.__dict__.keys():
                        types = {str, int, float}
                        if type(the_instance.__class__.__dict__[key]) in types:
                            typeOf = type(the_instance.__class__.__dict__[key])
                            the_instance.__dict__[key] = typeOf(value)
                    else:
                        the_instance.__dict__[key] = value

        storage.save()

    def do_count(self, arg):
        """
            Count instances of a class
        """
        command_args = arg.split()
        data = storage.all()
        count = 0

        for x in data.values():
            if command_args[0] == x.__class__.__name__:
                count += 1

        print(count)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
