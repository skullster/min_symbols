#!/usr/bin/python

"""  TODO: Need a better name - change file name to reflect it whenever """
class Base(object):
   def __init__(self, base):
      self.base = base
      self.symbol_arr = [0]
      self.symbol_count = len( self.symbol_arr )

   def convert_number(self, number):
      self.symbol_arr[0] = number
      
      while self.base < self.symbol_arr[0]:
         print(self.symbol_arr[0], self.symbol_arr[0] % self.base)
         self.symbol_arr.insert(1,self.symbol_arr[0] % self.base)
         """ self.symbol_arr[0]-= self.symbol_arr[len(self.symbol_arr) - 1] """
         self.symbol_arr[0]-= self.symbol_arr[1]
         self.symbol_arr[0] = self.symbol_arr[0] // self.base
         
      """ Append the MS symbol """
      self.symbol_arr.reverse()
         
   def print_conversion(self):
      for symbol in self.symbol_arr:
         print(symbol)
         
   def get_symbol_count(self):
       self.symbol_count = len( self.symbol_arr )
       return self.symbol_count
      
if __name__ == "__main__":
    aBase = Base(16)
    aBase.convert_number(10311)
    aBase.print_conversion()
    
    no_symbs = aBase.get_symbol_count()
    print( no_symbs )