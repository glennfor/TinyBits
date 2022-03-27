##Question 2:
##Which algorithm would you use to detect and remove cycles from a Linked List?
##Problem: Consider a circular list below:
##
##Input:  ->0->1->2->3->4->5->6-->|
##           |-----------------------------------|
##
##Output: 0->1->2->3->4->5->6
##
##Use a standard algorithm to detect and break the cycle so the circular linked list
##becomes a singly linked list.
##


# SOLUTION


# create a node class

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# create linked list class
class LinkedList:
    def __init__(self):

        self.head = None

    def push(self, data):
        if not self.head:
            self.head = Node(data)
            return
        temp = self.head
        while (temp.next):
            temp = temp.next
        temp.next = Node(data)

    def printList(self):
        temp = self.head
        print("List of <<< {}".format(temp.data), end="")
        while (temp.next):
            temp = temp.next
            print(" ,{}".format(temp.data), end="")
        print(" >>>")

    def detectAndRemoveLoop(self):
        node = self.head
        container = set()
        container.add(node)
        while (node is not None) and (node.next not in container):
            container.add(node.next)
            node = node.next

        if node:
            # loop found: disconnect from the head
            node.next = None

    def formADummyLoop(self):
        '''method to create a delibrate loop in the list to test for cycle'''
        '''this method assumes that the list is at least 1 item long'''
        if not self.head:
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = self.head


# test

if __name__ == "__main__":

    print("CODE TESTING...\n")
    # create a list object
    newList = LinkedList()

    # push random items to a the list
    items = [0, 1, 2, 3, 4, 5, 6]

    for item in items:
        newList.push(item)

    newList.printList()

    # create a test loop
    newList.formADummyLoop();

    # detect and remove loop
    # this next line can be commented to see the actual implication of a cyclic list (ie infinite traversal)
    newList.detectAndRemoveLoop()

    # print list
    newList.printList()
