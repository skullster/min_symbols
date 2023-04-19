#!/usr/bin/python

"""  Create a list of given objects satisfying a given minimum non-zero metric """

class MinimumTracker(object):
    def __init__(self):
        """ Initialize to zero - metric will never be zero """
        self.minimum_metric = 0
        self.object_tracker_list = []

    def add_object(self, reference_obj, metric):
        if ( self.minimum_metric == 0 ):
            self.minimum_metric = metric
            self.object_tracker_list.append( reference_obj )
        elif ( self.minimum_metric >= metric ): 
            if ( self.minimum_metric > metric ):
                self.minimum_metric = metric
                """ Zero the array - a new minimum """
                self.object_tracker_list = []
            
            """ Add the reference to the list """
            self.object_tracker_list.append( reference_obj )   

    def print_list(self):
        print("Metric %d" % (self.minimum_metric))
        for an_idx in self.object_tracker_list :
            print("%d , %s" % (an_idx[0], an_idx[1]))

if __name__ == "__main__":
    minTracker = MinimumTracker()
    minTracker.add_object([10,"one"], 6)
    minTracker.add_object([23,"bill"], 4)
    minTracker.add_object([19,"JOBBY"], 100)
    minTracker.add_object([3, "slug"], 4)
    
    minTracker.print_list()
      