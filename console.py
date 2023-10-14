#!/usr/bin/python3
"""
This module defines the HBNBCommand class
"""

import cmd
import models
from models import storage
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    HBNB Command Line Interface
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit the command line interface
        """
        return True

    def do_EOF(self, arg):
        """
        Exit/Quit
        """
        return True

    def do_emptyline(self):
        """
        Empty line
        """
        pass

    def do_help(self, arg):
        """
        Display help manual
        """
        cmd.Cmd.do_help(self, arg)

    def do_create(self, arg):
        """
        Create a new instance
        """
        if not arg:
            print("** class name missing **")
            return

        try:
            class_name = arg.split()[0]
            new_instance = eval(class_name)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Show string representation of an instance
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        class_name = args[0]
        key = "{}.{}".format(class_name, instance_id)
        if key in models.storage.all():
            print(models.storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Delete an instance based on class name and id
        """
        classes = [
            "BaseModel"]
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        class_name = args[0]
        key = "{}.{}".format(class_name, instance_id)
        if key in models.storage.all():
            del models.storage.all()[key]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Print all instances of a class or all classes
        """
        classes = [
            "BaseModel"]
        args = arg.split()
        obj_list = []
        if not arg:
            for obj in moedls.storage.all().values():
                obj_list.append(str(obj))
            print(obj_list)
            return

        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        for key, obj in models.storage.all().items():
            class_name = key.split(".")[0]
            if class_name == args[0]:
                obj_list.append(str(obj))
        print(obj_list)

    def do_update(self, arg):
        """
        Update an instance based on the class name and ID
        """
        classes = [
            "BaseModel"]
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        class_name = args[0]
        key = "{}.{}".format(class_name, instance_id)
        if key in models.storage.all():
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return

            attribute_name = args[2]
            attribute_value = args[3]
            instance = models.storage.all()[key]
            setattr(instance, attribute_name, attribute_value)
            instance.save()
        else:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
