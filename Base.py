#!/usr/bin/python

"""  TODO: Need a better name - change file name to reflect it whenever """
class Base(object):
    def __init__(self, base):
        self.base = base
        self.symbol_arr = [0]
        self.symbol_count = len( self.symbol_arr )
    
    def convert_number(self, number):
        self.symbol_arr[0] = number
      
        while self.base - 1 < self.symbol_arr[0]:
            """ print(self.symbol_arr[0], self.symbol_arr[0] % self.base) """
            self.symbol_arr.insert(1,self.symbol_arr[0] % self.base)
            """ self.symbol_arr[0]-= self.symbol_arr[len(self.symbol_arr) - 1] """
            self.symbol_arr[0]-= self.symbol_arr[1]
            self.symbol_arr[0] = self.symbol_arr[0] // self.base
         
        """ Append the MS symbol """
        self.symbol_arr.reverse()
         
    def print_conversion(self):
        for symbol in reversed(self.symbol_arr):
            print(symbol,end=':')
        print(end='\n')
         
    def get_symbol_count(self):
        self.symbol_count = len( self.symbol_arr )
        return self.symbol_count
    
    """ get_range returns the range of the symbol count for the base. """
    """ The intention is to use this to reduce calculation effort.    """
    def get_range(self, symbol_count):
        min_range = 0
        max_range = 0

        if symbol_count > 0 :
            min_range = pow(self.base, symbol_count - 1)
            max_range = pow(self.base, symbol_count) - 1
         
        return [min_range, max_range]
      
if __name__ == "__main__":
    aBase = Base(2)
    """ 10311 """
    aBase.convert_number(1048576)
    aBase.print_conversion()
    
    no_symbs = aBase.get_symbol_count()
    print( no_symbs )
    
    range_list = aBase.get_range(39)
    
    print("%d %d" % (range_list[0], range_list[1]))