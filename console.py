#!/usr/bin/python3

import cmd
import inspect
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """EOF command to exit the program\n"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_create(self, arg):
        """Create command to create new instance of BaseModel\n"""
        if len(arg) < 1:
            print("** class name missing **")
        if not arg in inspect.getmembers(BaseModel):
            print("** class doesn't exist **")

    def emptyline(self):
        """Called when an empty line is entered"""
        pass

    def help(self, arg):
        """Help command to describe the function\n"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
