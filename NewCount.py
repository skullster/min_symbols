#!/usr/bin/python

"""  TODO: Need a better name - change file name to reflect it whenever """
"""  TODO: use a list of dictionaries - mult_a, mult_b and remainder keys """
class newCountList(object):
    def __init__(self, number):
        self.number = number
        self.count_list = []

    def create_count_list(self):
        prev_mult_a = 1
        cur_mult_a = 1
        cur_mult_b_sub = 1 
        remainder = 0
         
        while True :
            # Calculate the 2nd multiplier
            cur_mult_b = ((self.number - self.number % cur_mult_a) // cur_mult_a) - cur_mult_b_sub

            # Calculate the remainder
            remainder = self.number % cur_mult_a + cur_mult_a * cur_mult_b_sub
         
            # print("Break %d %d %d" % ( cur_mult_a, cur_mult_b, (cur_mult_a * cur_mult_b) ))
         
            # Create list and append to owning list - just for iterations 
            temp_list = [ cur_mult_a, cur_mult_b, remainder ]            
            self.count_list.append( temp_list )
        
            # Move onto the next subtractor
            cur_mult_b_sub += 1
         
            # Move onto the next multiplier ie when mult "b" is about to become the next mult "a"
            if ( cur_mult_b == cur_mult_a ):
                prev_mult_a = cur_mult_a
                cur_mult_a += 1
                cur_mult_b_sub = 1
                if ( (self.number % cur_mult_a) > 0 ):
                    cur_mult_b_sub = 0

                # Test the second multiplier
                test_mult_b = ((self.number - self.number % cur_mult_a) // cur_mult_a) - cur_mult_b_sub
            
                # Stop when mult b has already been used as mult_a - this is a repeat multiplication
                if ( prev_mult_a >= test_mult_b ):
                    break
               
                #print("%d %d" % ( cur_mult_a, cur_mult_b_sub ))

    def print_list(self):
        idx = 0
        for a_count in self.count_list :
            test_result = (a_count[0] * a_count[1]) + a_count[2]
            print("%2d : %2d x %2d + %2d = %d" % (idx, a_count[0], a_count[1], a_count[2], test_result ))
            idx+=1

if __name__ == "__main__":
    aNumber = newCountList(31)
    aNumber.create_count_list()
    aNumber.print_list()
      