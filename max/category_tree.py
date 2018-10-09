from __future__ import print_function
import datetime
class Node(object):
    """Tree node: left and right child + data which can be any object"""

    def __init__(self, user_id):
        with open("block_cate_user.txt") as f:
            content = f.readlines()
            for j in range(0,len(content)):
                line = content[j].strip()
                id = int(line.split(",")[0])
                if user_id == id:
                    p = line.split(",")[1]
                    producer_freq = line.split(",[")[1].split("]")[0]
                    entity_freq = line.split("],[")[1].split("]")[0]
                    long = [p, producer_freq, entity_freq]
                    history = self.user_history(id)
                    short = []
                    for s in range(0,5):
                        short.append(int(history[s].split(":")[1].split(",")[0]))
                    self.user_id = user_id
                    self.p = p
                    self.long = long
                    self.short = short
                    self.history = history
                    self.child = None

    def print_node(self):
        print("summary of user ",self.user_id)
        print("probability: ",self.p)
        print("browsing history: ",self.history)
        print("long term list: ",self.long)
        print("short term window: ",self.short)
        print()

    def user_history(self, user_id):
        result = []
        with open("user_hist.txt") as f:
            content = f.readlines()
            for i in range(0,len(content)):
                if content[i].startswith(str(user_id)+":"):
                    result.append(content[i].strip())
        return result

    def insert(self, data):
        """Insert new node to the tree

        @param data node data object to insert
        """
        if self.child:
            cur = self.child
        else:
            self.user_id = data.user_id
            self.p = data.p
            self.long = data.long
            self.short = data.short
            self.history = data.history
            self.child = data.child

    def combine(self, node_1, node_2):
        node = Node(node_1.user_id+node_2.user_id)
        node.long = max(node_1.long, node_2.long)
        node.p = max(node_1.p, node_2.p)

def rec_score(self, query):
    result = 0
    # print(str_to_list(self.long[1]))
    result = float(self.long[0]) +  vec_time_vec(str_to_list(node_list[i].long[1]),query[0])+ vec_time_vec(str_to_list(node_list[i].long[2]),query[1])
    return result

def str_to_list(str):
    str_vec = str.split(",")
    int_vec = []
    for i in str_vec:
        int_vec.append(int(i))
    return int_vec

def vec_time_vec(v1,v2):
    rel = 0
    for i in range(0,len(v1)):
        rel = v1[i]*v2[i] + rel
    return  rel

query = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0]]
with open("b_block_cate_user.txt") as f:
    node_list = []
    print("building category-tree...")
    content = f.readlines()
    for j in range(0, len(content)):
        user_id = int(content[j].split(",")[0])
        user_node = Node(user_id)
        user_node.print_node()
        node_list.append(user_node)
    print("finished building!")
    print("top-k recommendation calculation...")
    print("query is: ", query)

    a = datetime.datetime.now()
    for i in range(0, 29):
        print(node_list[i].user_id,rec_score(node_list[i],query))
    b = datetime.datetime.now()
    print("category-tree query time: ",b-a)
    a = datetime.datetime.now()
    for i in range(0, len(node_list)):
        # print(node_list[i].user_id,rec_score(node_list[i],query))
        node_list[i].user_id
        rec_score(node_list[i], query)
    b = datetime.datetime.now()
    print("scan query time: ",b-a)