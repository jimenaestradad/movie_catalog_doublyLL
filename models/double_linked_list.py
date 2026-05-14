
from models.node import Node

class DoubleLinkedList:
    def __init__(self):
        self.start = None
        self.end = None

    def __iter__(self):
        current = self.start

        while current is not None:
            yield current
            current = current.next

    def __len__(self):
        length = 0

        for _ in self:
            length += 1

        return length
    
    def __repr__(self):
        nodes = []

        for node in self:
            nodes.append(str(node.data))

        return " <--> ".join(nodes)
    
    def insert_at_beginning(self, element):
        if self.start is None:
            self.start = element
            self.end = element

        else:
            element.next = self.start
            self.start.prev = element
            self.start = element

    def insert_at_end(self, element):
        if self.end is None:
            self.start = element
            self.end = element

        else:
            self.end.next = element
            element.prev = self.end
            self.end = element
    
    def search(self, element_data):
        current = self.start
        while current is not None:
            if current.data == element_data:
                return current

            current = current.next

        return None
    
    def delete_node(self, element_data):
        node_to_delete = self.search(element_data)
        if node_to_delete is None:
            return

        if node_to_delete == self.start:
            self.start = node_to_delete.next

            if self.start is not None:
                self.start.prev = None

            else:
                self.end = None

  
        elif node_to_delete == self.end:
            self.end = node_to_delete.prev
            self.end.next = None


        else:
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev