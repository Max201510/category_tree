from __future__ import print_function

class Node(object):
    """Tree node: left and right child + data which can be any object"""
    entityNumber = 50
    producerNumber = 15
    category = 1

    def __init__(self, user_id):
        #get the user history by userId
        history = [[1,(1,2,3),1],[1,(4,2,3),0],[1,(4,2),2],[3,(1,5,3),1]]
        p = 0.8
        producer_freq = [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
        entity_freq = [0,1,2,2,0,0,1,2,2,0,0,1,2,2,0,0,1,2,2,0,0,1,2,2,0,0,1,2,2,0,0,1,2,2,0,0,1,2,2,0,0,1,2,2,0,0,1,2,2,0,]
        long = [p,producer_freq,entity_freq]
        short = [1,1,0,1,1]
        self.user_id = user_id
        self.p = p
        self.long = long
        self.short = short
        self.history = history

    def print_node(self):
        print("summary of user ",self.user_id)
        print("probability: ",self.p)
        print("browsing history: ",self.history)
        print("long term list: ",self.long)
        print("short term window: ",self.short)
        print()


user_1 = Node(1)
user_2 = Node(2)
user_1.print_node()
user_2.print_node()

