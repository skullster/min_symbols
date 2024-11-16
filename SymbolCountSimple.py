# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 11:29:07 2023

@author: jfscu
"""

""" Symbol count """
""" - find the minimum number of symbols for different bases for a number in a * b + remainder format """
""" - what does minimum number of symbols mean? """
"""   base number-1 will always be 3 symbols for example 1 * base + 1 ... """

""" so 3 tests: """
    
"""    1 : symbol counts within bases """
"""    2 : symbol counts in binary within bases ie each symbol has the maximum binary symbols for the bases """
"""    3 : min binary representation for each symbol AND what base that fits into! """
import Base as B
import NumberList as NL
import MinimumTracker as MT
import math

class SymbolCountSimple(object):
    def __init__(self, number):
        self.number = number
        self.current_base = -1
        self.__get_base_range()
        self.number_list_obj = NL.NumberList(number)
        self.tracker_obj = MT.MinimumTracker()
        self.number_list_obj.create_number_list()
        self.symbol_count_list = []
        self.file_obj = None

    """ Private method """
    """ Gets the minimum and maximum bases for the given number """
    def __get_base_range(self):
        self.max_base = self.number
        self.min_base = 2
        
    """ Get the symbol count ranges for the given base """
    """ Foreach base get the ranges for each symbol count, """
    """ starting at 1 through to the max possible symbols """ 
    def __symbol_count_for_bases(self):
        # Set up base object
        base_idx = self.min_base
        base_obj = B.Base(base_idx)

        # Init min symbol count 
        min_symbol_count = self.max_base * 2
        while base_idx <= self.max_base :
            base_obj.convert_number( self.number )
            number_symbol_count = base_obj.get_symbol_count()
            # Min symbol count is the number of symbols representing the number + the number of symbols in the base
            cur_min_symbol_count = number_symbol_count + base_idx
            # Change the min symbol count?
            if cur_min_symbol_count < min_symbol_count :
                # Yep ...
                min_symbol_count < cur_min_symbol_count

            # TODO: setup for MinimumTracker.py
            self.symbol_count_list.append([base_idx,number_symbol_count])
            base_idx += 1
            base_obj.set_new_base(base_idx)
            
    def __get_symbol_count(self):
        """ Base range list should be set up prior to calling this """
        """ Get base symbol data """
        for number_obj in self.number_list_obj.number_list :
            self.__get_base_symbol_data(number_obj)
                                 
    def print_symbols_to_file(self):
        """ Use files for now - see how it goes """
        """ TODO : use MongoDB - seems a likely candidate """
        """ TODO : create a class that can be used both for MongoDB and file operations """
        file_name = str(self.number) + '.txt'
        self.file_obj = open( file_name, 'w' )
        self.__get_base_symbol_data(0)
        self.file_obj.close()
        
    def set_number(self, number):
        self.number = number
        self.__get_base_range()
                
    def print_list(self):
        print("Number %d, min base %d, max base %d" % (self.number, self.min_base, self.max_base))

if __name__ == "__main__":
    aSymbolObj = SymbolCount(31)
    """ aSymbolObj.print_list() """
    """ aSymbolObj.set_number(54) """
    aSymbolObj.print_list()
    aSymbolObj.print_range(31)
    
    #aSymbolObj.print_symbols_to_file()
    aSymbolObj.get_symbol_data()