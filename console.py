#!/usr/bin/python3

import cmd
import inspect
import models
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
        elif arg == 'BaseModel':
            b = BaseModel()
            b.save()
            print(b.id)
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        ls_arg = arg.split(' ')
        if ls_arg[0] not in ['BaseModel']:
            print("** class doesn't exist **")        
        elif len(ls_arg) is 1:
            print('** instance id missing **')
        else:
            key = '.'.join(ls_arg)
            if key not in models.storage.all():
                print('** no instance found **')
            else:
                del models.storage.all()[key]
                models.storage.save()

    def do_show(self,arg):
        if not arg:
            print("** class name missing **")
            return
        ls_arg = arg.split(' ')
        if ls_arg[0] not in ['BaseModel']:
            print("** class doesn't exist **")        
        elif len(ls_arg) is 1:
            print('** instance id missing **')
        else:
            key = '.'.join(ls_arg)
            if key not in models.storage.all():
                print('** no instance found **')
            else:
                print(models.storage.all()[key])

    def do_all(self, arg):
        if not arg:
            print("** class name missing **")
            return
        ls_arg = arg.split(' ')
        if ls_arg[0] not in ['BaseModel']:
            print("** class doesn't exist **")
        else:
            for key in models.storage.all():
                obj = models.storage.all()[key]
                print(obj)

    def do_update(self, arg):
        ls_arg = arg.split(' ')
        num_arg = len(arg)
        if not ls_arg:
            print("** class name missing **")
            return
        if ls_arg[0] not in ['BaseModel']:
            print("** class doesn't exist **")
        elif num_arg is 1:
            print("** instance id missing **")
        elif num_arg < 3:
            print("** attribute name missing **")
        elif ls_arg[2] in ['id', 'created_at', 'update_at']:
            pass
        elif num_arg < 4:
            print('** value missing **')
        else:
            model = models.storage.all()['.'.join(ls_arg[:2])]
            ls_arg[3] = ls_arg[3].strip('\"')
            if ls_arg[3].isdigit():
                ls_arg[3] = int(ls_arg[3])
            elif ls_arg.isdecimal():
                ls_arg[3] = float(ls_arg[3])
            setattr(model, ls_arg[2], ls_arg[3])

    def emptyline(self):
        """Called when an empty line is entered"""
        pass

    def help(self, arg):
        """Help command to describe the function\n"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
