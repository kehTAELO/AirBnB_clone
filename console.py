#!/usr/bin/python3

import cmd

"""Defines the HBnB console"""
class HBNBCommand(cmd.Cmd):
     """
    this will define the commandinterpreter of HBNB.

    """

     prompt = "(hbnb)"

     def emptyline(self):
        """this will Do nothing after it received an empty line """
        pass
     
     def do_quit(self, arg):
        """This is the quit command which will exit the program"""
        return True

     def do_EOF(self, arg):
        """this will end the program"""
        print("")
        return True
     
if __name__ == '__main__':
    HBNBCommand().cmdloop()
