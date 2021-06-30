#!/usr/bin/python3
"""
Module that contains the entry point of the command interpreter
"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
import cmd
import inspect
from models.engine.file_storage import FileStorage
from models.place import Place
from models.review import Review
from models import storage
from models.state import State
from models.user import User
import re
import sys


class HBNBCommand(cmd.Cmd):
    """
    Command processor
    """

    prompt = '(hbnb) '

    @staticmethod
    def check_str_to_int(c):
        """
        Check if a variable is convertible to int or not and returns it.
        """
        try:
            n = int(c)
            return n
        except:
            return c

    @staticmethod
    def check_class(x):
        """Check if x is a class."""
        try:
            r = inspect.isclass(eval(x))
            return r
        except:
            return False

    def do_EOF(self, line):
        """
        End-of-file marker
        """
        print("")
        return True

    def do_quit(self, line):
        """
        Quit the command line
        """
        return True

    def emptyline(self):
        """
        Called when an empty line is entered in response to the prompt.
        """
        pass

    def do_create(self, line):
        """
        Create an instance of BaseModel
        Usage: create <class Name>
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif (HBNBCommand.check_class(args[0])):
            if not issubclass(eval(args[0]), BaseModel):
                print("** class doesn't exist **")
            else:
                my_class = eval(args[0])()
                my_class.save()
                print("{}".format(my_class.id))
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """
        Prints the string representation of an instance based on the class name
        and id.
        Usage: show <class Name> <id>
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif (HBNBCommand.check_class(args[0])):
            if not issubclass(eval(args[0]), BaseModel):
                print("** class doesn't exist **")
            else:
                if len(args) == 1:
                    print("** instance id missing **")
                else:
                    key = args[0] + "." + args[1]
                    objs = storage.all()
                    if key in objs:
                        print(objs[key])
                    else:
                        print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        Usage: Destroy <class Name> <id>
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif (HBNBCommand.check_class(args[0])):
            if not issubclass(eval(args[0]), BaseModel):
                print("** class doesn't exist **")
            else:
                if len(args) == 1:
                    print("** instance id missing **")
                else:
                    key = args[0] + "." + args[1]
                    objects = storage.all()
                    if key in objects:
                        del objects[key]
                        storage.save()
                    else:
                        print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, line):
        """
        Prints all string representation of all instances based or not on
        the class name.
        Usage: all <class Name> or all
        """
        args = line.split()
        objs = []
        if len(args) == 0:
            for k, v in storage.all().items():
                objs.append(str(v))
            print(objs)
        elif (HBNBCommand.check_class(args[0])):
            if not issubclass(eval(args[0]), BaseModel):
                print("** class doesn't exist **")
            else:
                for k, v in storage.all().items():
                    obj_keys = k.split('.')
                    if obj_keys[0] == args[0]:
                        objs.append(str(v))
                print(objs)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif (HBNBCommand.check_class(args[0])):
            if not issubclass(eval(args[0]), BaseModel):
                print("** class doesn't exist **")
            else:
                if len(args) == 1:
                    print("** instance id missing **")
                else:
                    key = args[0] + "." + args[1]
                    objects = storage.all()
                    if key in objects:
                        if len(args) == 2:
                            print('** attribute name missing **')
                        else:
                            line2 = line.split('"')
                            if len(line2) == 1:
                                print("** value missing **")
                            else:
                                setattr(
                                        objects[key],
                                        str(args[2]),
                                        str(line2[1])
                                        )
                                storage.save()
                    else:
                        print("** no instance found **")
        else:
            print("** class doesn't exist **")

    @staticmethod
    def handle_def_all(line, cls_name):
        """
        Handles the default <class name>.all() console function.
        """
        objs = []
        for k, v in storage.all().items():
            if (k.split('.')[0] == cls_name):
                objs.append(str(v))
        if len(objs) > 0:
            print('[', end='')
            for i in range(len(objs)):
                print(objs[i], end='')
                if i < len(objs) - 1:
                    print(', ', end='')
                else:
                    print(']')
        else:
            print('[]')

    @staticmethod
    def handle_def_count(line, cls_name):
        """
        Handles the default <class name>.count() console function.
        """
        count = 0
        objs = []
        for k, v in storage.all().items():
            if (k.split('.')[0] == cls_name):
                count = count + 1
        print(count)

    @staticmethod
    def handle_def_show(cls_name, id):
        """
        Handles the default <class name>.show(<id>) console function.
        """
        objs = storage.all()
        key = cls_name + '.' + id
        if key in objs:
            print(objs[key])
        else:
            print("** no instance found **")

    @staticmethod
    def handle_def_destroy(cls_name, id):
        """
        Handles the default <class name>.destory(<id>) console function.
        """
        objs = storage.all()
        key = cls_name + '.' + id
        if key in objs:
            del objs[key]
            storage.save()
        else:
            print("** no instance found **")

    @staticmethod
    def handle_def_update(cls_name, id, attr, value):
        """
        Handles the default <class name>.destory(<id>) console function.
        """
        objs = storage.all()
        key = cls_name + '.' + id
        if key in objs:
            setattr(
                objs[key],
                attr,
                HBNBCommand.check_str_to_int(value)
                )
            storage.save()
        else:
            print("** no instance found **")

    @staticmethod
    def handle_def_update_with_dict(cls_name, id, d):
        """
        Handles the <class name>.update(<id>, <dictionary representation>)
        console function.
        """
        objs = storage.all()
        key = cls_name + '.' + id
        if key in objs:
            for k, v in d.items():
                setattr(
                    objs[key],
                    k,
                    HBNBCommand.check_str_to_int(v)
                )
            storage.save()
        else:
            print("** no instance found **")

    def default(self, line):
        """
        Called on an input line when the command prefix is not recognized.
        the commands that are handled here are:
        <class name>.all()
        """
        args = line.split('.')
        cls_name = ""
        if args[0] is not None:
            cls_name = args[0]
        if args[1] is not None:
            if (args[1] == 'all()'):
                HBNBCommand.handle_def_all(line, cls_name)
            elif (args[1] == 'count()'):
                HBNBCommand.handle_def_count(line, cls_name)
            else:
                cmds = re.split('\(|\"|\)', args[1])
                cmds = list(filter(lambda s: s != '', cmds))
                if cmds[0] == 'show':
                    HBNBCommand.handle_def_show(cls_name, cmds[1])
                elif cmds[0] == 'destroy':
                    HBNBCommand.handle_def_destroy(cls_name, cmds[1])
                elif cmds[0] == 'update':
                    cmds = re.split('\(|\"|\)|\{|\'|\}|: |:|, ', args[1])
                    cmds = list(filter(lambda s: s != '' and s != ' ', cmds))
                    cmds = list(filter(lambda s: s != ', ', cmds))
                    if (len(cmds) == 4):
                        HBNBCommand.handle_def_update(
                            cls_name, cmds[1], cmds[2], cmds[3]
                        )
                    else:
                        tab = cmds[2:]
                        d = {}
                        for i in range(0, len(tab), 2):
                            d[tab[i]] = tab[i + 1]
                        HBNBCommand.handle_def_update_with_dict(
                            cls_name, cmds[1], d
                        )


if __name__ == '__main__':
    HBNBCommand().cmdloop()
