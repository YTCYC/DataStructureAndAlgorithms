
# class Node():

#     def __init__(self, input):
#         self.head = input
#         self.next = None
#         self.length = 1
#         # self.tail = self.head

#     def append(self, input):
#         self.next = input
#         self.next = None
#         self.length += 1

     
class Linked_List():

    def __init__(self,data):
        self.node = {"head": data, "next": None }
        self.tail = self.node
        self.length = 1

    def append(self, new_data):
        new_node = {"head": new_data, "next": None }
        # print(new_node)
        self.tail["next"] = new_node
        self.tail = new_node
        self.length += 1

    def traverse(self):
            cur = self.node
            while (cur != None):
                print(cur["head"])
                cur = cur["next"]
    

my_linked_list = Linked_List(1)
my_linked_list.append(2)
my_linked_list.traverse()