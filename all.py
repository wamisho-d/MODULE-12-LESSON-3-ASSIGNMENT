# Implementing a Singly Linked List in Python
# Task 1: Implement the Node class
class Node:
    def __init__(self, data):
        self.data = data # Stores the value of the node
        self.next = None # Points to the next node, initially None

# Task 2: Implement the SinglyLinkedList class
class SinglyLinkedList:
    def __init__(self):
        self.head = None # Head of the linked list, initially None

    # Insert a new node at the end of the list
    def insert(self, data):
        new_node = Node(data)
        if self.head is None: # If the list is empty, the new node becomes the head 
            self.head = new_node
        else:
            current = self.head
            while current.next: # Traverse to the last node
                current = current.next
            current.next = new_node # Append the new node at the end

     # Delete the first occurence of a node containing 'data'
    def delete(self, data):
        current = self.head
        if current is None: # If the list is empty
            print("List is empty, nothing to delete.")
            return
        if current.data == data: # If the head node contains the data to be deleted 
            self.head = current.next # Move the head to the next node
            current = None # Delete the current node
            return
        
        prev = None
        while current and current.data != data: # Traverse to find the node
            prev = current
            current = current.next
        
        if current is None: # Data not found in the list
            print(f"Node with data {data} not found.")
            return
        
        prev.next = current.next # Unlink the node to delete it
        current = None


    # Traverse the linked list and print each node's data
    def traverse(self):
        if self.head is None:
            print("The list is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "\n")
            current = current.next

# Task 3: Test the functionality
if __name__ == "__main__":
    # Create a new singly linked list
    linked_list = SinglyLinkedList()

    # Insert elements into the linked list
    linked_list.insert(10)
    linked_list.insert(20)
    linked_list.insert(30)
    linked_list.insert(40)

    print("Linked list after insertion:")
    linked_list.traverse()

    # Delete an element from the list
    print("\nDeleting 20:")
    linked_list.delete(20)
    linked_list.traverse()

    # Try to delete a non-existent element
    print("\nDeleting 100 (non-existent):")
    linked_list.delete(100)
    linked_list.traverse()

    # Delete the head element
    print("\nDeleting 10 (head):")
    linked_list.delete(10)
    linked_list.traverse()

    # Insert more elements
    print("\nInserting 50 and 60:")
    linked_list.insert(50)
    linked_list.insert(60)
    linked_list.traverse()

    
# Task 1: Node class to represent an individual node in a doubly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None  # Pointer to the previous node
        self.next = None  # Pointer to the next node

# Task 2: DoublyLinkedList class to manage the doubly linked list
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Points to the first node
        self.tail = None  # Points to the last node

    # Insert a node at the end of the list
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.tail is None:  # Empty list
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    # Insert a node at the start of the list
    def insert_at_start(self, data):
        new_node = Node(data)
        if self.head is None:  # Empty list
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # Delete a node with the given data
    def delete_node(self, data):
        if self.head is None:  # Empty list
            print("List is empty. No node to delete.")
            return

        current = self.head
        while current:
            if current.data == data:
                if current.prev:  # Node is not the head
                    current.prev.next = current.next
                else:  # Node is the head
                    self.head = current.next

                if current.next:  # Node is not the tail
                    current.next.prev = current.prev
                else:  # Node is the tail
                    self.tail = current.prev

                print(f"Deleted node with data: {data}")
                return
            current = current.next
        print(f"Node with data {data} not found.")

    # Traverse the list from head to tail
    def traverse_forward(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    # Traverse the list from tail to head
    def traverse_backward(self):
        result = []
        current = self.tail
        while current:
            result.append(current.data)
            current = current.prev
        return result

# Task 3: Test the DoublyLinkedList implementation
if __name__ == "__main__":
    dll = DoublyLinkedList()

    # Insert elements at the end
    dll.insert_at_end(10)
    dll.insert_at_end(20)
    dll.insert_at_end(30)

    # Insert elements at the start
    dll.insert_at_start(0)
    dll.insert_at_start(-10)

    print("Forward traversal:", dll.traverse_forward())  # Expected: [-10, 0, 10, 20, 30]
    print("Backward traversal:", dll.traverse_backward())  # Expected: [30, 20, 10, 0, -10]

    # Delete specific nodes
    dll.delete_node(0)  # Deleting the node with data '0'
    dll.delete_node(30)  # Deleting the tail node
    dll.delete_node(-10)  # Deleting the head node

    print("Forward traversal after deletions:", dll.traverse_forward())  # Expected: [10, 20]
    print("Backward traversal after deletions:", dll.traverse_backward())  # Expected: [20, 10]