#!/usr/bin/python3

"""
This is a module for the Console class
"""

import cmd
import inspect
import models
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    This is a class Command Prompt
    """
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """
        Function that has EOF command to exit the program\n
        """
        return True

    def count_instance_class(self, arg):
        """
        Function that counts all instances of a specific class
        """
        count = 0
        ls_arg = arg.split(' ')
        for key in models.storage.all():
                obj = models.storage.all()[key]
                if obj.__class__.__name__ == ls_arg[0]:
                    count = count + 1
        return count

    def do_BaseModel(self, arg):
        """
        Function that does all advanced tasks for class BaseModel
        """
        if arg == ".all()":
            self.do_all("BaseModel")
        elif arg == ".count()":
            counter = self.count_instance_class("BaseModel")
            print(counter)
        elif arg.startswith(".show("):
            ls_arg = arg.split('.')
            split = ls_arg[1].split('(', 1)
            string = split[1][:-1]
            self.do_show("BaseModel {}".format(string))

    def do_User(self, arg):
        """
        Function that does all advanced tasks for class User
        """
        if arg == ".all()":
            self.do_all("User")
        elif arg == ".count()":
            counter = self.count_instance_class("User")
            print(counter)
        elif arg.startswith(".show("):
            ls_arg = arg.split('.')
            split = ls_arg[1].split('(', 1)
            string = split[1][:-1]
            self.do_show("User {}".format(string))

    def do_State(self, arg):
        """
        Function that does all advanced tasks for class State
        """
        if arg == ".all()":
            self.do_all("State")
        elif arg == ".count()":
            counter = self.count_instance_class("State")
            print(counter)
        elif arg.startswith(".show("):
            ls_arg = arg.split('.')
            split = ls_arg[1].split('(', 1)
            string = split[1][:-1]
            self.do_show("State {}".format(string))

    def do_City(self, arg):
        """
        Function that does all advanced tasks for class City
        """
        if arg == ".all()":
            self.do_all("City")
        elif arg == ".count()":
            counter = self.count_instance_class("City")
            print(counter)
        elif arg.startswith(".show("):
            ls_arg = arg.split('.')
            split = ls_arg[1].split('(', 1)
            string = split[1][:-1]
            self.do_show("City {}".format(string))

    def do_Amenity(self, arg):
        """
        Function that does all advanced tasks for class Amenity
        """
        if arg == ".all()":
            self.do_all("Amenity")
        elif arg == ".count()":
            counter = self.count_instance_class("Amenity")
            print(counter)
        elif arg.startswith(".show("):
            ls_arg = arg.split('.')
            split = ls_arg[1].split('(', 1)
            string = split[1][:-1]
            self.do_show("Amenity {}".format(string))

    def do_Place(self, arg):
        """
        Function that does all advanced tasks for class Place
        """
        if arg == ".all()":
            self.do_all("Place")
        elif arg == ".count()":
            counter = self.count_instance_class("Place")
            print(counter)
        elif arg.startswith(".show("):
            ls_arg = arg.split('.')
            split = ls_arg[1].split('(', 1)
            string = split[1][:-1]
            self.do_show("Place {}".format(string))

    def do_Review(self, arg):
        """
        Function that does all advanced tasks for class Review
        """
        if arg == ".all()":
            self.do_all("Review")
        elif arg == ".count()":
            counter = self.count_instance_class("Review")
            print(counter)
        elif arg.startswith(".show("):
            ls_arg = arg.split('.')
            split = ls_arg[1].split('(', 1)
            string = split[1][:-1]
            self.do_show("Review {}".format(string))

    def do_quit(self, arg):
        """
        Function that has Quit command to exit the program\n
        """
        return True

    def do_create(self, arg):
        """
        Function that has Create command to create new instances
        of Classes available in the database\n
        """
        if len(arg) < 1:
            print("** class name missing **")
        elif arg == 'BaseModel':
            b = BaseModel()
            b.save()
            print(b.id)
        elif arg == 'User':
            u = User()
            u.save()
            print(u.id)
        elif arg == 'State':
            s = State()
            s.save()
            print(s.id)
        elif arg == 'City':
            c = City()
            c.save()
            print(c.id)
        elif arg == 'Amenity':
            a = Amenity()
            a.save()
            print(a.id)
        elif arg == 'Place':
            p = Place()
            p.save()
            print(p.id)
        elif arg == 'Review':
            r = Review()
            r.save()
            print(r.id)
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """
        Function that has Delete command to delete an instance
        based on the class name and id\n
        """
        if not arg:
            print("** class name missing **")
            return
        ls_arg = arg.split(' ')
        if ls_arg[0] not in ['BaseModel', 'User', 'State',
                             'City', 'Amenity', 'Place', 'Review']:
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

    def do_show(self, arg):
        """
        Function that has Show command to show an instance
        based on the class name and id\n
        """
        if not arg:
            print("** class name missing **")
            return
        ls_arg = shlex.split(arg)
        if ls_arg[0] not in ['BaseModel', 'User', 'State',
                             'City', 'Amenity', 'Place', 'Review']:
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
        """
        Function that has All command to show all instances
        based on the class name\n
        """
        if len(arg) == 0:
            for key in models.storage.all():
                obj = models.storage.all()[key]
                print(obj)
            return
        if not arg:
            print("** class name missing **")
            return
        ls_arg = arg.split(' ')
        if ls_arg[0] not in ['BaseModel', 'User', 'State',
                             'City', 'Amenity', 'Place', 'Review']:
            print("** class doesn't exist **")
        else:
            for key in models.storage.all():
                obj = models.storage.all()[key]
                if obj.__class__.__name__ == ls_arg[0]:
                    print(obj)

    def do_update(self, arg):
        """
        Function that has Update command to update already
        existing instances in a class
        """
        ls_arg = arg.split(' ')
        num_arg = len(arg)
        if not arg:
            print("** class name missing **")
            return
        if ls_arg[0] not in ['BaseModel', 'User', 'State',
                             'City', 'Amenity', 'Place', 'Review']:
            print("** class doesn't exist **")
            return
        elif len(ls_arg) is 1:
            print("** instance id missing **")
            return
        check_id = models.storage.all()
        key = ls_arg[0] + "." + ls_arg[1]
        if key not in check_id:
            print("** no instance found **")
            return
        elif len(ls_arg) is 2:
            print("** attribute name missing **")
            return
        elif len(ls_arg) is 3:
            print('** value missing **')
            return
        else:
            model = models.storage.all()['.'.join(ls_arg[:2])]
            ls_arg[3] = ls_arg[3].strip('\"')
            if ls_arg[3].isdigit():
                ls_arg[3] = int(ls_arg[3])
            setattr(model, ls_arg[2], ls_arg[3])

    def emptyline(self):
        """
        Function that is called when an empty line is entered\n
        """
        pass

    def help(self, arg):
        """
        Function that is called when Help command is entered
        to describe the function given\n
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
