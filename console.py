#!/usr/bin/python3
""" Command Interpreter """
import cmd
import sys
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ HBNBCommand class """
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ""

    __classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
    }

    def preloop(self):
        """ Prints if isatty is false """
        if not sys.__stdin__.isatty():
            print("(hbnb)")

    def postcmd(self, stop, line):
        """ Prints if isatty is false """
        if not sys.__stdin__.isatty():
            print("(hbnb) ", end="")
        return stop

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """ EOF command to exit the program """
        print()
        exit()

    def emptyline(self):
        """ An empty line + ENTER shouldn't execute anything """
        pass

    def do_create(self, arg):
        """
            Creates a new instance of BaseModel,
            saves it (to the JSON file) and prints the id
            Usage: create <class name> <param 1> <param 2> <param 3>...
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            my_model = HBNBCommand.__classes[args[0]]()
            for param in args[1:]:
                try:
                    key, value = param.split("=")
                    # Replace "_" by " " for string type
                    if value == '"':
                        value = value.replace('_', ' ')
                    # convert value to int, float or keep it string
                    try:
                        value = int(value)
                    except ValueError:
                        try:
                            value = float(value)
                        except ValueError:
                            value = str(value)
                    setattr(my_model, key, value)
                except:
                    pass

            my_model.save()
            print(my_model.id)

    def do_show(self, arg):
        """
             Prints the string representation of an instance,
             based on the class name and id.
             Ex: $ show BaseModel 1234-1234-1234.
             Usage: show <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
            Deletes an instance based on the class name and id
            (save the change into the JSON file).
            Usage: destroy <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
            Prints all string representation of all instances
            based or not on the class name.
            Usage: all [class name]
        """
        args = arg.split()
        objects = storage.all()
        if not args:
            result = []
            for obj in objects.values():
                result.append(str(obj))
            print(result)
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            if class_name in HBNBCommand.__classes:
                class_objs = []
                for key, obj in objects.items():
                    if key.startswith(class_name + "."):
                        class_objs.append(str(obj))
                print(class_objs)
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """
            Updates an instance based on the class name and id,
            by adding or updating attribute.
            Usage: update <class name> <id> \
                <attribute name> "<attribute value>"
        """
        objects = storage.all()
        args = shlex.split(arg)

        if len(args) == 0:
            print("** class name missing **")
            return

        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        key_find = args[0] + '.' + args[1]
        obj = objects.get(key_find, None)

        if not obj:
            print("** no instance found **")
            return

        if len(args) == 2:
            print("** attribute name missing **")
            return

        if len(args) == 3:
            print("** value missing **")
            return

        setattr(obj, args[2], args[3].lstrip('"').rstrip('"'))
        storage.save()

    def default(self, line):
        """
            Method called on input when the command prefix is not recognized.
            In this case it will be used to handle:
                - <class name>.all()
                - <class name>.count()
                - <class name>.show(<id>)
        """
        split_line = line.split(".")
        if len(split_line) != 2:
            print("** invalid command **")

        cls_name = split_line[0]
        meth_arg = split_line[1].split("(")
        if len(meth_arg) != 2:
            print("** invalid command **")

        method = meth_arg[0]
        arg = meth_arg[1].strip(")")
        if method == "all":
            self.do_all(cls_name)
        elif method == "count":
            self.do_count(cls_name)
        elif method == "show":
            self.do_show(cls_name + " " + arg)
        elif method == "destroy":
            self.do_destroy(cls_name + " " + arg)

    def do_count(self, arg):
        """
            Prints numbers of instances based on the class name.
            Usage: <class name>.count()
        """
        class_name = arg
        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        objects = storage.all()
        count = 0
        for key in objects.keys():
            if key.startswith(class_name + "."):
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
