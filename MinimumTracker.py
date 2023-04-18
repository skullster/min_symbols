#!/usr/bin/python

"""  Create a list of given indices satisfying a given minimum non-zero metric """

class MinimumTracker(object):
    def __init__(self):
        """ Initialize to zero - metric will never be zero """
        self.minimum_metric = 0
        self.tracker_list = []

    def add_index(self, reference_idx, metric):
        if ( self.minimum_metric == 0 ):
            self.minimum_metric = metric
            self.tracker_list.append( reference_idx )
        elif ( self.minimum_metric >= metric ): 
            if ( self.minimum_metric > metric ):
                self.minimum_metric = metric
                """ Zero the array - a new minimum """
                self.tracker_list = []
            
            """ Add the reference to the list """
            self.tracker_list.append( reference_idx )   

    def print_list(self):
        print("Metric %d" % (self.minimum_metric))
        for an_idx in self.tracker_list :
            print("%d" % (an_idx))

if __name__ == "__main__":
    minTracker = MinimumTracker()
    minTracker.add_index(10, 6)
    minTracker.add_index(23, 4)
    minTracker.add_index(19, 100)
    minTracker.add_index(3, 4)
    
    minTracker.print_list()
      