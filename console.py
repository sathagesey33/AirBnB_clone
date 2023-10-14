#!/usr/bin/python3
"""
    CMD entrypoint program
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program.
        """
        print("EOF")
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

    def create(self, arg):
        """
        Create a new instance of BaseModel, save it, and print its id.
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance.
        Usage: show <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        try:
            instances = storage.all()
            key = "{}.{}".format(args[0], args[1])
            print(instances[key])
        except KeyError:
            print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        Usage: destroy <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        try:
            instances = storage.all()
            key = "{}.{}".format(args[0], args[1])
            del instances[key]
            storage.save()
        except KeyError:
            print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """
            Prints all string representation of instances.
            Usage: all [optional class name]
        """
        args = arg.split()
        if args and args[0]:
            try:
                instances = storage.all()
                filtered_instances = [str(val) for val in instances.values()
                                      if val.__class__.__name__ == args[0]]
                if not filtered_instances:
                    print("** class doesn't exist **")
                else:
                    print(filtered_instances)
            except NameError:
                print("** class doesn't exist **")
        else:
            instances = storage.all()
            print([str(val) for val in instances.values()])

    def do_update(self, arg):
        """
        Updates an instance based on the class and id by updating an attribute
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        try:
            instances = storage.all()
            key = "{}.{}".format(args[0], args[1])
            instance = instances.get(key)
            if instance:
                setattr(instance, args[2], args[3].strip('\"'))
                storage.save()
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_help(self, arg):
        """
        Show help message.
        """
        cmd.Cmd.do_help(self, arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
