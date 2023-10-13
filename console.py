#!/usr/bin/python3
"""
Console module for handling the command line interface.
"""

from models.base_model import BaseModel
import cmd
from models import storage
from models.user import User


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_create(self, args):
        """Create a new instance of User"""
        if not args:
            print("** class name missing **")
        elif args != "User":
            print("** class doesn't exist **")
        else:
            new_user = User()
            new_user.save()
            print(new_user.id)

    def do_show(self, args):
        """Show the string representation of an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
        else:
            arg_list = args.split()
            if arg_list[0] != "User":
                print("** class doesn't exist **")
            elif len(arg_list) < 2:
                print("** instance id missing **")
            else:
                user_id = arg_list[1]
                key = "User." + user_id
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, args):
        """Delete an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
        else:
            arg_list = args.split()
            if arg_list[0] != "User":
                print("** class doesn't exist **")
            elif len(arg_list) < 2:
                print("** instance id missing **")
            else:
                user_id = arg_list[1]
                key = "User." + user_id
                if key in storage.all():
                    del storage.all()[key]
                    models.storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, args):
        """Print all string representation of all instances based or not on the class name"""
        arg_list = args.split()
        if not args or arg_list[0] == "User":
            user_list = []
            for value in storage.all().values():
                if arg_list[0] == "User" or value.__class__.__name__ == "User":
                    user_list.append(str(value))
            print(user_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """Update an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
        else:
            arg_list = args.split()
            if arg_list[0] != "User":
                print("** class doesn't exist **")
            elif len(arg_list) < 2:
                print("** instance id missing **")
            elif len(arg_list) < 3:
                print("** attribute name missing **")
            elif len(arg_list) < 4:
                print("** value missing **")
            else:
                
                if key in storage.all():
                    setattr(models.storage.all()[key], arg_list[2], arg_list[3])
                    models.storage.save()
                else:
                    print("** no instance found **")

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
