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

class SymbolCount(object):
    def __init__(self, number):
        self.number = number
        self.current_base = -1
        self.__get_base_range()
        self.number_list_obj = NL.NumberList(number)
        self.tracker_obj = MT.MinimumTracker()
        self.number_list_obj.create_number_list()
        self.symbol_range_list = []
        self.file_obj = None

    """ Private method """
    """ Gets the minimum and maximum bases for the given number """
    def __get_base_range(self):
        self.max_base = self.number
        
        """ TODO : is this a correct assumption ie is this the minimum starting point? """
        """ Get min base - base * base + base >= number """ 
        """ base * base + base = base(base +1 ) > base^2 """
        """ So get the closest square root - test and increment if less than number """
        min_base = math.floor(math.sqrt(self.number))
        
        while min_base * (min_base + 1) < self.number :
            min_base += 1
            
        self.min_base = min_base
        
    """ Get the symbol count ranges for the given base """
    """ Foreach base get the ranges for each symbol count, """
    """ starting at 1 through to the max possible symbols """ 
    def __symbol_count_for_base(self, base):
        self.current_base = base
        base_obj = B.Base(base)
        base_obj.convert_number( self.number - 1 )
        max_symbols = base_obj.get_symbol_count()
        
        symbol_idx = 1
        # Add a duff 0 entry - match the number of symbols to the index
        # It's a list of a minimum and maximum range for the base where
        # the index is the number of symbols
        self.symbol_range_list = [[0,0]]
        while symbol_idx <= max_symbols :
            self.symbol_range_list.append(base_obj.get_range(symbol_idx))
            symbol_idx += 1
            
    def __get_symbol_count(self):
        """ Base range list should be set up prior to calling this """
        """ Get base symbol data """
        self.__get_base_symbol_data(0)
                
    """ TODO: what is list_idx for?  just for initial set up ...."""    
    def __get_base_symbol_data(self, list_idx):
        mult_a_sym_cnt = -1
        mult_b_sym_cnt = -1
        rem_sym_cnt = -1
        
        mult_a = self.number_list_obj.number_list[list_idx][0]
        mult_b = self.number_list_obj.number_list[list_idx][1]
        remainder = self.number_list_obj.number_list[list_idx][2]

        #print( "Base symbols count %2d : %2d,  %2d,  %2d" % (list_idx, mult_a, mult_b, remainder ), file=self.file_obj )
        
        """ range idx matches symbol count - ignore 0 idx """
        cnt_idx = 1
        range_length = len(self.symbol_range_list)
        
        print( "Range length %d" % (range_length))
        while cnt_idx < range_length :
            min_range = self.symbol_range_list[cnt_idx][0]
            max_range = self.symbol_range_list[cnt_idx][1]
            if mult_a_sym_cnt < 0 :
                if mult_a >= min_range and mult_a <= max_range :
                    mult_a_sym_cnt = cnt_idx

            if mult_b_sym_cnt < 0 :
                if mult_b >= min_range and mult_b <= max_range :
                    mult_b_sym_cnt = cnt_idx
                    
            if rem_sym_cnt < 0 :
                if remainder >= min_range and remainder <= max_range :
                    rem_sym_cnt = cnt_idx
                    
            if mult_a_sym_cnt < 0 or mult_b_sym_cnt < 0 or rem_sym_cnt < 0 :
                cnt_idx += 1
            else:
                """ All done break from while """
                break
            
        """ Base symbols count """
        """ OK create lists of various minimums here """
        total = mult_a_sym_cnt + mult_b_sym_cnt + rem_sym_cnt
        
        print("TOTAL : %d" % (total))
        self.tracker_obj.add_object([mult_a_sym_cnt, mult_b_sym_cnt, rem_sym_cnt, self.current_base], total)
            
            
    def __get_minimum_symbol_data(self, list_idx):
        mult_a = self.number_list_obj.number_list[list_idx][0]
        mult_b = self.number_list_obj.number_list[list_idx][1]
        remainder = self.number_list_obj.number_list[list_idx][2]
        print( "Minimum sysmbols %2d : %2d x %2d + %2d" % (list_idx, mult_a, mult_b, remainder ), file=self.file_obj )
            
            
    def get_symbol_data(self):
        file_name = str(self.number) + '.txt'
        self.file_obj = open( file_name, 'w' )
        
        """ Set up the range list for the base """
        base = self.min_base
        self.__symbol_count_for_base(base)
        self.__get_symbol_count()
        for min_obj in self.tracker_obj.object_tracker_list :
            print( "Base symbols count a = %2d, b = %2d,  c = %2d, base : %2d" % (min_obj[0], min_obj[1], min_obj[2], min_obj[3]))

        self.file_obj.close()
        
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
        
    def print_range(self, base):
        self.__symbol_count_for_base(base)
        range_length = len(self.symbol_range_list)
        range_idx = 1
        while range_idx < range_length:
            print("Base %d: symbol count %d, min range %d max range %d" % (base, range_idx, self.symbol_range_list[range_idx][0], self.symbol_range_list[range_idx][1] ))
            range_idx += 1

    def print_range_temp(self, base):
        self.__symbol_count_for_base(base)
            
if __name__ == "__main__":
    aSymbolObj = SymbolCount(31)
    """ aSymbolObj.print_list() """
    """ aSymbolObj.set_number(54) """
    aSymbolObj.print_list()
    aSymbolObj.print_range(31)
    
    #aSymbolObj.print_symbols_to_file()
    aSymbolObj.get_symbol_data()