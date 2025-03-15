"""
This file contains functions for linked list operations like:
    *check if an element belongs
    *insert element
    *delete element
    *reverse linked list
    *find max/min values
    *print linked list (not functions, demostrated in examples)
"""

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

"""
belongs_to_the_linked_list - checks if an element with value==n exists in the linked list
    head - first element of the linked list
    n - element to search for
"""

def belongs_to_the_linked_list(head, n):
    if head is None:
        return "does not belong"
    elif head.val==n:
        return "belongs"
    else:
        return belongs_to_the_linked_list(head.next, n)
"""
head - first element of the linked list
value - value to insert
position - insertion position
ATTENTION!!!!
    if position = "beginning" - element becomes the new head
    if position = "end" - element becomes the last element
    if position = number (int/float) - insert after EVERY node with this value (value==position)
"""
def insert_element_to_the_linked_list(head, value, position):
    if not head: 
        return Node(value)
    current = head
    if position == "beginning":
        new_node = Node(value)
        new_node.next = head 
        return new_node 
    elif position == "end":
        new_node = Node(value)
        while current.next: 
            current = current.next
        current.next = new_node
        return head
    elif isinstance(position, (int, float)): 
        while current:
            if current.val == position:
                new_node = Node(value) #i have to create new node EVERYTIME when value=position
                new_node.next = current.next
                current.next = new_node
                current = new_node.next
            else:
                current = current.next
        return head
    return head
"""

"""
"""
Deletes ALL nodes with this value 
"""
def delete_element_from_the_linked_list(head, value):
    while head and head.val==value: #if element which i want to delete is a first element
        head = head.next
    if not head: #i have to check this after previous while because my linked list could have only head
        return None
    current = head
    while current.next:
        if current.next.val == value: #find element which is next to value which i want to delete
            current.next = current.next.next #now my finding element "point at" old next of deleted element
        else:
            current = current.next
    return head

def reverse_linked_list(head):
    prev = None
    current = head

    while current:
        tmp = current.next
        current.next = prev
        prev = current
        current = tmp
    return prev

def find_max_and_min_in_the_linked_list(head):
    current = head
    cur_max=float('-inf')
    cur_min=float('inf')
    while current:
        if current.val>cur_max:
            cur_max=current.val
        if current.val<cur_min:
            cur_min=current.val
        current = current.next
    return f"max is {cur_max}, min is {cur_min}"

#checking functions
head = Node(10)
head = insert_element_to_the_linked_list(head, 20, "beginning")
head = insert_element_to_the_linked_list(head, 4, "end")
head = insert_element_to_the_linked_list(head, 8, 10)
head = insert_element_to_the_linked_list(head, 8, 20)
head = insert_element_to_the_linked_list(head, 30, 8)


# print linked_list
current = head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")

print(belongs_to_the_linked_list(head, 10))
new_head = delete_element_from_the_linked_list(head, 10)
current = new_head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")              
print(find_max_and_min_in_the_linked_list(new_head)) 
