
class Node():

    def __init__(self, input):
        self.data = input
        self.next = None


class Linked_List():

    def __init__(self, input):
        self.head = Node(input)
        self.tail = self.head
        self.length = 1

    def append(self, new_input):
        new_node = Node(new_input)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, new_input):
        new_node = Node(new_input)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insert(self, index, new_input,):
        new_node = Node(new_input)
        # check params
        if index == 0:
            self.prepend(new_input)
        elif index >= self.length - 1:
            self.append(new_input)
        else:
            cur = self.head
            i = 0
            while i < index-1:
                cur = cur.next
                i += 1
            new_node.next = cur.next
            cur.next = new_node
        self.length += 1

    def remove(self, index):
        if index >=  self.length - 1:
            index = self.length - 1
            
        cur = self.head
        i = 0 
        while i < index-1:
            cur = cur.next
            i += 1
        del_node = cur.next
        cur.next = del_node.next
        self.length -= 1

        # if index >=  self.length - 1:


    def __str__(self):
        cur = self.head
        link_list = ''
        while (cur != None):
            link_list += str(cur.data)
            if cur.next != None:
                link_list += '->'
            cur = cur.next
        return link_list


my_linked_list = Linked_List('apple')
my_linked_list.append(3)
my_linked_list.prepend(4)
my_linked_list.append(6)
# my_linked_list.insert(0, 'flower')
# my_linked_list.insert(5, 'flower')
# my_linked_list.insert(2, 'flower')
my_linked_list.remove(1)
# my_linked_list.remove(2)
print(my_linked_list)
