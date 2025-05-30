#!/usr/bin/!
""" Use the program for execute for this script """
class MyList(list):
    """ Custom list class that inherits from the built-in list. """
    def print_sorted(self):
        """Prints the list in acsending order (without modifying the original list). """
        print(sorted(self))
        """ this command can show the list """
