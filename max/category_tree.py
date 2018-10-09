from __future__ import print_function

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


with open("block_cate_user.txt") as f:
    content = f.readlines()
    for j in range(0, len(content)):
        user_id = int(content[j].split(",")[0])
        user_node = Node(user_id)
        user_node.print_node()

