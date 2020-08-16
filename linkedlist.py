

# the Node class
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def get_data(self):
        return self.val

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next
    
# the Linkedlist class
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.count = 0
    
    def get_count(self):
        return self.count

    def insert(self, data):
        # TODO: insert a new node ahead of existing first node
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1

    def find(self, val):
        # TODO: find the first item with a given value
        item = self.head
        while (item != None):
            if item.get_data() == val:
                return item
            else:
                item = item.get_next()
        return None

    def deleteAt(self, idx):
        # TODO: delete an item at given index
        if idx > self.count-1:
            return
        if idx == 0:
            self.head = self.head.get_next()
        else:
            tempIdx = 0
            node = self.head
            while tempIdx < idx-1:
                node = node.get_next()
                tempIdx += 1
            node.set_next(node.get_next().get_next())
            self.count -= 1

    def dump_list(self):
        tempnode = self.head
        while (tempnode != None):
            print("Node: ", tempnode.get_data())
            tempnode = tempnode.get_next()

# Testing
itemList = LinkedList()
itemList.insert(38)
itemList.insert(23)
itemList.insert(5)
itemList.dump_list()

print("item count:", itemList.get_count())
print("finding item 13:", itemList.find(13))
print("finding item 5:", itemList.find(5))

itemList.deleteAt(2)
print("item count:", itemList.get_count())
print("finding item 38:", itemList.find(38))
itemList.dump_list()
