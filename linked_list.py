class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node in the list.
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data

class LinkedList: 
    """
    Singly linked list
    """

    def __init__(self): 
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        """
        Returns the number of nodes in the list
        Takes 0(n) time
        """
        current = self.head
        count = 0
        while current:
            count = count + 1
            current = current.next_node
        
        return count


    def add(self, data):
        """
        Adds a new Node containing data at the head of the list
        Takes O(1) time
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        Search for the first node containing data that matches the key
        Returns the node or 'None' if not found

        Takes O(n) time / linear time
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def searchAtIndex(self, index):
        """
        Takes index as an argument and retuns the node at this 
        index node or 'Not found' if the index doesn't exist.
        Runs in linear time O(n)
        """
        current = self.head
        position = index
        found = False
        size = self.size()

        if index == 0:
            found = True
        elif index > 0:
            if index >= size:
                current = 'Not found'
            else:
                while current and not found:
                    if position == 0:
                        found = True
                    else:
                        current = current.next_node
                        position -= 1
        else:
            current = 'Not found'
        return current

    def insert(self, data, index):
        """
        Inserts a new Node containing data at index position
        Insertion takes O(1) time / constant time but finding 
        the node at the insertion point takes O(n) time / linear time

        Takes an overall O(n) time / linear time
        """

        if index == 0:
            self.add(data)

        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1
            
            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

    def remove(self, key):
        """
        Removes Node containing data that matches the key
        Returns the node or None if the key doesn't exist
        Takes O(n) time / linear time
        """
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current == self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        return current

    def removeAtIndex(self, index):
        """
        Takes an index to remove a node at, returning the 
        node that has been removed or 'Not found' if the 
        index doesn't exist.
        Runs using linear time O(n). 
        """
        size = self.size()
        found = False
        current = self.head

        if index == 0:
            found = True
            self.head = current.next_node
        elif index > 0:
            if index >= size:
                current = 'Not found'
            else:
                position = index
                current = self.head
                previous = None

                while current and position > 0 and not found:
                    previous = current
                    current = current.next_node
                    position -= 1

                if position == 0:
                    found = True
                    if index < size:
                        previous.next_node = current.next_node
                    else:
                        previous.next_node = None
        else:
            current = 'Not found'

        return current

    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_node
        return  '-> '.join(nodes)