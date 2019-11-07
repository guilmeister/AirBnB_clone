#!/usr/bin/python3

import cmd

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

    def help(self, arg):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
